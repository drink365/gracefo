
# app.py — Phase 1 Mini-Platform (Tax Calculator + Asset Map + Branded PDF)
# Author: ChatGPT for Grace Family Office
# Encoding: utf-8
import math
from datetime import datetime
from io import BytesIO

import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ---- Page Setup ----
st.set_page_config(page_title="AI 傳承策略平台｜第一階段", page_icon="📊", layout="wide")

# Global CSS (fonts + brand tone)
st.markdown(
    '''
    <style>
    :root {
        --brand-primary: #2B6CB0;   /* 深藍：專業信任 */
        --brand-accent:  #38B2AC;   /* 藍綠：科技安心 */
        --brand-cta:     #2563EB;   /* 藍色 CTA，避免刺眼紅 */
    }
    html, body, [class*="css"]  {
        font-family: "Noto Sans TC", "Microsoft JhengHei", "PingFang TC", "Heiti TC", "Helvetica", "Arial", sans-serif;
    }
    .brand-header {
        background: linear-gradient(100deg, var(--brand-primary), #1E3A8A);
        color: white;
        padding: 16px 20px;
        border-radius: 14px;
        margin-bottom: 12px;
    }
    .brand-footer {
        color: #4B5563;
        font-size: 13px;
        margin-top: 24px;
        border-top: 1px solid #E5E7EB;
        padding-top: 10px;
    }
    .cta a, .stButton>button {
        background: var(--brand-cta);
        color: white;
        border: none;
        padding: 10px 16px;
        border-radius: 10px;
        font-weight: 600;
    }
    .soft-card {
        background: #ffffff;
        border: 1px solid #E5E7EB;
        border-radius: 14px;
        padding: 16px;
    }
    .subtle {
        color: #6B7280;
        font-size: 14px;
    }
    </style>
    ''',
    unsafe_allow_html=True,
)

st.markdown(
    '''
    <div class="brand-header">
        <h2 style="margin:0;">讓家族對話更自然，讓傳承規劃更清晰</h2>
        <div class="subtle">想知道家族資產的稅務風險嗎？立即免費試算！</div>
    </div>
    ''',
    unsafe_allow_html=True,
)

# ---- Constants (TWD; 單位：萬元) ----
BASIC_EXEMPTION = 1333     # 基本免稅額 13,330,000
SPOUSE_DEDUCTION = 553     # 配偶扣除 5,530,000
CHILD_DEDUCTION = 56       # 直系卑親屬每人 560,000
PARENT_DEDUCTION = 138     # 直系尊親屬每人（最多 2 人） 1,380,000
PARENT_MAX_COUNT = 2
DISABLED_DEDUCTION = 693   # 身心障礙扣除每人 6,930,000
OTHER_DEP_DEDUCTION = 56   # 其他受扶養每人 560,000
FUNERAL_CAP = 138          # 喪葬費上限 1,380,000

# Estate tax brackets (萬元)
BRACKETS = [
    (5621, 0.10, 0),       # ≤ 56,210,000 → 10%
    (11242, 0.15, 281),    # 56,210,001–112,420,000 → 15%, 速算扣除 2,810,000
    (math.inf, 0.20, 843), # > 112,420,000 → 20%, 速算扣除 8,430,000
]

# Gift tax
GIFT_ANNUAL_EXEMPTION = 244   # 2,440,000
GIFT_BRACKETS = [
    (2811, 0.10, 0),
    (5621, 0.15, 281),
    (math.inf, 0.20, 843),
]

def calc_tax_from_brackets(tax_base_wan: float, brackets):
    if tax_base_wan <= 0:
        return 0.0
    for limit, rate, quick in brackets:
        if tax_base_wan <= limit:
            return max(0.0, tax_base_wan * rate - quick)
    return 0.0

