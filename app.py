
import streamlit as st
from src.config import APP_TITLE, APP_ICON, APP_LAYOUT, BRAND
from src.ui.components import hide_streamlit_chrome, topbar, page_footer
from src.utils.state import init_state
from src.utils.auth import login_block, get_user

from src.modules import estate_tax, insurance_planner, asset_map, values_explorer

st.set_page_config(page_title=APP_TITLE, page_icon=APP_ICON, layout=APP_LAYOUT)

hide_streamlit_chrome()
init_state()

user = get_user()
if not user:
    ses = login_block()
    st.stop()

topbar(user.display_name, user.end_date, BRAND["logo_path"])

tab1, tab2, tab3, tab4 = st.tabs([
    "🏛️ 遺產稅試算", "📦 保單規劃", "🗺️ 傳承圖", "💛 價值觀探索"
])

with tab1:
    estate_tax.render()
with tab2:
    insurance_planner.render()
with tab3:
    asset_map.render()
with tab4:
    values_explorer.render()

page_footer()
