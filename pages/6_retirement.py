import streamlit as st
# Anchor for CTA jump
st.markdown('<a id="booking"></a>', unsafe_allow_html=True)
# ---- Topbar (welcome + CTA) ----
_user_name = "Grace"
_user_expiry = "2026-12-31"
st.markdown(f"""
<div class="topbar">
  <div class="left">👋 歡迎回來，<b>{_user_name}</b>（到期日：{_user_expiry}）</div>
  <div class="right">
    <a href="#booking">預約 30 分鐘傳承健檢</a>
  </div>
</div>
""", unsafe_allow_html=True)
# ---- Global brand style & cleanup ----
st.markdown("""
<style>
/* Hide Sidebar & its toggle */
[data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="collapsedControl"] {
  display: none !important;
}
/* Hide default header buttons */
.stAppDeployButton, button[kind="header"], [data-testid="BaseButton-header"] {
  display: none !important;
}
:root {
  --brand:#145DA0; --accent:#2E8BC0; --gold:#F9A826; --bg:#F7FAFC; --ink:#1A202C;
}
html, body, .stApp { background: var(--bg); color: var(--ink); }
.topbar {
  display:flex; align-items:center; justify-content:space-between;
  padding:10px 16px; margin-bottom:8px; border-bottom:1px solid #E2E8F0; background:#fff; border-radius:12px;
}
.topbar .right a { margin-left:8px; text-decoration:none; padding:10px 16px; border-radius:999px; background:var(--brand); color:#fff; }
.topbar .right a:hover { background:#0F4D88; }
.section-card { background:#fff; border:1px solid #E2E8F0; border-radius:16px; padding:20px; }
.footer { color:#4A5568; font-size:14px; margin-top:40px; }
</style>
""", unsafe_allow_html=True)
from io import BytesIO
from datetime import date
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.units import mm
import os
from modules.cta_section import render_cta

# 頁面設定
st.set_page_config(
    page_title="樂活退休試算｜《影響力》傳承策略平台",
    page_icon="💰",
    layout="centered"
)

pdfmetrics.registerFont(TTFont('NotoSansTC', 'NotoSansTC-Regular.ttf'))

# 標題區
st.markdown("""
<div style='text-align: center;'>
    <h2>💰 樂活退休試算</h2>
    <p style='font-size: 18px; margin-top: -10px;'>由《影響力》傳承策略平台陪您看見未來，預作準備</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
《影響力》陪您一起看清未來 30 年的生活輪廓：

✅ 預估退休期間的年支出（生活、醫療、長照）  
✅ 了解目前資產是否足以支撐退休生活  
✅ 預測可能出現的財務缺口，提早準備、安心退休

💬 「退休不是結束，而是另一段人生的開始。」  
《影響力》提醒您，提早預備的每一步，都是為自己與家人創造安心與選擇的自由。

> 📌 本工具為初步估算，實際規劃仍需搭配個人財務諮詢
---
""")

# 使用者輸入
st.markdown("### 👤 基本資料")
age = st.number_input("目前年齡", min_value=30, max_value=80, value=55)
retire_age = st.number_input("預計退休年齡", min_value=50, max_value=80, value=60)
life_expectancy = st.number_input("預估壽命（活多久）", min_value=70, max_value=110, value=90)

st.markdown("### 💼 現有資產與報酬")
current_assets = st.number_input("目前可用於退休的總資產（萬元）", min_value=0, value=1000)
expected_return = st.slider("預期年報酬率（％）", 0.0, 10.0, 2.0, 0.1)

st.markdown("### 💸 預估年支出")
annual_expense = st.number_input("每年退休生活支出（萬元）", min_value=0, value=100)
annual_medical = st.number_input("每年醫療支出預估（萬元）", min_value=0, value=10)
annual_longterm = st.number_input("每年長照支出預估（萬元）", min_value=0, value=5)

