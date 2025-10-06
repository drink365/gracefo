
import streamlit as st
from app_config import ensure_page_config

ensure_page_config()

st.markdown("<h2>客戶首頁</h2>", unsafe_allow_html=True)
st.write("歡迎回到《影響力》傳承策略平台：先從 3 分鐘評估開始，快速看見你的重點。")

# -------------------- QUICK ASSESSMENT CARD --------------------
st.markdown("### ✅ 從這裡開始：3 分鐘看見你的重點")
st.write("回答幾個簡單問題，我們會生成「傳承重點摘要」，再引導你使用對的工具。")
if st.button("➡️ 開始 3 分鐘評估", key="go_quick_assessment"):
    try:
        st.switch_page("pages/9_risk_check.py")  # or "pages/1_coach.py"
    except Exception:
        st.warning("請從左側選單進入 評估頁（風險盤點 或 風格探索）。")

# -------------------- TOOL GRID --------------------
st.markdown("---")
st.markdown("#### 工具導覽（先做評估，再依建議使用）")
t1, t2, t3 = st.columns(3)
with t1:
    st.markdown("""<div class="card">
    <h4>🧭 風格探索</h4>
    <p class="muted">理解你的價值觀與重視順位，讓安排更貼近家人的期待。</p>
    </div>""", unsafe_allow_html=True)
    if st.button("前往風格探索", key="go_style"):
        try: st.switch_page("pages/1_coach.py")
        except Exception: st.info("請從左側選單進入「風格探索」。")

with t2:
    st.markdown("""<div class="card">
    <h4>🛡️ 風險盤點</h4>
    <p class="muted">先看懂風險落點與優先順序，避免在關鍵處失分。</p>
    </div>""", unsafe_allow_html=True)
    if st.button("前往風險盤點", key="go_risk"):
        try: st.switch_page("pages/9_risk_check.py")
        except Exception: st.info("請從左側選單進入「風險盤點」。")

with t3:
    st.markdown("""<div class="card">
    <h4>🗺️ 家族資產圖</h4>
    <p class="muted">把散落的資產轉成清楚的圖，理解稅務與交棒順序。</p>
    </div>""", unsafe_allow_html=True)
    if st.button("前往資產圖", key="go_asset"):
        try: st.switch_page("pages/7_asset_map.py")
        except Exception: st.info("請從左側選單進入「資產圖」。")

u1, u2, u3 = st.columns(3)
with u1:
    st.markdown("""<div class="card">
    <h4>📦 保單策略</h4>
    <p class="muted">用 20% 的保險，守護 100% 的資產—建立穩定與確定性。</p>
    </div>""", unsafe_allow_html=True)
    if st.button("前往保單策略", key="go_insurance"):
        try: st.switch_page("pages/8_insurance_strategy.py")
        except Exception: st.info("請從左側選單進入「保單策略」。")

with u2:
    st.markdown("""<div class="card">
    <h4>🏛️ 遺產稅估算</h4>
    <p class="muted">先估再決定，讓安排有根據，少走冤枉路。</p>
    </div>""", unsafe_allow_html=True)
    if st.button("前往遺產稅", key="go_estate"):
        try: st.switch_page("pages/5_estate_tax.py")
        except Exception: st.info("請從左側選單進入「遺產稅」。")

with u3:
    st.markdown("""<div class="card">
    <h4>🌱 退休與現金流</h4>
    <p class="muted">把未來的花費、收入與現金流，轉成可視化的路線圖。</p>
    </div>""", unsafe_allow_html=True)
    if st.button("前往退休規劃", key="go_retire"):
        try: st.switch_page("pages/6_retirement.py")
        except Exception: st.info("請從左側選單進入「退休規劃」。")

# -------------------- LEAD CAPTURE --------------------
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
            # MVP: 先顯示成功訊息。未來可寫入CSV/Google Sheet並寄出Email。
            st.success("已接收，初步報告將以 Email 寄送給您。")
            st.info("想更快完成？您也可以直接預約 30 分鐘諮詢。")

# -------------------- FOOTER NOTE --------------------
st.markdown('<div class="muted">《影響力》傳承策略平台｜永傳家族辦公室｜僅以最小必要原則使用資料</div>',
            unsafe_allow_html=True)
