import streamlit as st
# ---- Force-hide Sidebar & header buttons ----
st.markdown("""
<style>
/* Sidebar & its toggle */
[data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="collapsedControl"] { display: none !important; }
/* Header default buttons (Deploy/Settings/Rerun) */
.stAppDeployButton, button[kind="header"], [data-testid="BaseButton-header"], [data-testid="stToolbar"] { display: none !important; }
/* Ensure main stretches wide */
[data-testid="stAppViewContainer"] .main .block-container {
  max-width: 1600px; padding-left: 24px; padding-right: 24px;
}
</style>
""", unsafe_allow_html=True)

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
