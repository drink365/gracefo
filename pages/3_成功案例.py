
import streamlit as st

st.\1
st.markdown("""
<style>
/* Hide and remove the sidebar completely */
[data-testid="stSidebar"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

st.title("🏆 成功案例")
st.write("以下為去識別化示意，真實專案將於簽署保密條款後進行。")

st.markdown("**案例 A｜高齡長輩 5 億保額規劃**")
st.markdown("- 目標：減輕未來稅負、指定受益三代、婚前財產隔離")
st.markdown("- 作法：要保人／被保人／受益人分層設計，搭配逐年贈與與壓縮策略")
st.markdown("- 結果：達成跨代保障與現金流秩序，法律稅務合規")

st.markdown("---")
st.markdown("**案例 B｜創辦人股權與現金流分配**")
st.markdown("- 目標：保障經營權與家人生活品質")
st.markdown("- 作法：股權信託＋保單分期給付")
st.markdown("- 結果：避免爭產風險，建立家族共識")
