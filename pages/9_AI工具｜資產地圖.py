
import streamlit as st
from src.modules.asset_map import render


st.markdown("""
<style>
/* Hide and remove the sidebar completely */
[data-testid="stSidebar"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

st.page_link("app.py", label="回首頁", icon="🏠")
render()

from src.utils.lead import render_lead_cta
render_lead_cta(page_name='9_AI工具｜資產地圖')

