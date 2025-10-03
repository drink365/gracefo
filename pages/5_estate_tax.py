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
from modules.tax_constants import TaxConstants
from modules.tax_calculator import EstateTaxCalculator
from modules.estate_tax_ui import render_estate_tax_ui
from modules.cta_section import render_cta

# 頁面設定
st.set_page_config(
    page_title="AI秒算遺產稅｜《影響力》傳承策略平台",
    page_icon="🧮",
    layout="wide"
)

# 標題與說明
st.markdown("""
<div style='text-align: center; margin-top: 1em;'>
    <h1 style='font-size: 36px;'>🧮 AI秒算遺產稅</h1>
    <p style='font-size: 20px; color: #555;'>快速預估潛在稅負，提前預備稅源，守住資產轉移的關鍵</p>
    <br>
</div>
""", unsafe_allow_html=True)

# 說明文字區塊
st.markdown("""
- 本工具為高資產家庭設計的簡易試算系統，可協助您快速掌握未來可能面對的遺產稅與現金缺口。
- 試算結果僅供參考，實際稅額將依各國法令與個別申報內容為準，建議搭配專業顧問進行進一步規劃。
""")

st.markdown("---")

# 啟用試算模組
constants = TaxConstants()
calculator = EstateTaxCalculator(constants)
render_estate_tax_ui(calculator)

# 行動導引 CTA
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
