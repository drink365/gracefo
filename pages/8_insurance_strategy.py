# --- pages/8_insurance_strategy.py ---

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
from modules.insurance_logic import get_recommendations
from modules.pdf_generator import generate_insurance_strategy_pdf
from io import BytesIO

# 頁面設定
st.set_page_config(
    page_title="《影響力》保單策略規劃",
    page_icon="📦",
    layout="centered"
)

# 標題區
st.markdown("""
<div style='text-align: center; margin-top: 1em;'>
    <h2>📦 《影響力》保單策略規劃</h2>
    <p style='font-size: 18px; color: #666;'>為高資產家庭設計最適保障結構，讓每一分資源，都能守護最重要的事。</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# 步驟一：輸入條件
st.markdown("### 🔍 步驟一：輸入您的規劃條件")

age = st.number_input("年齡", min_value=18, max_value=90, value=45)
gender = st.radio("性別", ["女性", "男性"])
budget = st.number_input("預計投入金額（單位：萬元）", min_value=100, step=50)
currency = st.radio("預算幣別", ["台幣", "美元"])
pay_years = st.selectbox("繳費年期偏好", ["䠢繳", "6年期", "10年期", "15年期", "20年期"])

GOALS = ["稅源預備", "資產傳承", "退休現金流", "子女教育金", "重大醫療/長照", "資產保全與信託"]
selected_goals = st.multiselect("您的規劃目標（可複選）", GOALS)

if selected_goals:
    st.success("✅ 已選擇目標：" + "、".join(selected_goals))

# 步驟二：系統建議
if st.button("📌 取得建議策略組合"):
    st.markdown("---")
    st.markdown("### 🧩 步驟二：系統建議策略")

    recs = get_recommendations(age, gender, budget, pay_years, selected_goals)

    if recs:
        for r in recs:
            st.subheader(f"🎯 {r['name']}")
            st.markdown(f"**適合目標：** {'、'.join(r['matched_goals'])}")
            st.markdown(f"**組合結構說明：** {r['description']}")
            st.markdown("---")

        # PDF 下載
        pdf_bytes = generate_insurance_strategy_pdf(age, gender, budget, currency, pay_years, selected_goals, recs)
        st.download_button(
            label="📄 下載建議報告 PDF",
            data=pdf_bytes,
            file_name="insurance_strategy.pdf",
            mime="application/pdf"
        )
    else:
        st.info("尚未有符合條件的建議，請重新調整您的目標或條件。")

# 行動導引
st.markdown("---")
st.markdown("### 📬 想討論更進一步的保單設計？")
st.markdown("歡迎預約 1 對 1 專屬對談，讓我們陪您設計最安心的保障架構。")
st.markdown("👉 <a href='mailto:123@gracefo.com?subject=預約保單策略諮詢' target='_blank'>點我寄信預約對談</a>", unsafe_allow_html=True)

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
