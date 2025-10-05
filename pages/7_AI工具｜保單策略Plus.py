
import streamlit as st
from src.modules.insurance_planner_plus import render

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
render_lead_cta(page_name='7_AI工具｜保單策略Plus')

