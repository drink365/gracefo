
import streamlit as st
from src.modules.asset_map import render

st.set_page_config(page_title="9_AI工具｜資產地圖", page_icon="🧰", layout="wide")
st.page_link("app.py", label="回首頁", icon="🏠")
render()
