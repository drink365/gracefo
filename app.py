
import streamlit as st
from datetime import datetime, date
import csv, os

st.set_page_config(
    page_title="永傳家族傳承導師｜《影響力》傳承策略平台",
    page_icon="assets/favicon.png",
    layout="wide"
)

# ---------- Global CSS (raw string, no formatting) ----------
st.markdown("""
<style>
@font-face {
  font-family: 'NotoSansTC';
  src: url('assets/NotoSansTC-Regular.ttf') format('truetype');
  font-weight: 400;
  font-style: normal;
}
html, body, [class*="css"] {
  font-family: 'NotoSansTC', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans TC", "PingFang TC", "Heiti TC", sans-serif;
}

/* Wide layout */
.block-container {max-width: 1200px !important;}

/* Hide default Streamlit menu & footer to make room for brand */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.hero {
  background: linear-gradient(120deg, #0E1E42 0%, #173B6D 100%);
  border-radius: 20px;
  padding: 48px 40px;
  color: white;
  margin-bottom: 24px;
}
.hero h1 {
  font-size: 40px;
  margin-bottom: 12px;
}
.hero p {
  font-size: 18px;
  opacity: 0.95;
}

.card {
  padding: 18px 16px;
  border-radius: 16px;
  border: 1px solid rgba(20, 20, 20, 0.08);
  background: #fff;
  box-shadow: 0 6px 18px rgba(10, 28, 58, 0.06);
}

.small {
  font-size: 13px;
  color: #6b7280;
}

.section-title{
  font-weight: 700;
  font-size: 24px;
  margin: 8px 0 0 0;
}

.cta {
  display: inline-block;
  padding: 12px 18px;
  border-radius: 999px;
  background: #F4B400;
  color: #111 !important;
  font-weight: 700;
  text-decoration: none !important;
  margin-right: 8px;
}

.ghost {
  display: inline-block;
  padding: 12px 18px;
  border-radius: 999px;
  border: 2px solid #F4B400;
  color: #F4B400 !important;
  font-weight: 700;
  text-decoration: none !important;
}
hr{border: none; border-top: 1px solid #eee; margin: 20px 0;}
</style>
""", unsafe_allow_html=True)

# --- Brand header ---
col_logo, col_head = st.columns([1,3], vertical_alignment="center")
with col_logo:
    st.image("assets/logo.png", use_container_width=True)
with col_head:
    st.markdown("### 永傳家族傳承導師｜《影響力》傳承策略平台")
    st.caption("專業 × 溫暖 × 信任｜讓家族的愛與資產，都能安全傳承三代。")

# --- Hero Section ---
with st.container():
    st.markdown('''
    <div class="hero">
        <h1>準備與從容，為家族打造「財務確定性」</h1>
        <p>結合財稅專業與保險策略，打造跨世代的傳承方案——把愛與資產，放心交棒。</p>
        <div style="margin-top:10px;">
            <a class="cta" href="#lead">預約 30 分鐘傳承健檢</a>
            <a class="ghost" href="#tools">試用 AI 工具箱</a>
        </div>
    </div>
    ''', unsafe_allow_html=True)

# --- Who & Problems ---
st.markdown("#### 你在找的，可能是這些答案：")
c1, c2, c3 = st.columns(3)
with c1:
    st.markdown('''<div class="card">
    <b>創辦人一代</b><br/>如何在合法節稅下，把股權與現金流安全交棒？
    </div>''', unsafe_allow_html=True)
with c2:
    st.markdown('''<div class="card">
    <b>企業接班</b><br/>贈與、信託、保單如何搭配？怎麼設計最穩妥又有效率？
    </div>''', unsafe_allow_html=True)
with c3:
    st.markdown('''<div class="card">
    <b>跨境家族</b><br/>台灣 / 中國大陸 / 美國多地資產與稅務，應如何兼顧？
    </div>''', unsafe_allow_html=True)

st.write("")
st.markdown("#### 我們的方法｜專業顧問＋AI 模組")
m1, m2, m3 = st.columns(3)
with m1:
    st.markdown('''<div class="card">
    <b>顧問框架</b><br/>以「家業／家產／家風」為主軸，建立可控的權責與現金流。
    </div>''', unsafe_allow_html=True)
with m2:
    st.markdown('''<div class="card" id="tools">
    <b>AI 工具箱</b><br/>遺產稅估算、贈與壓縮、保單策略模擬、價值觀探索。
    </div>''', unsafe_allow_html=True)
with m3:
    st.markdown('''<div class="card">
    <b>法稅合規</b><br/>整合法稅與保險策略，重視風險防範與代間信任的建立。
    </div>''', unsafe_allow_html=True)

st.write("")
st.markdown("#### 社會信任與見證")
tc1, tc2 = st.columns(2)
with tc1:
    st.markdown('''<div class="card">
    <b>教學與培訓</b><br/>勞動部《理財規劃實務》《傳承規劃實務》講師；企業主專題講座。
    </div>''', unsafe_allow_html=True)
with tc2:
    st.markdown('''<div class="card">
    <b>真實案例</b><br/>高齡長輩 5 億保額規劃：減輕稅負、婚前財產隔離、三代共好。
    </div>''', unsafe_allow_html=True)

st.write("")
st.markdown("---")

# --- Lead Form (Anchor: lead) ---
st.markdown('<a id="lead"></a>', unsafe_allow_html=True)
st.markdown("### 預約 30 分鐘傳承健檢")
st.caption("留下聯絡方式，將由顧問與您確認時間（線上或線下）。")

with st.form("lead_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("姓名/稱呼 *")
        phone = st.text_input("手機 *")
        email = st.text_input("Email（可選）")
    with col2:
        role = st.selectbox("身份", ["創辦人/一代", "企業管理層", "二代/家族成員", "顧問/會計師/律師", "其他"])
        date_pref = st.date_input("偏好日期", value=None)
        time_pref = st.selectbox("時段偏好", ["上午", "下午", "不限"])

    memo = st.text_area("想先讓我們了解的重點（可選）", placeholder="例：資產分佈、傳承顧慮、跨境情境、股權安排…")

    agreed = st.checkbox("我同意由永傳家族傳承導師與我聯繫，提供傳承健檢與後續資訊。", value=True)
    submitted = st.form_submit_button("送出預約")

if submitted and agreed and name and phone:
    save_path = "leads.csv"
    new_row = [datetime.now().isoformat(), name, phone, email, role, str(date_pref) if date_pref else "", time_pref, memo]
    write_header = not os.path.exists(save_path)
    with open(save_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["created_at","name","phone","email","role","date_pref","time_pref","memo"])
        writer.writerow(new_row)
    st.success("已收到您的預約，我們將盡快與您確認時間。謝謝！")
elif submitted and not (name and phone):
    st.warning("請填寫姓名與手機，以便聯繫您。")

st.write("")
st.markdown("----")
st.markdown(
    "《影響力》傳承策略平台｜永傳家族辦公室  \n"
    "聯絡信箱：123@gracefo.com  \n"
    "© " + str(datetime.now().year) + " Grace Family Office"
)
