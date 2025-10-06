
import streamlit as st

st.set_page_config(page_title="🧮 遺產稅試算（簡版）", page_icon="🧮", layout="centered")
st.title("🧮 遺產稅試算（簡版）")
st.caption("此結果僅為教育性試算，實務需依個案由專業顧問確認。")

net_estate = st.number_input("預估淨遺產（新台幣）", min_value=0, step=1000000, value=50000000)
exemption = st.number_input("免稅額（新台幣）", min_value=0, step=1000000, value=13300000)
rate = st.slider("名目稅率（%）", min_value=0, max_value=30, value=10, step=1)

tax_base = max(0, net_estate - exemption)
tax = int(tax_base * (rate/100))

st.metric("試算稅基", f"{tax_base:,} 元")
st.metric("試算稅額", f"{tax:,} 元")

st.info("提示：可用保單作為『稅源準備』與『流動性』工具，避免資產被動變現。")
