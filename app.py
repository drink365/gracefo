
import os
import uuid
import csv
from datetime import datetime
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="《影響力》傳承策略平台｜永傳家族辦公室",
    page_icon="💛",
    layout="wide"
)

PRIMARY = "#145DA0"
ACCENT  = "#F9A826"
BG      = "#F7FAFC"
TEXT    = "#1A202C"

DATA_DIR = Path("./data")
DATA_DIR.mkdir(exist_ok=True)
LEADS_CSV = DATA_DIR / "leads.csv"

if Path("assets/logo.png").exists():
    st.logo("assets/logo.png")

st.markdown(
    f"""
    <style>
      .stApp {{
        background: {BG};
        color: {TEXT};
        font-family: "Noto Sans TC", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang TC", "Microsoft JhengHei", sans-serif;
      }}
      #MainMenu {{visibility: hidden;}}
      footer {{visibility: hidden;}}
      .hero {{
        padding: 56px 24px;
        border-radius: 24px;
        background: white;
        border: 1px solid #EDF2F7;
        box-shadow: 0 6px 24px rgba(0,0,0,0.06);
      }}
      .hero h1 {{
        font-size: 36px;
        line-height: 1.25;
        margin: 0 0 8px 0;
        color: {PRIMARY};
      }}
      .hero p.sub {{
        font-size: 18px;
        color: #4A5568;
        margin: 8px 0 0 0;
      }}
      .kpi-wrap {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
        margin-top: 16px;
      }}
      .kpi {{
        background: #FAFAFA;
        border: 1px solid #EDF2F7;
        border-radius: 14px;
        padding: 14px 16px;
        text-align: center;
        font-size: 14px;
        color: #4A5568;
      }}
      .section {{
        margin-top: 24px;
        padding: 24px;
        background: white;
        border: 1px solid #EDF2F7;
        border-radius: 20px;
        box-shadow: 0 3px 14px rgba(0,0,0,0.04);
      }}
      .sec-title {{
        font-size: 22px;
        font-weight: 700;
        color: {PRIMARY};
        margin: 0 0 12px 0;
      }}
      .how-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
      }}
      .card {{
        border: 1px solid #EDF2F7;
        border-radius: 16px;
        padding: 16px;
        background: #FCFCFD;
      }}
      .trust-grid, .case-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
      }}
      .cta-final {{
        text-align: center;
        padding: 32px 16px;
        border: 2px dashed {ACCENT};
        border-radius: 20px;
        background: #FFFBF2;
      }}
      .footer {{
        margin-top: 24px;
        color: #4A5568;
        font-size: 13px;
        text-align: center;
      }}
      .btn-row {{
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
        align-items: center;
        margin-top: 16px;
      }}
      .small-note {{ font-size: 12px; color: #6B7280; }}
    </style>
    """,
    unsafe_allow_html=True
)

GA_ID = os.getenv("GA_MEASUREMENT_ID", "")
META_PIXEL_ID = os.getenv("META_PIXEL_ID", "")

ga_script = f"""
<script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', '{GA_ID}');
</script>
""" if GA_ID else ""

meta_pixel = f"""
<script>
!function(f,b,e,v,n,t,s)
{{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '{META_PIXEL_ID}');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id={META_PIXEL_ID}&ev=PageView&noscript=1"
/></noscript>
""" if META_PIXEL_ID else ""

if ga_script or meta_pixel:
    components.html(ga_script + meta_pixel, height=0, width=0)

def append_lead(email: str, name: str = "", note: str = "", source: str = "whitepaper"):
    is_new = not LEADS_CSV.exists()
    with open(LEADS_CSV, mode="a", newline="", encoding="utf-8") as f:
        import csv
        writer = csv.writer(f)
        if is_new:
            writer.writerow(["id", "created_at", "name", "email", "note", "source"])
        writer.writerow([str(uuid.uuid4()), datetime.now().isoformat(), name.strip(), email.strip(), note.strip(), source])

