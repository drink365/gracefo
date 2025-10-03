
import streamlit as st
from typing import Optional
from ..config import BRAND

def hide_streamlit_chrome():
    hide_css = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display:none !important;}
    div[data-testid="collapsedControl"] {display:none !important;}
    </style>
    """
    st.markdown(hide_css, unsafe_allow_html=True)

def topbar(name: str, end_date: str, logo_path: Optional[str] = None):
    cols = st.columns([1,6,2])
    with cols[0]:
        if logo_path:
            st.image(logo_path, use_container_width=True)
    with cols[1]:
        st.markdown(f"### 😊 歡迎，**{name}**  ｜  帳號有效期限：**{end_date}**")
    with cols[2]:
        st.write("")


def normalize_numbers_css():
    # 縮小數字樣式（包含 st.metric 的值），並為自訂 KPI 設計一般文字大小
    st.markdown("""
    <style>
    div[data-testid="stMetricValue"] { font-size: 1rem !important; }
    div[data-testid="stMetricLabel"] { font-size: 0.9rem !important; }
    .kpi { font-size: 1.15rem; font-weight: 600; line-height: 1.2; }
    </style>
    """, unsafe_allow_html=True)

def page_footer():

    st.write("---")
    st.caption(BRAND["footer"])