# 試算邏輯
if st.button("📊 開始試算") or "calc_done" in st.session_state:
    st.session_state.calc_done = True
    total_years = life_expectancy - retire_age
    total_expense = total_years * (annual_expense + annual_medical + annual_longterm)
    total_assets_future = current_assets * ((1 + expected_return / 100) ** (retire_age - age))
    shortage = total_expense - total_assets_future

    st.markdown("---")
    st.markdown("### 📈 試算結果")
    st.markdown(f"預估退休年數：**{total_years} 年**")
    st.markdown(f"退休總支出：約 **{total_expense:,.0f} 萬元**")
    st.markdown(f"退休資產成長：約 **{total_assets_future:,.0f} 萬元**")
    st.markdown(f"退休資金缺口：約 **{shortage:,.0f} 萬元**")

    if shortage > 0:
        suggested_insurance = round(shortage * 1.05)
        st.warning(f"⚠️ 建議預留補強金額（含 5% 安全係數）：約 **{suggested_insurance:,.0f} 萬元**")
        st.markdown("""
💬 <i>《影響力》提醒：</i> 不用擔心，這正是開始規劃的好時機！  
- 您可以評估是否透過保險、年金或不動產現金流做補強  
- 建議進一步釐清資產配置與支出彈性，打造安心的退休現金流
""", unsafe_allow_html=True)
    else:
        st.success("✅ 恭喜！目前規劃的資產足以支應您的退休需求。")
        st.markdown("""
💬 <i>《影響力》提醒：</i> 即使足夠，也建議定期檢視，調整投資策略與風險控管，讓退休後生活更有彈性與餘裕。
""", unsafe_allow_html=True)

    # PDF 匯出功能
    st.markdown("---")
    st.markdown("### 📥 下載試算摘要（PDF）")

    def generate_pdf():
        buffer = BytesIO()
        logo_path = "logo.png"
        font_path = "NotoSansTC-Regular.ttf"
        pdfmetrics.registerFont(TTFont('NotoSansTC', font_path))

        styleN = ParagraphStyle(name='Normal', fontName='NotoSansTC', fontSize=12)
        styleH = ParagraphStyle(name='Heading2', fontName='NotoSansTC', fontSize=14, spaceAfter=10)
        styleC = ParagraphStyle(name='Center', fontName='NotoSansTC', fontSize=10, alignment=TA_CENTER)

        story = []
        if os.path.exists(logo_path):
            logo = Image(logo_path, width=80 * mm, height=20 * mm)
            logo.hAlign = 'CENTER'
            story.append(logo)
        story.append(Spacer(1, 12))
        story.append(Paragraph("樂活退休試算摘要", styleH))
        story.append(Paragraph(f"• 試算日期：{date.today()}", styleN))
        story.append(Paragraph(f"• 退休年齡：{retire_age} 歲", styleN))
        story.append(Paragraph(f"• 預估壽命：{life_expectancy} 歲", styleN))
        story.append(Paragraph(f"• 預估退休年數：{total_years} 年", styleN))
        story.append(Spacer(1, 6))
        story.append(Paragraph(f"• 退休總支出：約 {total_expense:,.0f} 萬元", styleN))
        story.append(Paragraph(f"• 資產成長預估：約 {total_assets_future:,.0f} 萬元", styleN))
        story.append(Paragraph(f"• 資金缺口：約 {shortage:,.0f} 萬元", styleN))
        if shortage > 0:
            story.append(Paragraph(f"• 建議補強金額：約 {suggested_insurance:,.0f} 萬元", styleN))
        story.append(Spacer(1, 12))
        story.append(Paragraph("《影響力》傳承策略平台｜永傳家族辦公室", styleC))
        story.append(Paragraph("https://gracefo.com", styleC))
        story.append(Paragraph("聯絡信箱：123@gracefo.com", styleC))

        doc = SimpleDocTemplate(buffer, pagesize=A4)
        doc.build(story)
        buffer.seek(0)
        return buffer

    st.download_button(
        label="📄 下載我的退休試算報告（PDF）",
        data=generate_pdf(),
        file_name="retirement_summary.pdf",
        mime="application/pdf"
    )

    render_cta()

# --- 聯絡資訊 ---
st.markdown("---")
st.markdown("""
<div style='display: flex; justify-content: center; align-items: center; gap: 1.5em; font-size: 14px; color: gray;'>
  <!-- 根路徑“/”會帶回到 app.py -->
  <a href='/' style='color:#006666; text-decoration: underline;'>《影響力》傳承策略平台</a>
  <a href='https://gracefo.com' target='_blank'>永傳家族辦公室</a>
  <a href='mailto:123@gracefo.com'>123@gracefo.com</a>
</div>
""", unsafe_allow_html=True)
