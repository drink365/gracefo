
import streamlit as st
from src.modules.insurance_planner import render

st.set_page_config(page_title="6_AI工具｜保單策略", page_icon="🧰", layout="wide")
st.page_link("app.py", label="回首頁", icon="🏠")
render()
