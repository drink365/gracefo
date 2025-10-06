
import streamlit as st
from app_config import ensure_page_config
ensure_page_config()
# --- Force-hide Streamlit sidebar & its toggle (applies to this page) ---
hide_sidebar_style = """
    <style>
        [data-testid="stSidebar"] {display: none;}
        [data-testid="stSidebarNav"] {display: none;}
        [data-testid="collapsedControl"] {display: none;}
    </style>
"""
st.markdown(hide_sidebar_style, unsafe_allow_html=True)
# --- 頁首區 ---
st.markdown("""
<div style='text-align: center;'>
    <h2>🙋 我的專屬傳承規劃工具</h2>
    <p style='font-size: 18px;'>從探索到設計，每一步都有我們陪你一起思考</p>
</div>
""", unsafe_allow_html=True)



# --- 快速導流：3分鐘評估 ---
st.markdown("### ✅ 從這裡開始：3 分鐘看見你的重點")
st.write("回答幾個簡單問題，我們會先生成「傳承重點摘要」，再引導你使用對的工具。")
if st.button("➡️ 開始 3 分鐘評估", key="go_quick_assessment"):
    # 先導到既有的評估頁（可改成 pages/1_coach.py）
    st.switch_page("pages/9_risk_check.py")

st.markdown("---")

# --- 工具導覽 ---
st.markdown("### 🔍 我的傳承探索工具")

st.markdown("#### 🌿 1. 傳承風格探索")
st.write("透過風格測驗，了解您偏好的溝通方式與規劃重點。")
if st.button("🌿 開始探索我的風格", key="go_coach_client"):
    st.switch_page("pages/1_coach.py")

st.markdown("#### 🛡️ 2. 傳承風險盤點")
st.write("快速檢視六大潛在風險，讓您知道從哪裡開始規劃最重要。")
if st.button("🛡️ 檢視我的風險清單", key="go_risk_check_client"):
    st.switch_page("pages/9_risk_check.py")

st.markdown("#### 🗺️ 3. 資產結構與現金流模擬")
st.write("輸入您的資產分布，系統自動整理結構與風險建議。")
if st.button("🗺️ 建立我的資產圖", key="go_asset_map_client"):
    st.switch_page("pages/7_asset_map.py")

st.markdown("#### 📦 4. 保單策略設計")
st.write("根據年齡與需求，幫您模擬合適的保障組合與財稅結構。")
if st.button("📦 啟動我的保單模擬", key="go_insurance_client"):
    st.switch_page("pages/8_insurance_strategy.py")

st.markdown("#### 🧮 5. 稅務與退休試算")
st.write("了解未來的現金缺口與長期退休預備是否充足。")
col1, col2 = st.columns(2)
with col1:
    if st.button("🧮 AI秒算遺產稅", key="go_tax_client"):
        st.switch_page("pages/5_estate_tax.py")
with col2:
    if st.button("💰 樂活退休試算", key="go_retire_client"):
        st.switch_page("pages/6_retirement.py")

# 6. 不動產稅負試算
st.markdown("#### 🏠 6. 不動產稅負試算")
st.write("協助您試算未來不動產買賣或贈與/繼承的稅負情境。")
if st.button("🏠 AI秒算房產傳承稅負", key="go_real_estate_tax_client"):
        st.switch_page("pages/10_property.py")


# --- 寄送我的初步報告（留資） ---
st.markdown("---")
st.markdown("### 📧 寄送我的初步報告")
with st.form("lead_capture_form"):
    name  = st.text_input("姓名*", max_chars=40)
    email = st.text_input("Email*", max_chars=80)
    agree = st.checkbox("我了解此評估僅供初步參考，實際方案需由專業人士確認。", value=True)
    submitted = st.form_submit_button("寄送給我")
    if submitted:
        if not name or not email or not agree:
            st.warning("請完整填寫並勾選同意。")
        else:
            st.success("已接收，初步報告將以Email寄送給您。")
            st.info("想更快完成？您也可以直接預約 30 分鐘諮詢。")
            # 可改為 st.switch_page("pages/booking.py")

# --- 聯絡資訊 ---
st.markdown("---")
st.markdown(
    """
    <div style='display: flex; justify-content: center; align-items: center; gap: 1.5em; font-size: 14px; color: gray;'>
      <a href='?' style='color:#006666; text-decoration: underline;'>《影響力》傳承策略平台</a>
      <a href='https://gracefo.com' target='_blank'>永傳家族辦公室</a>
      <a href='mailto:123@gracefo.com'>123@gracefo.com</a>
    </div>
    """,
    unsafe_allow_html=True
)
