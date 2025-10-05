
import streamlit as st
from src.modules.estate_tax import render

st.set_page_config(page_title="5_AI工具｜遺產稅估算", page_icon="🧰", layout="wide")
st.page_link("app.py", label="回首頁", icon="🏠")
render()
