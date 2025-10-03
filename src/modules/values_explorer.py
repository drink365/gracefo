
import streamlit as st

def render():
    st.subheader("💛 價值觀探索（簡版）")
    st.write("請從下列詞語中選出 3–5 個最重要的價值：")
    opts = ["守護家人", "財務確定性", "教育傳承", "公益影響力", "企業永續", "世代和諧"]
    picks = st.multiselect("價值觀", options=opts, key="vx_picks")
    if picks:
        st.success("你的價值主軸：" + "、".join(picks))
        st.caption("＊接續將價值觀連結到策略與商品模組（價值觀 → 策略 → 商品）。")
