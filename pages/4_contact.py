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
    page_title="聯絡我們｜《影響力》傳承策略平台",
    page_icon="📬",
    layout="centered"
)

# 頁首標題
st.markdown("""
<div style='text-align: center;'>
    <h1 style='font-size: 36px;'>📬 聯絡我們</h1>
    <p style='font-size: 16px; color: gray;'>歡迎與《影響力》團隊聯繫，我們樂意陪伴您思考、設計屬於自己的傳承策略。</p>
</div>
""", unsafe_allow_html=True)

# 聯絡資訊區塊
st.markdown("---")
st.markdown("""
### 📧 電子信箱  
若您有任何疑問，或想預約一對一對談，請來信：  
<a href="mailto:123@gracefo.com">123@gracefo.com</a>

### 🌐 官方網站  
更多關於我們的介紹與服務內容，歡迎造訪：  
<a href="https://gracefo.com" target="_blank">https://gracefo.com</a>

### 📌 公司資訊  
永傳家族辦公室｜永傳科創股份有限公司  
台北市中山區南京東路二段 101 號 9 樓

---

我們重視每一位用戶的提問與回饋，  
期盼成為您在傳承旅程中的陪伴者與策略夥伴。
""", unsafe_allow_html=True)

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
