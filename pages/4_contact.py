# pages/4_contact.py — 友善預約表單（最小必填 + 成功導引）
import streamlit as st
from datetime import date

st.title("📅 預約 1 對 1 傳承規劃")

st.markdown(
    "我們採 **保密制** 與 **預約制**：留下基本聯絡方式與偏好時段，顧問將於一個工作日內與您確認。"
)

with st.form("booking"):
    name = st.text_input("您的稱呼*", placeholder="王先生 / 李小姐")
    phone = st.text_input("聯絡電話*", placeholder="09xx-xxx-xxx")
    email = st.text_input("Email（可選）", placeholder="you@example.com")
    prefer_day = st.date_input("偏好日期", value=date.today())
    prefer_slot = st.selectbox("偏好時段", ["上午", "下午", "不限"])
    notes = st.text_area("想先了解的重點（可選）", placeholder="如：跨境資產配置、保單傳承、企業接班...")

    submitted = st.form_submit_button("送出預約")

if submitted:
    # 這裡先顯示前端確認訊息；後續若要自動寄信，可再加 SMTP / webhook
    st.success("已收到您的預約！我們將在一個工作日內與您確認時段。")
    st.info("下一步：請留意手機來電與 Email 通知。")
    st.markdown("— 也可以同時來信：**123@gracefo.com**（主旨：預約傳承規劃）")