def estate_tax_calc(
    assets_wan: float,
    debts_wan: float,
    funeral_wan: float,
    spouse: bool,
    child_count: int,
    parent_count: int,
    disabled_count: int,
    other_dep_count: int
):
    """Return dict with detailed estate tax calculation (unit: 萬元)."""
    gross = assets_wan
    deductible_funeral = min(max(funeral_wan, 0), FUNERAL_CAP)
    parent_count_capped = min(max(parent_count, 0), PARENT_MAX_COUNT)

    deductions = 0.0
    deductions += BASIC_EXEMPTION
    deductions += SPOUSE_DEDUCTION if spouse else 0
    deductions += max(child_count, 0) * CHILD_DEDUCTION
    deductions += parent_count_capped * PARENT_DEDUCTION
    deductions += max(disabled_count, 0) * DISABLED_DEDUCTION
    deductions += max(other_dep_count, 0) * OTHER_DEP_DEDUCTION
    deductions += max(debts_wan, 0)
    deductions += deductible_funeral

    taxable_base = max(0.0, gross - deductions)
    tax = calc_tax_from_brackets(taxable_base, BRACKETS)
    effective_rate = (tax / gross * 100.0) if gross > 0 else 0.0

    return {
        "總資產（萬）": gross,
        "債務（萬）": max(debts_wan, 0),
        "喪葬費（萬，封頂 138 萬）": deductible_funeral,
        "基本免稅額（萬）": BASIC_EXEMPTION,
        "配偶扣除（萬）": SPOUSE_DEDUCTION if spouse else 0,
        "直系卑親屬扣除（萬）": max(child_count, 0) * CHILD_DEDUCTION,
        "直系尊親屬扣除（萬）": parent_count_capped * PARENT_DEDUCTION,
        "身心障礙扣除（萬）": max(disabled_count, 0) * DISABLED_DEDUCTION,
        "其他受扶養扣除（萬）": max(other_dep_count, 0) * OTHER_DEP_DEDUCTION,
        "課稅遺產淨額（萬）": taxable_base,
        "遺產稅（萬）": tax,
        "平均稅負（%）": round(effective_rate, 2),
    }

def gift_tax_calc(gift_amount_wan: float):
    base = max(0.0, gift_amount_wan - GIFT_ANNUAL_EXEMPTION)
    tax = calc_tax_from_brackets(base, GIFT_BRACKETS)
    return {"贈與金額（萬）": gift_amount_wan, "免稅額（萬）": GIFT_ANNUAL_EXEMPTION, "課稅基礎（萬）": base, "應納贈與稅（萬）": tax}

