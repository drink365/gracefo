
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

st.set_page_config(
    page_title="我是客戶｜《影響力》傳承策略平台",
    page_icon="🙋",
    layout="centered"
)

# --- 頁首區 ---
st.markdown("""
<div style='text-align: center;'>
    <h2>🙋 我的專屬傳承規劃工具</h2>
    <p style='font-size: 18px;'>從探索到設計，每一步都有我們陪你一起思考</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- 工具導覽 ---
st.markdown("### 🔍 我的傳承探索工具")

st.markdown("#### 🌿 1. 傳承風格探索")
st.write("透過風格測驗，了解您偏好的溝通方式與規劃重點。")
if st.button("🌿 開始探索我的風格", key="go_coach_client"):
    st.switch_page("pages/1_coach.py")

st.markdown("#### 🛡️ 2. 傳承風險盤點")
st.write("快速檢視六大潛在風險，讓您知道從哪裡開始規劃最重要。")
if st.button("🛡️ 檢視我的風險清單", key="go_risk_check_client"):
    st.switch_page("pages/9_risk_check.py")

st.markdown("#### 🗺️ 3. 資產結構與現金流模擬")
st.write("輸入您的資產分布，系統自動整理結構與風險建議。")
if st.button("🗺️ 建立我的資產圖", key="go_asset_map_client"):
    st.switch_page("pages/7_asset_map.py")

st.markdown("#### 📦 4. 保單策略設計")
st.write("根據年齡與需求，幫您模擬合適的保障組合與財稅結構。")
if st.button("📦 啟動我的保單模擬", key="go_insurance_client"):
    st.switch_page("pages/8_insurance_strategy.py")

st.markdown("#### 🧮 5. 稅務與退休試算")
st.write("了解未來的現金缺口與長期退休預備是否充足。")
col1, col2 = st.columns(2)
with col1:
    if st.button("🧮 AI秒算遺產稅", key="go_tax_client"):
        st.switch_page("pages/5_estate_tax.py")
with col2:
    if st.button("💰 樂活退休試算", key="go_retire_client"):
        st.switch_page("pages/6_retirement.py")

# 6. 不動產稅負試算
st.markdown("#### 🏠 6. 不動產稅負試算")
st.write("協助您試算未來不動產買賣或贈與/繼承的稅負情境。")
if st.button("🏠 AI秒算房產傳承稅負", key="go_real_estate_tax_client"):
        st.switch_page("pages/10_property.py")

# --- 聯絡資訊 ---
st.markdown("---")
st.markdown(
    """
    <div style='display: flex; justify-content: center; align-items: center; gap: 1.5em; font-size: 14px; color: gray;'>
      <a href='?' style='color:#006666; text-decoration: underline;'>《影響力》傳承策略平台</a>
      <a href='https://gracefo.com' target='_blank'>永傳家族辦公室</a>
      <a href='mailto:123@gracefo.com'>123@gracefo.com</a>
    </div>
    """,
    unsafe_allow_html=True
)
