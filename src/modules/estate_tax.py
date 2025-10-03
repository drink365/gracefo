
import streamlit as st
from ..services.tax import EstateTaxInput, calc_estate_tax

def render():
    st.subheader("🏛️ 遺產稅即時試算")
    col1, col2 = st.columns(2)
    with col1:
        net_estate = st.number_input("淨遺產（元）", min_value=0.0, step=1_000_000.0, value=100_000_000.0, key="et_net")
        exemption = st.number_input("免稅額（元）", min_value=0.0, step=1_000_000.0, value=12_000_000.0, key="et_ex")
    with col2:
        rate = st.slider("稅率（%）", 10, 30, 20, 1, key="et_rate")
        rate = rate / 100.0
    res = calc_estate_tax(EstateTaxInput(net_estate=net_estate, exemption=exemption, rate=rate))
    st.metric("應稅基", f"{res['taxable']:,.0f} 元")
    st.metric("估算稅額", f"{res['tax']:,.0f} 元")
    st.metric("有效稅率", f"{res['effective_rate']*100:,.2f}%")
    st.info("＊此為簡化示意，實務請依最新法規與財稅顧問審閱。")