# ---- Sidebar Navigation ----
st.sidebar.title("📍 導覽")
page = st.sidebar.radio("選擇功能", ["免費試算", "資產地圖", "報告輸出"], index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("**提示**：不直接賣保單，我們**先找出風險與缺口**，再提出完整方案。")

# ---- Shared Inputs (kept in session) ----
def asset_inputs():
    st.subheader("輸入資產（萬）｜六大分類")
    c1, c2, c3 = st.columns(3)
    with c1:
        company = st.number_input("公司股權", min_value=0.0, value=2000.0, step=10.0)
        realty  = st.number_input("不動產", min_value=0.0, value=3000.0, step=10.0)
    with c2:
        finance = st.number_input("金融資產（存款/股票/基金）", min_value=0.0, value=1500.0, step=10.0)
        policy  = st.number_input("保單（現金價值）", min_value=0.0, value=500.0, step=10.0)
    with c3:
        overseas = st.number_input("海外資產", min_value=0.0, value=800.0, step=10.0)
        other    = st.number_input("其他資產", min_value=0.0, value=200.0, step=10.0)
    total_assets = company + realty + finance + policy + overseas + other

    st.subheader("負債與支出（萬）")
    d1, d2, d3 = st.columns(3)
    with d1:
        debts = st.number_input("債務合計", min_value=0.0, value=300.0, step=10.0)
    with d2:
        funeral = st.number_input("喪葬費（上限 138 萬）", min_value=0.0, value=100.0, step=5.0)
    with d3:
        _ = st.text_input("備註（可留空）", value="")
    return total_assets, company, realty, finance, policy, overseas, other, debts, funeral

def household_inputs():
    st.subheader("家庭成員與扣除額條件")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        spouse = st.checkbox("有配偶", value=True)
        parents = st.number_input("直系尊親屬（0–2）", min_value=0, max_value=2, value=0, step=1)
    with c2:
        children = st.number_input("直系卑親屬（子女數）", min_value=0, value=2, step=1)
        disabled = st.number_input("身心障礙（人數）", min_value=0, value=0, step=1)
    with c3:
        others = st.number_input("其他受扶養（人數）", min_value=0, value=0, step=1)
    with c4:
        st.markdown('<div class="soft-card subtle">單位一律為「萬」，例如 3,000,000 元請輸入 300。</div>', unsafe_allow_html=True)
    return spouse, int(children), int(parents), int(disabled), int(others)

def show_footer():
    st.markdown(
        '''
        <div class="brand-footer">
        《影響力》傳承策略平台｜永傳家族辦公室<br/>
        https://gracefo.com　｜　聯絡信箱：123@gracefo.com
        </div>
        ''',
        unsafe_allow_html=True,
    )

# ---- Page: 免費試算 ----
if page == "免費試算":
    st.markdown("### AI 遺產稅／贈與稅 免費試算")
    st.markdown('<div class="subtle">不談產品，先幫您找出真正的缺口。</div>', unsafe_allow_html=True)

    total_assets, company, realty, finance, policy, overseas, other, debts, funeral = asset_inputs()
    spouse, children, parents, disabled, others = household_inputs()

    st.markdown("#### 遺產稅試算結果")
    estate = estate_tax_calc(
        assets_wan=total_assets,
        debts_wan=debts,
        funeral_wan=funeral,
        spouse=spouse,
        child_count=children,
        parent_count=parents,
        disabled_count=disabled,
        other_dep_count=others,
    )
    df_estate = pd.DataFrame(list(estate.items()), columns=["項目", "金額/數值"])
    st.dataframe(df_estate, use_container_width=True)

    st.markdown("#### 贈與稅快速試算")
    gift_amount = st.number_input("預計贈與金額（萬）", min_value=0.0, value=0.0, step=10.0)
    gift = gift_tax_calc(gift_amount)
    df_gift = pd.DataFrame(list(gift.items()), columns=["項目", "金額（萬）"])
    st.dataframe(df_gift, use_container_width=True)

    st.markdown("---")
    st.markdown("##### 顧問下一步建議（AI 草案）")
    tips = []
    if estate["遺產稅（萬）"] > 0:
        tips.append("考慮以壽險或慈善工具，部分覆蓋預估稅額，降低一次性資金壓力。")
    if overseas > 0:
        tips.append("海外資產建議評估身份／稅務居民影響，必要時結合信託或控股層。")
    if realty > total_assets * 0.4:
        tips.append("不動產占比高，建議評估流動性與稅務負擔，分期贈與或保單補位。")
    if not tips:
        tips.append("目前風險可控，建議建立年度檢視機制，確保家庭狀況與資產變動能即時反映。")
    st.write("• " + "\n• ".join(tips))

    show_footer()

# ---- Page: 資產地圖 ----
elif page == "資產地圖":
    st.markdown("### 家族資產傳承地圖（簡版）")
    total_assets, company, realty, finance, policy, overseas, other, debts, funeral = asset_inputs()

    st.markdown("#### 資產分布圖（圓餅）")
    labels = ["公司股權", "不動產", "金融資產", "保單", "海外資產", "其他資產"]
    values = [company, realty, finance, policy, overseas, other]

    # Pie chart with matplotlib (single chart, no explicit colors)
    fig1, ax1 = plt.subplots()
    def _fmt_pct(p):
        return f"{p:.1f}%" if p > 0 else ""
    ax1.pie(values, labels=labels, autopct=_fmt_pct, startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1, clear_figure=True)

    st.markdown("#### 資產金額長條圖")
    fig2, ax2 = plt.subplots()
    ax2.bar(labels, values)
    ax2.set_ylabel("金額（萬）")
    ax2.set_xticklabels(labels, rotation=0)
    st.pyplot(fig2, clear_figure=True)

    # Show table
    df_assets = pd.DataFrame({
        "資產類別": labels,
        "金額（萬）": values
    })
    st.dataframe(df_assets, use_container_width=True)

    show_footer()

# ---- Page: 報告輸出 ----
else:
    st.markdown("### AI 分析摘要（PDF 報告輸出）")
    st.markdown('<div class="subtle">自動整理重點，方便家族對話與顧問解讀。</div>', unsafe_allow_html=True)

    total_assets, company, realty, finance, policy, overseas, other, debts, funeral = asset_inputs()
    spouse, children, parents, disabled, others = household_inputs()

    estate = estate_tax_calc(
        assets_wan=total_assets,
        debts_wan=debts,
        funeral_wan=funeral,
        spouse=spouse,
        child_count=children,
        parent_count=parents,
        disabled_count=disabled,
        other_dep_count=others,
    )

    # Build PDF with reportlab (fallback to simple text if reportlab missing)
    def build_pdf_bytes():
        try:
            from reportlab.lib.pagesizes import A4
            from reportlab.pdfgen import canvas
            from reportlab.lib.units import mm
            from reportlab.lib import colors

            buffer = BytesIO()
            c = canvas.Canvas(buffer, pagesize=A4)
            w, h = A4

            # Header
            c.setFillColor(colors.white)
            c.rect(0, h-40, w, 40, stroke=0, fill=1)
            c.setFillColor(colors.HexColor("#1E3A8A"))
            c.rect(0, h-40, w, 40, stroke=0, fill=1)
            c.setFillColor(colors.white)
            c.setFont("Helvetica-Bold", 14)
            c.drawString(20*mm, h-28, "AI 分析摘要｜永傳家族傳承教練")

            # Title
            c.setFillColor(colors.black)
            c.setFont("Helvetica-Bold", 16)
            c.drawString(20*mm, h-60, "家族稅務風險與資產摘要")

            # Body
            c.setFont("Helvetica", 11)
            y = h-80
            lines = [
                f"報告時間：{datetime.now().strftime('%Y-%m-%d %H:%M')}",
                f"總資產：{estate['總資產（萬）']:.0f} 萬",
                f"遺產稅預估：{estate['遺產稅（萬）']:.0f} 萬（平均稅負 {estate['平均稅負（%）']:.2f}%）",
                f"課稅遺產淨額：{estate['課稅遺產淨額（萬）']:.0f} 萬",
                "扣除項目：",
                f"　基本免稅額：{BASIC_EXEMPTION:.0f} 萬" + ("；配偶扣除：%d 萬" % SPOUSE_DEDUCTION if estate['配偶扣除（萬）']>0 else ""),
                f"　卑親屬扣除：{estate['直系卑親屬扣除（萬）']:.0f} 萬；尊親屬扣除：{estate['直系尊親屬扣除（萬）']:.0f} 萬",
                f"　身心障礙扣除：{estate['身心障礙扣除（萬）']:.0f} 萬；其他受扶養：{estate['其他受扶養扣除（萬）']:.0f} 萬",
                f"　債務：{estate['債務（萬）']:.0f} 萬；喪葬費：{estate['喪葬費（萬，封頂 138 萬）']:.0f} 萬",
                "",
                "顧問下一步建議：",
            ]

            for line in lines:
                c.drawString(20*mm, y, line); y -= 16
                if y < 40*mm:
                    c.showPage(); y = h - 40*mm

            # Dynamic tips
            tips = []
            if estate["遺產稅（萬）"] > 0:
                tips.append("．以保單或慈善工具覆蓋部分稅額，降低一次性資金壓力。")
            if realty > total_assets * 0.4:
                tips.append("．調整不動產占比，提升資產流動性，避免分配爭議。")
            if overseas > 0:
                tips.append("．釐清身份與稅務居民狀態，必要時結合信託／控股。")
            if not tips:
                tips.append("．建立年度檢視機制，隨家庭與資產變動滾動調整。")
            for t in tips:
                c.drawString(20*mm, y, t); y -= 16

            # Footer
            c.setFont("Helvetica", 9)
            c.setFillColor(colors.HexColor("#6B7280"))
            c.drawString(20*mm, 15*mm, "《影響力》傳承策略平台｜永傳家族辦公室  ｜  https://gracefo.com  ｜  聯絡信箱：123@gracefo.com")
            c.save()
            pdf = buffer.getvalue()
            buffer.close()
            return pdf
        except Exception as e:
            # Fallback: plain text bytes
            txt = "AI 分析摘要（純文字備用）\n"
            for k, v in estate.items():
                if isinstance(v, float):
                    txt += f"{k},{v:.2f}\n"
                else:
                    txt += f"{k},{v}\n"
            return txt.encode("utf-8")

    pdf_bytes = build_pdf_bytes()
    st.download_button("⬇️ 下載 PDF 報告", data=pdf_bytes, file_name="ai_summary_report.pdf", mime="application/pdf")

    show_footer()
