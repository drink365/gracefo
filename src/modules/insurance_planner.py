
import streamlit as st
from ..services.insurance import PolicyPlan, simulate_policy

def render():
    st.subheader("📦 保單策略規劃（示意版）")
    c1, c2, c3 = st.columns(3)
    with c1:
        annual_premium = st.number_input("年繳保費", min_value=0.0, step=10000.0, value=3_000_000.0, key="ip_ap")
    with c2:
        pay_years = st.number_input("繳費年期（年）", min_value=1, step=1, value=6, key="ip_py")
    with c3:
        factor = st.slider("90歲現價倍數（示意）", 1.0, 1.6, 1.25, 0.01, key="ip_factor")
    res = simulate_policy(PolicyPlan(annual_premium=annual_premium, pay_years=int(pay_years), projected_cash_value_factor=factor))
    st.write("—")
    colA, colB, colC = st.columns(3)
    colA.metric("總繳保費", f"{res['total_premium']:,.0f} 元")
    colB.metric("90歲現價（估）", f"{res['cash_value_90']:,.0f} 元")
    colC.metric("現價CP值（%）", f"{res['cp_cash_percent']:,.1f}%")
    st.caption("＊可擴充：贈與壓縮、指定受益、分期給付等情境模擬。")
