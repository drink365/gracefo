
import streamlit as st

def init_state():
    defaults = {"asset_items": []}
    for k,v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
