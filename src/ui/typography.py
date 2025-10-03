
import streamlit as st
import matplotlib
from matplotlib import font_manager

def setup_cjk_font(ttf_path: str = "assets/NotoSansTC-Regular.ttf"):
    """Register CJK font for both Streamlit (CSS) and Matplotlib."""
    # Streamlit body font via CSS
    st.markdown(f'''
        <style>
        @font-face {{
            font-family: "Noto Sans TC";
            src: url("{ttf_path}") format("truetype");
            font-weight: normal;
            font-style: normal;
        }}
        html, body, [class*="css"] {{
            font-family: "Noto Sans TC", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol" !important;
        }}
        </style>
    ''', unsafe_allow_html=True)

    # Matplotlib font for charts
    try:
        fp = font_manager.FontProperties(fname=ttf_path)
        matplotlib.rcParams["font.family"] = fp.get_name()
        matplotlib.rcParams["axes.unicode_minus"] = False  # show minus properly in CJK
    except Exception:
        # Fallback silently if font not found
        pass
