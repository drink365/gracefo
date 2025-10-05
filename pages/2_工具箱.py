
import streamlit as st

st.set_page_config(page_title="工具箱｜永傳家族傳承導師", page_icon="🧰", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
[data-testid="stSidebar"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

st.title("🧰 AI 工具箱")
st.caption("以下為可直接使用的工具與模組。若有新增模組，我可以幫你持續擴充。")

st.page_link("app.py", label="🏠 回首頁")

st.markdown("### 常用工具")
col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/5_AI工具｜遺產稅估算.py", label="AI 工具｜遺產稅估算", icon="🧮")
    st.page_link("pages/6_AI工具｜保單策略.py", label="AI 工具｜保單策略", icon="📄")
    st.page_link("pages/7_AI工具｜保單策略Plus.py", label="AI 工具｜保單策略Plus", icon="📈")
with col2:
    st.page_link("pages/8_AI工具｜價值觀探索.py", label="AI 工具｜價值觀探索", icon="🧭")
    st.page_link("pages/9_AI工具｜資產地圖.py", label="AI 工具｜資產地圖", icon="🗺️")

st.markdown("---")
st.caption("若需將工具體驗的結果，導向『預約 30 分鐘健檢』以提升轉換，我可以為各模組加入行動按鈕與事件追蹤。")

from src.utils.lead import render_lead_cta
render_lead_cta(page_name='工具箱')
