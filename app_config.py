# app_config.py
import streamlit as st
from pathlib import Path

def ensure_page_config():
    fav = Path(__file__).parent / "favicon.png"
    st.set_page_config(
        page_title="永傳家族傳承導師｜影響力傳承平台",
        page_icon=str(fav) if fav.exists() else "📦",
        layout="wide",
        initial_sidebar_state="collapsed",  # ← 預設收起（搭配 config.toml = 不顯示）
    )
