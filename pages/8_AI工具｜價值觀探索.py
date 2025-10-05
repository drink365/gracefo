
import streamlit as st
from src.modules.values_explorer import render

st.set_page_config(page_title="8_AI工具｜價值觀探索", page_icon="🧰", layout="wide")
st.page_link("app.py", label="回首頁", icon="🏠")
render()
