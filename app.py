
import streamlit as st
from app_config import ensure_page_config

ensure_page_config()

# -------------------- HERO --------------------
st.markdown(
    """
    <div class="section hero section-centered">
      <h1>讓傳承，成為愛的延續</h1>
      <p>在 10 分鐘內，看見你的傳承方向與下一步：讓複雜的安排，變成可理解、可行動。</p>
      <p style="margin-top: 10px;">
        <a href="#get-started" class="cta">開始我的傳承評估</a>
      </p>
    </div>
    """, unsafe_allow_html=True
)

# -------------------- WHAT WE HELP --------------------
st.markdown("""
<div class="section">
  <h2>這個平台能幫你什麼？</h2>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(
        """<div class="card">
        <h3>🎯 立即診斷</h3>
        <p class="muted">3 分鐘評估你的傳承重點，先看懂自己，再選擇工具。</p>
        </div>""", unsafe_allow_html=True)
with c2:
    st.markdown(
        """<div class="card">
        <h3>🧩 規劃藍圖</h3>
        <p class="muted">把散落的資產轉成一張清楚的圖，理解風險與順序。</p>
        </div>""", unsafe_allow_html=True)
with c3:
    st.markdown(
        """<div class="card">
        <h3>🤝 專人協作</h3>
        <p class="muted">需要更深入？可安排專人與您協作，完成商品配置、法稅與文件安排。</p>
        </div>""", unsafe_allow_html=True)

# -------------------- START JOURNEY (CLIENT ONLY) --------------------
st.markdown('<div id="get-started"></div>', unsafe_allow_html=True)
st.markdown("""
<div class="section section-centered">
  <h2>開始你的專屬旅程</h2>
  <p class="muted">單一路徑：3 分鐘評估 → 初步報告 → 預約諮詢</p>
</div>
""", unsafe_allow_html=True)

# Button to go to client_home
go = st.button("開始我的傳承評估 ➜", type="primary")
if go:
    try:
        st.switch_page("pages/client_home.py")
    except Exception:
        # Fallback: show hint if switch_page not available in the runtime
        st.info("請從左側選單進入「客戶首頁 / Client Home」。")

st.markdown("""<div class="section section-centered muted">
  僅以最小必要原則使用資料，並提供刪除與匿名化機制。
</div>""", unsafe_allow_html=True)
