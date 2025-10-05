
import streamlit as st

st.\1
st.markdown("""
<style>
/* Hide and remove the sidebar completely */
[data-testid="stSidebar"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

st.title("🤝 關於與聯絡")

st.markdown("我們以人為本，結合國際法稅與保險策略，協助高資產家族完成跨世代傳承。")

st.markdown("**品牌主張**")
st.markdown("- 專業 × 溫暖 × 信任")
st.markdown("- 準備與從容：把愛與資產，放心交棒")

st.markdown("---")
st.subheader("聯絡方式")
st.markdown("Email：123@gracefo.com")
st.markdown("網站：gracefo.com（示意）")
