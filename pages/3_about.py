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
    page_title="關於我們｜《影響力》傳承策略平台",
    page_icon="🌿",
    layout="centered"
)

# --- 頁首標題 ---
st.markdown("""
<div style='text-align: center;'>
    <h1 style='font-size: 36px;'>🌿 關於《影響力》</h1>
    <p style='font-size: 18px; color: gray;'>我們為什麼打造這個平台？</p>
</div>
""", unsafe_allow_html=True)

# --- 品牌介紹 ---
st.markdown("""
《影響力》是一個專為高資產家庭打造的互動式傳承策略平台，  
由永傳家族辦公室開發設計，結合專業洞見與數位工具，陪伴每一位家族掌舵者整理思緒、釐清方向。

我們相信，傳承不是填寫表格或購買商品，  
而是一段從心出發、由內而外的對話旅程。  
透過精心設計的探索模組，您將逐步形成屬於自己的「影響力藍圖」。

---

### 🧭 我們為什麼要打造這個平台？

在多年與高資產家庭互動的過程中，我們發現：  
許多創辦人早已在思考退休、資產安排、家庭關係與精神傳承，  
只是欠缺一個好起點，把這些想法整理並轉化成具體行動。

我們希望這個平台能成為那個「好起點」，  
在安靜的陪伴中，引導出屬於您的價值與選擇，  
讓影響力的延續，不再只是「有一天要做的事」。

---

### 🏛️ 關於永傳家族辦公室

永傳家族辦公室專注於高資產家庭的資產傳承與架構設計，  
整合財稅、法律、保險與治理團隊，  
為客戶量身訂製穩健永續的傳承策略。

我們擅長在「關係」與「制度」之間，找出最合適的平衡點，  
協助創辦人從容交棒，也幫助新一代建立自信與定位，承接使命。

📌 官方網站：<a href="https://gracefo.com" target="_blank">https://gracefo.com</a>  
📧 聯絡信箱：<a href="mailto:123@gracefo.com">123@gracefo.com</a>
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
