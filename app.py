
import streamlit as st
from src.config import APP_TITLE, APP_ICON, APP_LAYOUT, BRAND
from src.ui.components import hide_streamlit_chrome, topbar, page_footer
from src.ui.login import render_welcome_login
from src.ui.typography import setup_cjk_font
from src.utils.state import init_state
from src.utils.auth import login_block, get_user

from src.modules import estate_tax, insurance_planner, insurance_planner_plus, asset_map, asset_map_export, values_explorer

st.set_page_config(page_title=APP_TITLE, page_icon="assets/favicon.png", layout=APP_LAYOUT)

hide_streamlit_chrome()
setup_cjk_font("assets/NotoSansTC-Regular.ttf")
init_state()

user = get_user()
if not user:
    render_welcome_login()
    st.stop()

topbar(user.display_name, user.end_date, BRAND["logo_path"])

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏛️ 遺產稅試算", "📦 保單規劃（基礎）", "📦 贈與壓縮＋分期給付", "🗺️ 傳承圖", "🗺️ 構成輸出", "💛 價值觀探索"
])

with tab1:
    estate_tax.render()
with tab2:
    insurance_planner.render()
with tab3:
    insurance_planner_plus.render()
with tab4:
    asset_map.render()
with tab5:
    asset_map_export.render()
with tab6:
    values_explorer.render()

page_footer()
