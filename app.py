
import streamlit as st
from datetime import datetime, date
import csv, os

st.set_page_config(
    page_title="永傳家族傳承導師｜《影響力》傳承策略平台",
    page_icon="assets/favicon.png",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- Global CSS ----------
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
/* Hide and remove the sidebar completely */
[data-testid="stSidebar"] { display: none !important; }
section[data-testid="stSidebar"] { display: none !important; }
.block-container {max-width: 1200px !important;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Light hero (no heavy background) */
.hero {
  border-radius: 20px;
  padding: 28px 28px;
  color: #0F172A;
  background: rgba(255,255,255,0.8);
  border: 1px solid rgba(15,23,42,0.08);
  backdrop-filter: blur(2px);
  margin-bottom: 24px;
}
.hero h1 { font-size: 36px; margin-bottom: 10px; }
.hero p { font-size: 18px; opacity: 0.95; }

.card {
  padding: 18px 16px;
  border-radius: 16px;
  border: 1px solid rgba(20, 20, 20, 0.08);
  background: #fff;
  box-shadow: 0 6px 18px rgba(10, 28, 58, 0.06);
}

.navbar{
  display:flex; gap:10px; flex-wrap:wrap; margin-bottom:8px;
}
.navbtn{
  display:inline-block; padding:10px 14px; border-radius:999px;
  border:1px solid rgba(15,23,42,0.12); background:#fff; text-decoration:none !important;
}
.cta { display:inline-block; padding:12px 18px; border-radius:999px; background:#F4B400; color:#111 !important; font-weight:700; text-decoration:none !important; margin-right:8px;}
.ghost { display:inline-block; padding:12px 18px; border-radius:999px; border:2px solid #F4B400; color:#F4B400 !important; font-weight:700; text-decoration:none !important;}
hr{border:none; border-top:1px solid #eee; margin:20px 0;}
</style>
""", unsafe_allow_html=True)

# --- Top Brand + Simple Navbar ---
col_logo, col_head = st.columns([1,3], vertical_alignment="center")
with col_logo:
    st.image("assets/logo.png", use_container_width=True)
with col_head:
    st.markdown("### 永傳家族傳承導師｜《影響力》傳承策略平台")
    st.caption("專業 × 溫暖 × 信任｜讓家族的愛與資產，都能安全傳承三代。")
    st.markdown('<div class="navbar">', unsafe_allow_html=True)
    st.page_link("app.py", label="首頁", icon="🏠")
    st.page_link("pages/1_解決方案.py", label="解決方案", icon="🧭")
    st.page_link("pages/2_工具箱.py", label="工具箱", icon="🧰")
    st.page_link("pages/3_成功案例.py", label="成功案例", icon="🏆")
    st.page_link("pages/4_關於與聯絡.py", label="關於與聯絡", icon="🤝")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Hero Section (no dark background) ---
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
st.markdown("#### 我們的方法｜專業顧問＋AI 模組", help="方法論與工具並行，提升決策品質與效率")
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

# --- Quick Links Section to your tools/pages ---
st.write("")
st.markdown("#### 工具快速入口")
ql1, ql2, ql3, ql4 = st.columns(4)
with ql1: st.page_link("pages/2_工具箱.py", label="打開 AI 工具箱", icon="🧰")
with ql2: st.page_link("pages/1_解決方案.py", label="查看解決方案", icon="🧭")
with ql3: st.page_link("pages/3_成功案例.py", label="瀏覽成功案例", icon="🏆")
with ql4: st.page_link("pages/4_關於與聯絡.py", label="聯絡我們", icon="🤝")

st.write("")
st.markdown("---")

# --- Lead Form (Anchor: lead) ---
st.markdown('<a id="lead"></a>', unsafe_allow_html=True)
st.markdown("### 預約 30 分鐘傳承健檢")

st.caption("送出後，系統會將資料寫入 `leads.csv`，並嘗試寄信通知。")

def _send_email_notification(payload: dict):
    try:
        import smtplib
        from email.message import EmailMessage
        s = st.secrets.get("smtp", {})
        host = s.get("host")
        port = int(s.get("port", 587))
        user = s.get("user")
        pwd  = s.get("pass")
        to   = s.get("to", "123@gracefo.com")

        if not (host and user and pwd):
            return False, "未設定 SMTP 憑證，略過寄信"

        msg = EmailMessage()
        msg["Subject"] = "【傳承健檢預約】" + payload.get("name", "")
        msg["From"] = user
        msg["To"] = to
        lines = [f"{k}: {v}" for k, v in payload.items()]
        msg.set_content("\\n".join(lines))

        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(user, pwd)
            server.send_message(msg)
        return True, "Email 已寄出"
    except Exception as e:
        return False, f"寄信失敗：{e}"



with st.form("lead_form", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("姓名/稱呼（必填） *")
        phone = st.text_input("手機（必填） *")
        email = st.text_input("Email（必填） *")
    with col2:
        role = st.selectbox("身份（必填） *", ["創辦人/一代", "企業管理層", "二代/家族成員", "顧問/會計師/律師", "其他"])
        date_pref = st.date_input("偏好日期（可選）", value=None)
        time_pref = st.selectbox("時段偏好（必填） *", ["上午", "下午", "不限"], index=2)

    st.markdown("**想先讓我們了解的重點（必填）**")
    PRESET_TOPICS = [
        "跨境資產 / 申報與風險",
        "股權與投票權安排",
        "現金流模型 / 家族分配秩序",
        "贈與節奏 / 保單壓縮策略",
        "婚前財產隔離 / 家族保障",
        "教育金 / 創業金安排",
    ]
    topics = st.multiselect("請勾選適用主題（可複選）", PRESET_TOPICS, default=[])
    memo = st.text_area("補充說明（必填，可加入未列之主題） *", placeholder="例：資產分佈、跨境情境、股權安排…")

    agreed = st.checkbox("我同意由永傳家族傳承導師與我聯繫，提供傳承健檢與後續資訊。", value=True)
    required_ok = all([name.strip(), phone.strip(), email.strip(), role.strip(), time_pref.strip(), agreed, (len(topics) > 0 or memo.strip())])
    submitted = st.form_submit_button('送出預約')

if submitted:
    errors = []
    if not name.strip(): errors.append('請填寫姓名')
    if not phone.strip(): errors.append('請填寫手機')
    if not email.strip(): errors.append('請填寫 Email')
    if not role.strip(): errors.append('請選擇身份')
    if not time_pref.strip(): errors.append('請選擇時段偏好')
    if not (len(topics) > 0 or memo.strip()): errors.append('請至少勾選一個主題或填寫補充說明')
    if not agreed: errors.append('請勾選同意聯繫')
    if errors:
        st.error('；'.join(errors))
        st.stop()
    topics_str = ", ".join(topics) if topics else ""
    memo_full = (topics_str + ("；" if topics_str and memo.strip() else "") + memo.strip()).strip()
    save_path = "leads.csv"
    new_row = [datetime.now().isoformat(), name.strip(), phone.strip(), email.strip(), role, str(date_pref) if date_pref else "", time_pref, memo_full, "首頁"]
    write_header = not os.path.exists(save_path)
    with open(save_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if write_header:
            writer.writerow(["created_at","name","phone","email","role","date_pref","time_pref","memo","source_page"])
        writer.writerow(new_row)

    payload = {
        "created_at": new_row[0], "name": new_row[1], "phone": new_row[2],
        "email": new_row[3], "role": new_row[4], "date_pref": new_row[5],
        "time_pref": new_row[6], "memo": new_row[7], "source_page": "首頁"
    }
    # reuse helper if exists
    try:
        from src.utils.lead import _send_email_notification
        ok, msg = _send_email_notification(payload)
        if ok:
            st.success("✅ 已收到您的預約，並已發送 Email 通知。")
        else:
            st.success("✅ 已收到您的預約。"); st.caption(msg)
    except Exception as e:
        st.success("✅ 已收到您的預約（未寄信）。")
        st.caption(str(e))

    st.caption("資料已寫入專案根目錄的 `leads.csv`。")
st.markdown("----")
st.markdown(
    "《影響力》傳承策略平台｜永傳家族辦公室  \n"
    "聯絡信箱：123@gracefo.com  \n"
    "© " + str(datetime.now().year) + " Grace Family Office"
)
