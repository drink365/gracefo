
import streamlit as st
from src.modules.values_explorer import render

st.\1
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
render_lead_cta(page_name='8_AI工具｜價值觀探索')

