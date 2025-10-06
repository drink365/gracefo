# app.py — 永傳《影響力》傳承平台（首頁：定位 × 體驗 × 信任 × 轉換）
import streamlit as st
from pathlib import Path
from app_config import ensure_page_config
from modules.cta_section import render_cta

# ✅ 全站統一 config（favicon、wide/centered、收起側邊）
ensure_page_config()

root = Path(__file__).parent
LOGO = str(root / "logo.png") if (root / "logo.png").exists() else None

# ------------------------
# 自訂頂部導覽（因 .streamlit 關閉了左側 pages）
# ------------------------
def top_nav():
    st.markdown(
        """
        <style>
        .nav {display:flex; gap:18px; align-items:center; padding:10px 6px; border-bottom:1px solid #eee;}
        .nav a {text-decoration:none;}
        .brand {font-weight:700; font-size:16px;}
        .nav .spacer {flex:1}
        .btn {padding:8px 12px; border-radius:10px; border:1px solid #e6e6e6;}
        .btn-primary {border-color:#145DA0;}
        </style>
        <div class="nav">
          <div class="brand">永傳家族傳承導師｜影響力傳承平台</div>
          <div class="spacer"></div>
          <a class="btn" href="/" target="_self">首頁</a>
          <a class="btn" href="/3_about" target="_self">關於我們</a>
          <a class="btn" href="/2_cases" target="_self">客戶故事</a>
          <a class="btn" href="/0_tools" target="_self">工具</a>
          <a class="btn btn-primary" href="/4_contact" target="_self">預約規劃</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

top_nav()

# ------------------------
# 首屏 HERO（定位 × 價值 × 雙 CTA）
# ------------------------
col_logo, col_hero = st.columns([1, 3], vertical_alignment="center")
with col_logo:
    if LOGO:
        st.image(LOGO, use_container_width=True)
with col_hero:
    st.markdown("## 讓關心的人，在需要時真的被照顧到。")
    st.markdown(
        "專為高資產家庭設計的傳承策略與保障結構，**整合法律、稅務、保險**，打造家族的**永續現金流**。"
    )
    st.markdown(
        """
        <div style="display:flex; gap:12px; margin:8px 0 4px 0;">
          <a class="btn-primary" href="/5_estate_tax" target="_self"
             style="padding:10px 14px; border:1px solid #145DA0; border-radius:10px; text-decoration:none;">
             5題測出傳承準備度
          </a>
          <a class="btn-secondary" href="/4_contact" target="_self"
             style="padding:10px 14px; border:1px solid #e6e6e6; border-radius:10px; text-decoration:none;">
             預約 1 對 1 規劃
          </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
st.divider()

# ------------------------
# 工具入口（單一路徑：體驗 → 結果 → CTA → 預約）
# ------------------------
st.markdown("### 🔧 工具入口")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown("**傳承準備度**")
    st.write("用 5 題快速了解您的傳承風險與優先順序。")
    st.link_button("開始測驗", "/5_estate_tax")
with c2:
    st.markdown("**保單策略模擬**")
    st.write("試算保障結構與受益人設計，評估傳承確定性。")
    st.link_button("開啟模擬", "/8_insurance_strategy")
with c3:
    st.markdown("**風險檢查**")
    st.write("檢查資產分布、繼承順序與稅負敏感度。")
    st.link_button("立即檢查", "/9_risk_check")

st.info("建議路徑：先測驗 → 看結果建議 → 送出預約，我們會針對您的情況提出專屬方案。")

st.divider()

# ------------------------
# 信任與價值（權威三角＋生活案例）
# ------------------------
st.markdown("### 🤝 我們是誰")
st.markdown(
    """
**永傳家族傳承導師**｜專注高資產家族的跨世代傳承設計  
用 **法律 × 稅務 × 保險** 的整合能力，將抽象風險化為可執行的保障結構。

- 🇺🇸 美國會計師（CPA），投資銀行與上市公司管理背景  
- 家族辦公室創辦人：以顧問思維與科技工具，設計可落地的傳承方案  
- 勞動部與業界授課經驗：企業接班、傳承策略、稅務與保單應用  
"""
)

st.markdown("### 💬 客戶故事（匿名）")
with st.expander("▶ 90 歲長輩的安心交棒"):
    st.write(
        "在二代準備再婚、三代尚未接班的情況下，我們以保單與受益人設計，達成資產指定與稅負預備，確保第三代教育基金與家族現金流。"
    )
with st.expander("▶ 跨境資產的稅務整理"):
    st.write(
        "針對台灣＋海外資產，先確立法律／稅務的合規路徑，再用保單壓縮與信託替代機制，創造可預期的現金流。"
    )

st.caption("註：案例均經匿名化處理，保護客戶隱私。")

st.divider()

# ------------------------
# 品牌使命（溫暖而堅定）
# ------------------------
st.markdown("### 🌱 品牌使命")
st.write(
    "我們相信，每個家庭的成功都值得被延續。《影響力》致力於推動財富傳承教育，以專業顧問與科技工具，協助家族以更低成本、更高效率，完成愛與責任的交棒。"
)

# ------------------------
# 全站 CTA（頁尾固定出現）
# ------------------------
render_cta()
