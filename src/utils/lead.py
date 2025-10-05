
import streamlit as st
from datetime import datetime
import csv, os

PRESET_TOPICS = [
    "跨境資產 / 申報與風險",
    "股權與投票權安排",
    "現金流模型 / 家族分配秩序",
    "贈與節奏 / 保單壓縮策略",
    "婚前財產隔離 / 家族保障",
    "教育金 / 創業金安排",
]

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
        msg.set_content("\n".join(lines))

        with smtplib.SMTP(host, port) as server:
            server.starttls()
            server.login(user, pwd)
            server.send_message(msg)
        return True, "Email 已寄出"
    except Exception as e:
        return False, f"寄信失敗：{e}"

def _track_event(event_type: str, page_name: str, detail: str = ""):
    try:
        save_path = "events.csv"
        write_header = not os.path.exists(save_path)
        with open(save_path, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if write_header:
                w.writerow(["ts","event_type","page","detail"])
            w.writerow([datetime.now().isoformat(), event_type, page_name, detail])
    except Exception as e:
        pass

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

            # Validate required fields
            required_ok = all([
                name.strip(), phone.strip(), email.strip(), role.strip(), time_pref.strip(), agreed,
                (len(topics) > 0 or memo.strip())
            ])
            submitted = st.form_submit_button("送出預約", disabled=not required_ok)

        if submitted:
            topics_str = ", ".join(topics) if topics else ""
            memo_full = (topics_str + ("；" if topics_str and memo.strip() else "") + memo.strip()).strip()

            save_path = "leads.csv"
            new_row = [datetime.now().isoformat(), name.strip(), phone.strip(), email.strip(), role, "", time_pref, memo_full, page_name]
            write_header = not os.path.exists(save_path)
            with open(save_path, "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if write_header:
                    writer.writerow(["created_at","name","phone","email","role","date_pref","time_pref","memo","source_page"])
                writer.writerow(new_row)

            payload = {
                "created_at": new_row[0], "name": new_row[1], "phone": new_row[2],
                "email": new_row[3], "role": new_row[4], "date_pref": new_row[5],
                "time_pref": new_row[6], "memo": new_row[7], "source_page": page_name
            }
            ok, msg = _send_email_notification(payload)
            _track_event("lead_submit", page_name, "email_ok" if ok else "email_skip")

            if ok:
                st.success("✅ 已收到您的預約，並已發送 Email 通知。")
            else:
                st.success("✅ 已收到您的預約。")
                st.caption(msg)
            st.caption("資料已寫入 `leads.csv`；事件已記錄於 `events.csv`。")
