# app.py — 永傳《影響力》傳承平台（精簡首頁：清楚定位 × 正確導覽 × 友善轉換）
import streamlit as st
from pathlib import Path
from app_config import ensure_page_config
from modules.cta_section import render_cta

# 全站設定
ensure_page_config()
root = Path(__file__).parent
LOGO = str(root / "logo.png") if (root / "logo.png").exists() else None

# ---------- 外觀微調（降低雜訊、提高留白） ----------
st.markdown("""
<style>
/* 整體寬度與留白 */
.block-container {max-width: 1080px; padding-top: 0.8rem;}

/* 標題層級更克制 */
h1, .stMarkdown h1 {font-size: 1.8rem; margin-bottom: .6rem;}
h2, .stMarkdown h2 {font-size: 1.3rem; margin-top: 1.2rem;}
p {line-height: 1.7;}

/* 卡片風格 */
.card{border:1px solid #e9eef3; border-radius:12px; padding:16px; background:#fff;}
.card h4{margin:0 0 6px 0; font-size:1.05rem;}
.card p{margin:0 0 10px 0; color:#4a5568;}

/* 導覽列（改用內建 page_link，不再用 href） */
.nav {display:flex; gap:10px; align-items:center; padding:10px 0 14px 0; border-bottom:1px solid #eee;}
.brand {font-weight:700; font-size: 15px;}
.spacer{flex:1}

/* 首屏 CTA 行距 */
.hero-cta{display:flex; gap:10px; flex-wrap:wrap; margin-top:.5rem;}
.logo-wrap img{max-width: 160px; border-radius: 6px;}
</style>
""", unsafe_allow_html=True)

# ---------- 頂部導覽（使用 Streamlit 內建路由） ----------
def top_nav():
    st.markdown('<div class="nav">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([2,6,4])
    with col1:
        if LOGO: st.markdown('<div class="logo-wrap">', unsafe_allow_html=True); st.image(LOGO); st.markdown('</div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="brand">永傳家族傳承導師｜影響力傳承平台</div>', unsafe_allow_html=True)
    with col3:
        if hasattr(st, "page_link"):
            st.page_link("app.py", label="首頁")
            st.page_link("pages/3_about.py", label="關於我們")
            st.page_link("pages/2_cases.py", label="客戶故事")
            st.page_link("pages/0_tools.py", label="工具")
            st.page_link("pages/4_contact.py", label="預約規劃")
        else:
            # 若你的 Streamlit 版本較舊，暫時顯示文字提示
            st.info("導覽需要 Streamlit 1.32+（支援 st.page_link）。")
    st.markdown('</div>', unsafe_allow_html=True)

top_nav()

# ---------- 首屏 HERO（更克制的資訊量） ----------
st.markdown("### 讓關心的人，在需要時真的被照顧到。")
st.write("專為高資產家庭設計的傳承策略與保障結構，整合法律、稅務、保險，打造家族的永續現金流。")

# 使用原生按鈕／page_link，避免 404
cta_cols = st.columns([1,1,4])
with cta_cols[0]:
    if hasattr(st, "page_link"):
        st.page_link("pages/5_estate_tax.py", label="5題測出傳承準備度")
    else:
        st.link_button("5題測出傳承準備度", "#")  # 版本舊時先保留按鈕外觀
with cta_cols[1]:
    if hasattr(st, "page_link"):
        st.page_link("pages/4_contact.py", label="預約 1 對 1 規劃")
    else:
        st.link_button("預約 1 對 1 規劃", "#")

st.divider()

# ---------- 工具入口（2 欄、更清爽） ----------
st.markdown("#### 🔧 工具入口")
colA, colB = st.columns(2)

with colA:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("**傳承準備度**")
    st.write("用 5 題了解傳承風險與優先順序。")
    if hasattr(st, "page_link"):
        st.page_link("pages/5_estate_tax.py", label="開始測驗")
    else:
        st.link_button("開始測驗", "#")
    st.markdown('</div>', unsafe_allow_html=True)

with colB:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("**保單策略模擬**")
    st.write("試算保障結構與受益人設計，評估傳承確定性。")
    if hasattr(st, "page_link"):
        st.page_link("pages/8_insurance_strategy.py", label="開啟模擬")
    else:
        st.link_button("開啟模擬", "#")
    st.markdown('</div>', unsafe_allow_html=True)

# 第二列工具（可視需求保留或移到 Tools 頁）
colC, colD = st.columns(2)
with colC:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("**風險檢查**")
    st.write("檢查資產分布、繼承順序與稅負敏感度。")
    if hasattr(st, "page_link"):
        st.page_link("pages/9_risk_check.py", label="立即檢查")
    else:
        st.link_button("立即檢查", "#")
    st.markdown('</div>', unsafe_allow_html=True)

with colD:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("**工具總覽**")
    st.write("一次看見所有工具與說明。")
    if hasattr(st, "page_link"):
        st.page_link("pages/0_tools.py", label="前往工具")
    else:
        st.link_button("前往工具", "#")
    st.markdown('</div>', unsafe_allow_html=True)

st.info("建議路徑：先測驗 → 看結果建議 → 送出預約，我們會針對您的情況提出專屬方案。")

st.divider()

# ---------- 信任與價值（更簡潔） ----------
st.markdown("#### 🤝 我們是誰")
st.write(
    "永傳家族傳承導師｜專注高資產家族的跨世代傳承設計。以 **法律 × 稅務 × 保險** 的整合能力，將抽象風險化為可執行的保障結構。"
)
st.write("- 🇺🇸 美國會計師（CPA），投資銀行與上市公司管理背景")
st.write("- 家族辦公室創辦人：以顧問思維與科技工具，設計可落地的傳承方案")
st.write("- 勞動部與業界授課經驗：企業接班、傳承策略、稅務與保單應用")

st.markdown("#### 💬 客戶故事（匿名）")
with st.expander("▶ 90 歲長輩的安心交棒"):
    st.write("在二代準備再婚、三代尚未接班的情況下，以保單與受益人設計，達成資產指定與稅負預備，確保第三代教育基金與家族現金流。")
with st.expander("▶ 跨境資產的稅務整理"):
    st.write("針對台灣＋海外資產，先確立法律／稅務合規，再用保單壓縮與信託替代機制，創造可預期現金流。")
st.caption("註：案例均經匿名化處理，保護客戶隱私。")

st.divider()

# ---------- 品牌使命 ----------
st.markdown("#### 🌱 品牌使命")
st.write("我們相信，每個家庭的成功都值得被延續。以專業顧問與科技工具，協助家族更低成本、更高效率地完成愛與責任的交棒。")

# ---------- 全站 CTA ----------
render_cta()
