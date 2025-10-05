
import streamlit as st
from src.modules.insurance_planner_plus import render

st.set_page_config(page_title="7_AI工具｜保單策略Plus", page_icon="🧰", layout="wide")
st.page_link("app.py", label="回首頁", icon="🏠")
render()
