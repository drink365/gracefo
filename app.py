import streamlit as st

# ==== Booking: Email (admin + auto-reply) + Google Sheets logging ====
import smtplib, csv, json
from email.message import EmailMessage
from datetime import datetime

def _smtp_cfg_ok():
    smtp_cfg = st.secrets.get("smtp", {})
    book_cfg = st.secrets.get("booking", {})
    return bool(smtp_cfg.get("host") and smtp_cfg.get("username") and smtp_cfg.get("password") and book_cfg.get("to"))

def _send_email(subject: str, body: str, to_addr: str, cc_addr: str = "", from_addr: str | None = None) -> tuple[bool, str]:
    try:
        smtp_cfg = st.secrets.get("smtp", {})
        host = smtp_cfg.get("host"); port = int(smtp_cfg.get("port", 587))
        username = smtp_cfg.get("username"); password = smtp_cfg.get("password")
        use_tls = bool(smtp_cfg.get("use_tls", True))
        sender = from_addr or username

        em = EmailMessage()
        em["Subject"] = subject
        em["From"] = sender
        em["To"] = to_addr
        if cc_addr:
            em["Cc"] = cc_addr
        em.set_content(body)

        with smtplib.SMTP(host, port, timeout=20) as smtp:
            if use_tls:
                smtp.starttls()
            smtp.login(username, password)
            smtp.send_message(em)

        return True, f"已寄出到 {to_addr}{('；副本：' + cc_addr) if cc_addr else ''}"
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"

def _notify_admin(name: str, phone: str, email: str, slot: str, msg: str) -> tuple[bool, str]:
    book_cfg = st.secrets.get("booking", {})
    to_addr = book_cfg.get("to", "")
    cc_addr = book_cfg.get("cc", "")
    subject = "📅 新預約：影響力傳承健檢"
    body = f"""【新預約】
姓名/稱呼：{name}
手機：{phone}
Email：{email or '-'}
偏好時段：{slot}
需求/備註：{msg}

送出時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    return _send_email(subject, body, to_addr, cc_addr)

def _auto_reply(email: str, name: str) -> tuple[bool, str] | tuple[None, str]:
    if not email:
        return (None, "無信箱，略過自動回覆")
    book_cfg = st.secrets.get("booking", {})
    from_addr = book_cfg.get("auto_reply_from")  # 可選：若未設定則用 smtp.username
    subject = "我們已收到您的預約｜永傳家族傳承導師"
    body = f"""{name} 您好：

我們已收到您的預約，顧問會盡快與您聯繫，安排 30 分鐘傳承健檢（線上或現場皆可）。

若想提前提供資料或指定議題，歡迎直接回覆此信。
期待與您聊聊，祝順心！

— 《影響力》傳承策略平台｜永傳家族辦公室
gracefo.com
"""
    return _send_email(subject, body, email, cc_addr="", from_addr=from_addr)

def _append_booking_csv(name: str, phone: str, email: str, slot: str, msg: str, csv_path: str = "booking_backup.csv") -> None:
    try:
        exists = os.path.exists(csv_path)
        with open(csv_path, "a", newline="", encoding="utf-8") as f:
            import csv as _csv
            w = _csv.writer(f)
            if not exists:
                w.writerow(["timestamp", "name", "phone", "email", "slot", "message"])
            w.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, phone, email, slot, msg])
    except Exception:
        pass

def _log_to_gsheets(name: str, phone: str, email: str, slot: str, msg: str) -> tuple[bool, str]:
    try:
        gs = st.secrets.get("gsheets", {})
        import gspread
        creds = gs.get("service_account")
        if not creds:
            return False, "未設定 gsheets.service_account"
        sh_id = gs.get("spreadsheet_id"); ws_name = gs.get("worksheet_name", "booking")
        if not sh_id:
            return False, "未設定 gsheets.spreadsheet_id"

        gc = gspread.service_account_from_dict(creds)
        sh = gc.open_by_key(sh_id)
        try:
            ws = sh.worksheet(ws_name)
        except Exception:
            ws = sh.add_worksheet(title=ws_name, rows=1000, cols=10)
            ws.append_row(["timestamp", "name", "phone", "email", "slot", "message"])
        ws.append_row([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), name, phone, email, slot, msg])
        return True, "已寫入 Google Sheet"
    except Exception as e:
        return False, f"GS 錯誤：{e}"

import base64

# 設定頁面
st.set_page_config(
    page_title="《影響力》 | 高資產家庭的傳承策略入口",
    page_icon="🌿",
    layout="centered"
)

# 讀取 logo
def load_logo_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

try:
    logo_base64 = load_logo_base64("logo.png")
    st.markdown(f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{logo_base64}' width='200'><br>
    </div>
    """, unsafe_allow_html=True)
except:
    st.warning("⚠️ 無法載入 logo.png，請確認檔案存在")

# --- 品牌標語區 ---
st.markdown("""
<div style='text-align: center; margin-top: 2em;'>
    <h1 style='font-size: 36px; font-weight: bold;'>《影響力》</h1>
    <p style='font-size: 24px; color: #333; font-weight: bold; letter-spacing: 0.5px;'>
        高資產家庭的 <span style="color:#006666;">傳承策略平台</span>
    </p>
    <p style='font-size: 18px; color: #888; margin-top: -10px;'>
        讓每一分資源，都成為你影響力的延伸
    </p>
</div>
""", unsafe_allow_html=True)

# --- 品牌開場語 ---
st.markdown("""
<div style='text-align: center; margin-top: 3em; font-size: 18px; line-height: 1.8;'>
    《影響力》是一個專為高資產家庭打造的傳承策略平台。<br>
    我們陪你設計每一分資源的去向，<br>
    讓它能守護最重要的人，延續你真正的價值。
</div>
""", unsafe_allow_html=True)

# --- 三大價值主張 ---
st.markdown("""
<div style='display: flex; justify-content: center; gap: 40px; margin-top: 3em; flex-wrap: wrap;'>
    <div style='width: 280px; text-align: center;'>
        <h3>🏛️ 富足結構</h3>
        <p>為資產設計流動性與穩定性，讓財富更有效率地守護人生階段。</p>
    </div>
    <div style='width: 280px; text-align: center;'>
        <h3>🛡️ 風險預備</h3>
        <p>從保單、稅源到信託制度，設計資產的防禦系統與轉移機制。</p>
    </div>
    <div style='width: 280px; text-align: center;'>
        <h3>🌱 價值傳遞</h3>
        <p>不只是金錢，更是精神、信任與選擇，成就跨世代的連結。</p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 使用者分流 ---
st.markdown("---")
st.markdown("### 🧭 請選擇您的身份：")

col1, col2 = st.columns(2)
with col1:
    if st.button("🙋 我是客戶", use_container_width=True):
        st.switch_page("pages/client_home.py")
with col2:
    if st.button("🧑‍💼 我是顧問", use_container_width=True):
        st.switch_page("pages/advisor_home.py")

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


# ---- Admin-only tools: test email ----
try:
    if st.session_state.get("role") == "admin":
        st.info("管理工具（僅 admin 可見）")
        if st.button("發送測試郵件（到 booking.to）"):
            if _smtp_cfg_ok():
                ok, info = _send_email("TEST｜預約系統測試", "這是一封測試郵件。", st.secrets["booking"]["to"])
                st.success("測試結果：" + ("成功" if ok else "失敗") + "｜" + info)
            else:
                st.warning("SMTP 或收件人設定不完整")
except Exception:
    pass

