
import streamlit as st
from ..services.tax import EstateTaxInput, calc_estate_tax_progressive, DEFAULT_BRACKETS

def _fmt_twd(x: float) -> str:
    return f"{x:,.0f} 元"

def _fmt_pct(x: float) -> str:
    return f"{x*100:,.2f}%"

def render():
    st.subheader("🏛️ AI 秒算遺產稅（累進稅率）")

    with st.expander("輸入方式", expanded=True):
        mode = st.radio("選擇計算方式", ["快速模式（直接輸入淨遺產）", "完整模式（總額－債務－扣除）"], horizontal=True, key="et_mode")

    if mode.startswith("快速"):
        net_estate = st.number_input("淨遺產（元）", min_value=0.0, step=1_000_000.0, value=100_000_000.0, key="et_net_quick")
        total = None; debts = None; deductions = None
    else:
        c1, c2 = st.columns(2)
        with c1:
            total = st.number_input("遺產總額（元）", min_value=0.0, step=1_000_000.0, value=120_000_000.0, key="et_total")
            debts = st.number_input("負債／抵押（元）", min_value=0.0, step=1_000_000.0, value=10_000_000.0, key="et_debts")
        with c2:
            deductions = st.number_input("其他扣除（喪葬、特別扣除等，元）", min_value=0.0, step=500_000.0, value=0.0, key="et_deducts")
        net_estate = max(total - debts - deductions, 0.0)

    with st.expander("參數（可調整）", expanded=False):
        basic_ex = st.number_input("基本免稅額（元）", min_value=0.0, step=1_000_000.0, value=12_000_000.0, key="et_basic_ex")
        st.caption("＊其他扣除（配偶、撫養、喪葬、慈善等）請先在『完整模式』合併於扣除欄位。")

        st.write("累進稅率（區間上限／稅率）")
        # 可在 UI 動態調整各級門檻與稅率
        brackets = []
        for i, (thr, rate) in enumerate(DEFAULT_BRACKETS, start=1):
            col1, col2 = st.columns(2)
            with col1:
                thr_ui = st.number_input(f"第{i}級區間上限（元）", min_value=1_000_000.0, step=1_000_000.0,
                                         value=thr if thr != float('inf') else 100_000_000.0, key=f"et_thr_{i}")
            with col2:
                rate_ui = st.slider(f"第{i}級稅率（%）", 0.0, 100.0, rate*100, 0.5, key=f"et_rate_{i}") / 100.0
            if i < len(DEFAULT_BRACKETS):
                brackets.append((thr_ui, rate_ui))
            else:
                # 最高級無上限
                brackets.append((float('inf'), rate_ui))

    res = calc_estate_tax_progressive(EstateTaxInput(net_estate=net_estate, basic_exemption=basic_ex, brackets=brackets))

    # 結果卡片（不使用 st.metric，避免數字放大）
    st.markdown("### 結果")
    cA, cB, cC = st.columns(3)
    with cA:
        st.markdown("**應稅基**")
        st.markdown(f"<div class='kpi'>{_fmt_twd(res['taxable'])}</div>", unsafe_allow_html=True)
    with cB:
        st.markdown("**估算稅額**")
        st.markdown(f"<div class='kpi'>{_fmt_twd(res['tax'])}</div>", unsafe_allow_html=True)
    with cC:
        st.markdown("**有效稅率**")
        st.markdown(f"<div class='kpi'>{_fmt_pct(res['effective_rate'])}</div>", unsafe_allow_html=True)

    with st.expander("課稅級距明細", expanded=True):
        rows = res["details"]
        if rows:
            # 轉置成易讀表格
            table_rows = [{
                "區間": f"{_fmt_twd(r['區間起'])} ~ { '以上' if r['區間迄']==float('inf') else _fmt_twd(r['區間迄']) }",
                "稅率": _fmt_pct(r["稅率"]),
                "課稅額": _fmt_twd(r["課稅額"]),
                "稅額": _fmt_twd(r["稅額"]),
            } for r in rows]
            st.table(table_rows)
        else:
            st.info("無課稅明細（應稅基為 0）。")

    # 說明
    st.caption("""
＊本計算為示意用途，實務請依最新法規、扣除額類型與證明文件調整，並經專業顧問覆核。
    """)
