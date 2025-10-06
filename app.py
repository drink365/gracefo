# app.py — 永傳《影響力》傳承平台（情感引導 × 精簡文案 × 順暢轉換）
import streamlit as st
from pathlib import Path
from app_config import ensure_page_config
from modules.cta_section import render_cta

# 全站設定
ensure_page_config()
root = Path(__file__).parent
LOGO = str(root / "logo.png") if (root / "logo.png").exists() else None

# ---------- 外觀微調（極簡、留白、聚焦） ----------
st.markdown("""
<style>
.block-container {max-width: 1080px; padding-top: .6rem;}
h1 {font-size: 1.8rem; margin: .4rem 0 .2rem 0;}
h2 {font-size: 1.25rem; margin: 1.1rem 0 .5rem 0;}
p, li {line-height: 1.7;}
.muted {color:#6b7280}
.badges {display:flex; gap:10px; flex-wrap:wrap; margin:.3rem 0 0 0;}
.badge {border:1px solid #e6edf3; padding:6px 10px; border-radius:999px; font-size:.9rem; background:#fff;}
.hero-cta{display:flex; gap:10px; flex-wrap:wrap; margin-top:.6rem;}
.logo-wrap img{max-width: 150px; border-radius: 6px;}
.card{border:1px solid #e9eef3; border-radius:12px; padding:16px; background:#fff;}
.quote{border-left:4px solid #e9eef3; padding:.6rem 1rem; background:#fafcfe; border-radius:8px;}
.step{display:flex; gap:10px; align-items:flex-start; margin:.4rem 0;}
.step-num{background:#145DA0; color:#fff; border-radius:999px; width:26px; height:26px; display:flex; align-items:center; justify-content:center; font-size:.9rem; margin-top:.15rem;}
.kv{display:flex; gap:12px; flex-wrap:wrap;}
.kv .k{font-size:1.1rem; font-weight:700}
.kv .v{color:#374151}
.band{background:#0f172a; color:#e5e7eb; border-radius:12px; padding:14px; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap;}
.band a{color:#fff; text-decoration:none; border:1px solid #334155; padding:8px 12px; border-radius:10px; margin-top:6px;}
.nav {display:flex; gap:10px; align-items:center; padding:10px 0 12px 0; border-bottom:1px solid #eee;}
.spacer{flex:1}
</style>
""", unsafe_allow_html=True)

# ---------- 頂部導覽（使用 Streamlit 內建路由） ----------
def top_nav():
    st.markdown('<div class="nav">', unsafe_allow_html=True)
    c1, c2 = st.columns([1,5])
    with c1:
        if LOGO: st.markdown('<div class="logo-wrap">', unsafe_allow_html=True); st.image(LOGO); st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        cols = st.columns([6,7])
        with cols[0]:
            st.markdown("**永傳家族傳承導師｜影響力傳承平台**")
        with cols[1]:
            if hasattr(st, "page_link"):
                st.page_link("app.py", label="首頁")
                st.page_link("pages/3_about.py", label="關於我們")
                st.page_link("pages/2_cases.py", label="客戶故事")
                st.page_link("pages/0_tools.py", label="工具")
                st.page_link("pages/4_contact.py", label="預約規劃")
            else:
                st.info("導覽需要 Streamlit 1.32+（支援 st.page_link）。")
    st.markdown('</div>', unsafe_allow_html=True)

top_nav()

