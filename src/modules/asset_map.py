import streamlit as st

def render():
    # Initialize storage for asset items on first run
    if "asset_items" not in st.session_state:
        st.session_state.asset_items = []
    st.subheader("🗺️ 傳承圖／資產盤點（示意）")
    st.write("在此可建立六大資產分類、風險標籤與傳承箭線。")
    with st.expander("新增資產項目"):
        name = st.text_input("名稱", key="am_name")
        cat = st.selectbox("分類", ["公司股權", "不動產", "金融資產", "保單", "海外資產", "其他資產"], key="am_cat")
        val = st.number_input("估值", min_value=0.0, step=1000000.0, key="am_val")
        if st.button("加入清單", key="am_add"):
            if name:
                st.session_state.asset_items.append({"name": name, "cat": cat, "val": val})
    # Always show a table; if empty, show an empty placeholder row header
    if len(st.session_state.asset_items) == 0:
        st.info("目前尚無資料，請從上方『新增資產項目』加入。")
        st.table([{"name": "（示例）創辦人股份", "cat": "公司股權", "val": 0}])
    else:
        st.table(st.session_state.asset_items)
    st.caption("＊後續可視覺化為傳承地圖，並輸出 PDF / PNG。")
