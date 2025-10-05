
import streamlit as st
from datetime import datetime

PRESET_TOPICS = [
    "跨境資產 / 申報與風險",
    "股權與投票權安排",
    "現金流模型 / 家族分配秩序",
    "贈與節奏 / 保單壓縮策略",
    "婚前財產隔離 / 家族保障",
    "教育金 / 創業金安排",
]

def _send_email_notification(payload: dict):
    """Email via st.secrets['smtp'] settings. Supports username/password & booking.to fallback."""
    try:
        import smtplib
        from email.message import EmailMessage
        s = st.secrets.get("smtp", {})
        booking = st.secrets.get("booking", {})
        host = s.get("host")
        port = int(s.get("port", 587))
        user = s.get("user") or s.get("username")
        pwd  = s.get("pass") or s.get("password")
        to   = s.get("to") or booking.get("to") or "123@gracefo.com"
        use_tls = s.get("use_tls", True)
        use_ssl = s.get("use_ssl", False) or (str(port) == "465")

        if not (host and user and pwd):
            return False, "未設定 SMTP 憑證，略過寄信"

        msg = EmailMessage()
        msg["Subject"] = "【傳承健檢預約】" + payload.get("name", "")
        msg["From"] = user
        msg["To"] = to
        body_lines = [f"{k}: {v}" for k, v in payload.items()]
        msg.set_content("\n".join(body_lines))

        if use_ssl:
            with smtplib.SMTP_SSL(host, port) as server:
                server.login(user, pwd)
                server.send_message(msg)
        else:
            with smtplib.SMTP(host, port) as server:
                if use_tls: server.starttls()
                server.login(user, pwd)
                server.send_message(msg)
        return True, "Email 已寄出"
    except Exception as e:
        return False, f"寄信失敗：{e}"

def render_lead_cta(page_name: str):
    st.markdown("---")
    st.subheader("📅 想把今天討論的重點，轉成行動？")
    with st.expander("→ 立即預約 30 分鐘傳承健檢（點此展開表單）", expanded=False):
        with st.form("lead_form_" + page_name, clear_on_submit=True):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input("姓名/稱呼（必填） *")
                phone = st.text_input("手機（必填） *")
                email = st.text_input("Email（必填） *")
            with col2:
                role = st.selectbox("身份（必填） *", ["創辦人/一代", "企業管理層", "二代/家族成員", "顧問/會計師/律師", "其他"])
                time_pref = st.selectbox("時段偏好（必填） *", ["上午", "下午", "不限"], index=2)

            st.markdown("**想先讓我們了解的重點（必填）**")
            topics = st.multiselect("請勾選適用主題（可複選）", PRESET_TOPICS, default=[])
            memo = st.text_area("補充說明（必填，可加入未列之主題） *", placeholder="例：資產分佈、跨境情境、股權安排…")

            agreed = st.checkbox("我同意由永傳家族傳承導師與我聯繫，提供傳承健檢與後續資訊。", value=True)

            submitted = st.form_submit_button("送出預約")

        if submitted:
            # Server-side validation
            errors = []
            if not name.strip(): errors.append("請填寫姓名")
            if not phone.strip(): errors.append("請填寫手機")
            if not email.strip(): errors.append("請填寫 Email")
            if not role.strip(): errors.append("請選擇身份")
            if not time_pref.strip(): errors.append("請選擇時段偏好")
            if not (len(topics) > 0 or memo.strip()): errors.append("請至少勾選一個主題或填寫補充說明")
            if not agreed: errors.append("請勾選同意聯繫")
            if errors:
                st.error("；".join(errors))
                st.stop()

            topics_str = ", ".join(topics) if topics else ""
            memo_full = (topics_str + ("；" if topics_str and memo.strip() else "") + memo.strip()).strip()

            payload = {
                "created_at": datetime.now().isoformat(),
                "name": name.strip(),
                "phone": phone.strip(),
                "email": email.strip(),
                "role": role,
                "date_pref": "",
                "time_pref": time_pref,
                "memo": memo_full,
                "source_page": page_name
            }
            ok, msg = _send_email_notification(payload)

            if ok:
                st.success("✅ 已收到您的預約，並已發送 Email 通知。")
            else:
                st.success("✅ 已收到您的預約（未寄信）。")
                st.caption(msg)