# ---------- 首屏（一句話 × 兩個行動） ----------
st.markdown("## 讓關心的人，在需要時真的被照顧到。")
st.markdown(
    "以 **法律 × 稅務 × 保險** 的整合設計，為高資產家庭打造**可預期、可執行**的傳承現金流。"
)
# 以徽章呈現關鍵字，降低文字密度、增強記憶點
st.markdown('<div class="badges">', unsafe_allow_html=True)
st.markdown('<span class="badge">家族現金流</span>', unsafe_allow_html=True)
st.markdown('<span class="badge">指定受益</span>', unsafe_allow_html=True)
st.markdown('<span class="badge">稅負預備</span>', unsafe_allow_html=True)
st.markdown('<span class="badge">跨境合規</span>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

cta_cols = st.columns([1,1,4])
with cta_cols[0]:
    if hasattr(st, "page_link"):
        st.page_link("pages/5_estate_tax.py", label="5題測出準備度")
    else:
        st.link_button("5題測出準備度", "#")
with cta_cols[1]:
    if hasattr(st, "page_link"):
        st.page_link("pages/4_contact.py", label="預約 1 對 1")
    else:
        st.link_button("預約 1 對 1", "#")

# 社會證明（更像一行 KPI，而非長段文字）
st.markdown(
    '<div class="kv"><div><span class="k">300+ 場</span> <span class="v">企業／機構授課與分享</span></div>'
    '<div><span class="k">20+ 年</span> <span class="v">財稅與傳承顧問經驗</span></div>'
    '<div><span class="k">跨境</span> <span class="v">台／美／加／亞洲多地資產規劃</span></div></div>',
    unsafe_allow_html=True
)

st.divider()

# ---------- 工具入口（兩張卡，短句 + 單一按鈕） ----------
st.markdown("### 🔧 先體驗，再預約")
colA, colB = st.columns(2)

with colA:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### 傳承準備度")
    st.write("5 題找出你的風險盲點與優先順序。")
    if hasattr(st, "page_link"): st.page_link("pages/5_estate_tax.py", label="開始測驗")
    else: st.link_button("開始測驗", "#")
    st.markdown('</div>', unsafe_allow_html=True)

with colB:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("#### 保單策略模擬")
    st.write("試算保障結構與受益人設計，衡量傳承的確定性。")
    if hasattr(st, "page_link"): st.page_link("pages/8_insurance_strategy.py", label="開啟模擬")
    else: st.link_button("開啟模擬", "#")
    st.markdown('</div>', unsafe_allow_html=True)

st.caption("建議路徑：先測驗／模擬 → 看到重點 → 預約 1 對 1。")

st.divider()

# ---------- 客戶感受（一句話引用，拉情緒） ----------
st.markdown("### 💬 他們怎麼說")
st.markdown(
    """<div class="quote">
    「把最重要的事情先做好，家人心就安了。方案清楚、流程透明，我們知道每一步為什麼。」  
    <span class="muted">— 匿名企業家家庭</span>
    </div>""",
    unsafe_allow_html=True,
)

# ---------- 三步流程（降低決策負擔） ----------
st.markdown("### 🛠️ 我們怎麼一起做（3 步）")
for i, (t, d) in enumerate([
    ("了解情況", "15 分鐘初談：家族結構、資產分布、核心顧慮。"),
    ("設計方案", "以法律/稅務/保單整合，給你 1–2 套可執行選項。"),
    ("安心交棒", "確定受益、設定金流，建立傳承與風險的防護網。"),
], start=1):
    st.markdown(f'<div class="step"><div class="step-num">{i}</div><div><b>{t}</b><br><span class="muted">{d}</span></div></div>', unsafe_allow_html=True)

st.divider()

# ---------- 為什麼是現在（行動理由） ----------
st.markdown(
    '<div class="band">'
    '<div>稅制與家族情況會變，<b>越早規劃，越能用更低的成本換更高的確定性</b>。</div>'
    + ('<div>' + (st.page_link.__name__ if hasattr(st, "page_link") else '') + '</div>'),
    unsafe_allow_html=True
)
# 在 band 內再放一次 CTA（避免捲到底前流失）
b1, b2 = st.columns([1,1])
with b1:
    if hasattr(st, "page_link"): st.page_link("pages/5_estate_tax.py", label="5題測出準備度")
with b2:
    if hasattr(st, "page_link"): st.page_link("pages/4_contact.py", label="預約 1 對 1 規劃")

st.divider()

# ---------- 關於我們（極短版，更多細節在 About 頁） ----------
st.markdown("### 🤝 關於我們（短版）")
st.write("美國會計師（CPA）背景，投資銀行與上市公司管理經驗。以顧問思維與科技工具，專注高資產家族的跨世代傳承設計。")
if hasattr(st, "page_link"): st.page_link("pages/3_about.py", label="看完整介紹 →")

# ---------- 全站 CTA ----------
render_cta()
