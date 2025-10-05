# app_config.py — central page config for Streamlit (applies to all pages)
import os
import streamlit as st
from app_config import ensure_page_config
ensure_page_config()

def ensure_page_config():
    # Set only once per app session
    if not st.session_state.get("_page_config_done", False):
        favicon_path = os.path.join(os.path.dirname(__file__), "favicon.png")
        try:
except Exception:
            # In case a subpage ran first and already set config, ignore
            pass
        st.session_state["_page_config_done"] = True
