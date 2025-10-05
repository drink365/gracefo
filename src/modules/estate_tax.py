
import streamlit as st

# === 固定參數（依現行公告數值，NTD） ===
EXEMPTION = 13_330_000      # 基本免稅額
FUNERAL   = 1_380_000       # 喪葬費
# 每人扣除額（標準模式，僅填人數即可）
SPOUSE_DED = 5_530_000      # 配偶扣除額／每人
CHILD_DED  = 560_000        # 子女／孫子女 扣除額／每人
PARENT_DED = 1_380_000      # 父母 扣除額／每人

# 累進級距（上限、稅率）
# 0～56,210,000 → 10%；56,210,000～112,420,000 → 15%；>112,420,000 → 20%
BRACKETS = [
    (56_210_000, 0.10),
    (112_420_000, 0.15),
    (float("inf"), 0.20),
]

def _calc_progressive_tax(taxable: float) -> float:
    remain = taxable
    last_cap = 0.0
    tax = 0.0
    for cap, rate in BRACKETS:
        if remain <= 0:
            break
        band = min(remain, cap - last_cap)
        if band > 0:
            tax += band * rate
            remain -= band
        last_cap = cap
    return max(0.0, tax)

def render():
    st.set_page_config(page_title="AI 工具｜遺產稅估算（標準模式）", page_icon="🧮", layout="wide", initial_sidebar_state="collapsed")
    st.markdown("""<style>[data-testid='stSidebar']{display:none!important;}section[data-testid='stSidebar']{display:none!important;}</style>""", unsafe_allow_html=True)

    st.title("🧮 遺產稅估算（標準模式／固定法規）")
    st.caption("免稅額、喪葬費、每人扣除額與稅率級距皆固定；只需輸入金額與人數。")

    colA, colB = st.columns(2)
    with colA:
        gross = st.number_input("遺產總額（NTD）", min_value=0.0, step=1_000_000.0, format="%.0f")
        debts = st.number_input("債務與其他扣除（NTD）", min_value=0.0, step=100_000.0, format="%.0f",
                                help="如醫療費、合法債務、慈善等符合規定之扣除。")
    with colB:
        st.markdown("**家屬扣除（僅填人數）**")
        spouse_n = st.number_input("配偶（人）", min_value=0, max_value=1, step=1, value=0)
        child_n  = st.number_input("子女／孫子女（人）", min_value=0, step=1, value=0)
        parent_n = st.number_input("父母（人）", min_value=0, step=1, value=0)

    st.markdown("""---""")
    st.subheader("📌 固定法規參數（不可修改）")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("基本免稅額", f"{EXEMPTION:,.0f}")
        st.metric("喪葬費", f"{FUNERAL:,.0f}")
    with col2:
        st.write("**每人扣除額**")
        st.table({
            "項目": ["配偶", "子女／孫子女", "父母"],
            "每人金額（NTD）": [f"{SPOUSE_DED:,.0f}", f"{CHILD_DED:,.0f}", f"{PARENT_DED:,.0f}"]
        })
    with col3:
        st.write("**級距與稅率**")
        st.table({
            "區間上限（NTD）": ["56,210,000", "112,420,000", "∞"],
            "稅率": ["10%", "15%", "20%"]
        })

    family_deductions = spouse_n * SPOUSE_DED + child_n * CHILD_DED + parent_n * PARENT_DED
    total_deductions = EXEMPTION + FUNERAL + debts + family_deductions
    taxable_base = max(0.0, gross - total_deductions)
    tax = _calc_progressive_tax(taxable_base)

    st.markdown("""---""")
    st.subheader("🧾 試算結果")
    colR1, colR2, colR3 = st.columns(3)
    with colR1:
        st.metric("遺產總額", f"{gross:,.0f}")
    with colR2:
        st.metric("可扣除總額", f"{total_deductions:,.0f}")
        st.caption(f"(含免稅額 {EXEMPTION:,.0f}、喪葬費 {FUNERAL:,.0f}、債務/其他 {debts:,.0f}、家屬扣除 {family_deductions:,.0f})")
    with colR3:
        st.metric("課稅基礎", f"{taxable_base:,.0f}")
        st.metric("估算稅額", f"{tax:,.0f}")

    st.caption("此為示意估算，級距與扣除額依現行公告；實務仍以主管機關規定與申報文件為準。")
