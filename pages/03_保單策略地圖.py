
import streamlit as st

st.set_page_config(page_title="📦 保單策略地圖（簡版）", page_icon="📦", layout="centered")
st.title("📦 保單策略地圖（簡版）")
st.caption("根據您的目標與預算，生成初步策略路線圖。")

goal = st.selectbox("您的主要目標", ["傳承（指定受益/避免爭執）", "現金流（退休/長照）", "稅源準備（遺產/贈與）"])
budget = st.number_input("預估年繳保費（新台幣）", min_value=0, step=100000, value=1000000)
term = st.selectbox("繳費年期", ["一次躉繳", "6年", "10年"])

if st.button("生成策略"):
    if goal == "傳承（指定受益/避免爭執）":
        plan = "建議以『傳承型終身壽』為核心，搭配受益人指定與變更要保人機制。"
    elif goal == "現金流（退休/長照）":
        plan = "建議以『現金流型終身壽/利變型年金』，兼顧現金流與保障。"
    else:
        plan = "建議設計『稅源準備保單』，確保繳稅資金與流動性到位。"

    st.success("初步策略建議")
    st.write(f"- 目標：{goal}\n- 年繳：{budget:,} 元\n- 年期：{term}\n- 策略：{plan}")
    st.info("下一步：帶著此結果，與顧問討論最合適的商品與條款設計。")