col_hero, col_blank = st.columns([7, 5])
with col_hero:
    st.markdown(
        f"""
        <div class="hero">
          <h1>專為高資產家庭設計的 <br/>傳承策略工具</h1>
          <p class="sub">
            「準備與從容，讓家族影響力，被好好交棒。」<br/>
            以法律 × 稅務 × 保單的整合視角，為您打造確定性的傳承方案。
          </p>
          <div class="btn-row">
        """, unsafe_allow_html=True
    )
    st.page_link("pages/01_傳承風險檢測.py", label="🧭 立即開始 5 分鐘傳承檢測", icon="🧭")

    with st.popover("📗 下載《高資產傳承 7 大盲點》", use_container_width=False):
        with st.form("whitepaper_form", clear_on_submit=True):
            name = st.text_input("稱呼（可不填）", key="lead_name")
            email = st.text_input("Email（用於接收白皮書）*", key="lead_email")
            agree = st.checkbox("我了解此資料僅用於寄送白皮書與後續學習內容。")
            submitted = st.form_submit_button("送出並取得下載連結")
            if submitted:
                if not email or "@" not in email:
                    st.error("請輸入有效的 Email。")
                elif not agree:
                    st.error("請先勾選同意。")
                else:
                    append_lead(email=email, name=name, source="whitepaper")
                    st.success("已收到！白皮書下載連結已建立。")
                    st.markdown("👉 請留意您的信箱；若未收到，請檢查垃圾郵件匣或與我們聯絡。")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown(
        """
        <div class="kpi-wrap">
          <div class="kpi">跨國資產視角：<br/>台灣 × 美國 × 加拿大</div>
          <div class="kpi">法稅結合保單設計：<br/>兼顧流動性與節稅</div>
          <div class="kpi">顧問式陪伴：<br/>從風險辨識到行動落地</div>
        </div>
        """, unsafe_allow_html=True
    )

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="sec-title">如何運作</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="how-grid">
      <div class="card"><b>① 回答 6 題檢測</b><br/>以家庭結構、資產類別、跨境因素做初步盤點。</div>
      <div class="card"><b>② 取得初步建議</b><br/>自動生成您的「傳承地圖」與風險提示。</div>
      <div class="card"><b>③ 預約專業顧問</b><br/>用法律 × 稅務 × 保單完成可執行的行動方案。</div>
    </div>
    """, unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="sec-title">您將獲得</div>', unsafe_allow_html=True)
st.markdown(
    """
    - ✅ 專屬 <b>傳承地圖</b>（將資產、權責與受益設計可視化）
    - ✅ <b>初步風險分析報告</b>：稅負、流動性、接班秩序
    - ✅ <b>顧問一對一解說</b>：把建議轉成行動，避免留白與爭議
    <div class="small-note">＊所有結果僅為教育性初評，非稅法／投資建議，需經顧問複核。</div>
    """, unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="sec-title">信任與專業</div>', unsafe_allow_html=True)
c1, c2 = st.columns([5,7])
with c1:
    st.markdown(
        """
        **Grace Huang｜永傳家族傳承導師**  
        美國會計師（CPA）｜永傳家族辦公室創辦人  
        曾任投資銀行主管、上市公司高管、科技創業者  
        長年授課於勞動部與各協會，專注高資產家族傳承  

        > 「讓關心的人，在需要時真的被照顧到。」
        """)
with c2:
    st.markdown(
        """
        <div class="trust-grid">
          <div class="card"><b>跨領域整合</b><br/>法律 × 稅務 × 保單 × 股權規劃</div>
          <div class="card"><b>專家夥伴</b><br/>國際律師、會計師、信託與銀行合作</div>
          <div class="card"><b>公開分享</b><br/>媒體/協會講座與專欄（Logo 牆可置放於此）</div>
        </div>
        """, unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown('<div class="sec-title">真實情境（匿名示例）</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="case-grid">
      <div class="card">
        <b>90 歲長輩 × 二代再婚 × 三代分配</b><br/>
        作法：保單加速＋指定受益；婚前財產隔離設計。<br/>
        成效：減輕未來稅負、避免落入外籍配偶、同時照顧第三代。
      </div>
      <div class="card">
        <b>股權在台、子女在海外</b><br/>
        作法：治理與權責設計＋信託／保單組合。<br/>
        成效：接班秩序清楚、流動性與稅務預備到位。
      </div>
      <div class="card">
        <b>不動產占比高、缺現金流</b><br/>
        作法：調整資產載體、建立永續現金流模型。<br/>
        成效：穩定照顧一代、二代、三代的現金需求。
      </div>
    </div>
    """, unsafe_allow_html=True
)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section cta-final">', unsafe_allow_html=True)
st.markdown("### 現在開始，為家族打造確定性的傳承方案")
st.page_link("pages/01_傳承風險檢測.py", label="🧭 立即開始 5 分鐘傳承檢測", icon="🧭")
st.markdown('<div class="small-note">或先下載白皮書了解方向，再與我們對話。</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="footer">
    《影響力》傳承策略平台｜永傳家族辦公室<br/>
    https://gracefo.com｜聯絡信箱：hello@gracefo.com
    </div>
    """, unsafe_allow_html=True
)
