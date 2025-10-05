
import streamlit as st

st.set_page_config(page_title="工具箱｜永傳家族傳承導師", page_icon="🧰", layout="wide")
st.title("🧰 AI 工具箱")
st.caption("以下為示意連結，可依您的實際模組整合。")

st.page_link("app.py", label="回首頁", icon="🏠")
st.markdown("")
st.link_button("AI 遺產稅估算（Demo）", "https://example.com")
st.link_button("保單策略模擬（Demo）", "https://example.com")
st.link_button("價值觀探索（Demo）", "https://example.com")
