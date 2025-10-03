
import streamlit as st
from ..config import BRAND, APP_TITLE, APP_SUBTITLE
from .components import page_footer
from ..utils.auth import login_block

def render_welcome_login():
    # Centered container
    st.markdown("<div style='height: 20px'></div>", unsafe_allow_html=True)
    col_logo, col_main, col_blank = st.columns([1,2,1])
    with col_logo:
        st.image(BRAND["logo_path"], use_container_width=True)
    with col_main:
        st.markdown(f"# {APP_TITLE}")
        st.markdown(f"#### {APP_SUBTITLE}")
        st.write("""- **這是什麼？** AI 導師式傳承平台：把資產盤點、遺／贈稅試算、保單策略、價值觀探索整合在一起。  
- **誰適合？** 高資產家庭／企業主；保險與財稅顧問（B2B2C）。  
- **能帶來什麼？** 更安心的可視化方案、節省時間的提案神器、專業與信任的快速建立。
""")
        st.info("🔑 測試帳號：帳號 **demo** ／ 密碼 **demo123**")

    st.markdown("---")
    # Login form
    login_block()
    page_footer()
