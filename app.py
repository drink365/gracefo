
import streamlit as st
from datetime import datetime
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path

LOGO = Path("logo.png")
FAVICON = Path("logo2.png")
FONT = Path("NotoSansTC-Regular.ttf")

st.set_page_config(
    page_title="永傳影響力傳承平台｜客戶入口",
    page_icon=str(FAVICON) if FAVICON.exists() else "✨",
    layout="wide",
)

# CSS override for st.metric
st.markdown("""
<style>
div[data-testid="stMetricValue"] {
    font-size: 20px !important;
    font-weight: 700 !important;
    color: #1e40af !important;
}
div[data-testid="stMetricLabel"] {
    font-size: 14px !important;
    color: #475569 !important;
}
</style>
""", unsafe_allow_html=True)

if LOGO.exists():
    st.sidebar.image(str(LOGO), width=200)
else:
    st.sidebar.info("找不到 logo.png（請放在專案根目錄）。")

FONT_NAME = "NotoSansTC"
if FONT.exists():
    try:
        pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONT)))
    except Exception as e:
        st.sidebar.warning(f"無法載入字型：{e}")
else:
    st.sidebar.info("提示：放入 NotoSansTC-Regular.ttf 以在 PDF 正確顯示繁體中文。")

INTEGRATIONS = {"has_gsheet": False, "has_sendgrid": False, "sheet_id": None, "notify_email": None}

try:
    if "gcp_service_account" in st.secrets and "SHEET_ID" in st.secrets:
        import gspread
        from google.oauth2.service_account import Credentials
        SCOPES = ["https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"]
        creds = Credentials.from_service_account_info(st.secrets["gcp_service_account"], scopes=SCOPES)
        gclient = gspread.authorize(creds)
        INTEGRATIONS["has_gsheet"] = True
        INTEGRATIONS["sheet_id"] = st.secrets["SHEET_ID"]
except Exception:
    st.sidebar.warning("⚠️ Google Sheets 尚未設定或金鑰有誤（目前以離線模式運作）。")

try:
    if "SENDGRID_API_KEY" in st.secrets and st.secrets["SENDGRID_API_KEY"]:
        from sendgrid import SendGridAPIClient
        from sendgrid.helpers.mail import Mail
        INTEGRATIONS["has_sendgrid"] = True
    if "NOTIFY_EMAIL" in st.secrets and st.secrets["NOTIFY_EMAIL"]:
        INTEGRATIONS["notify_email"] = st.secrets["NOTIFY_EMAIL"]
except Exception:
    st.sidebar.warning("⚠️ Email 通知尚未設定（會提供 mailto 傳送）。")

def append_row(sheet_title: str, row: list):
    if not INTEGRATIONS["has_gsheet"]:
        return False, "GSHEET_DISABLED"
    try:
        sh = gclient.open_by_key(INTEGRATIONS["sheet_id"])
        try:
            ws = sh.worksheet(sheet_title)
        except Exception:
            ws = sh.add_worksheet(title=sheet_title, rows=1000, cols=20)
            ws.append_row(["timestamp","name","email","phone","note","source"], value_input_option="USER_ENTERED")
        ws.append_row(row, value_input_option="USER_ENTERED")
        return True, "OK"
    except Exception as e:
        return False, str(e)

def send_email(subject: str, html: str):
    if not INTEGRATIONS["has_sendgrid"] or not INTEGRATIONS["notify_email"]:
        return False, "EMAIL_DISABLED"
    try:
        sg = SendGridAPIClient(st.secrets["SENDGRID_API_KEY"])
        message = Mail(from_email=INTEGRATIONS["notify_email"], to_emails=INTEGRATIONS["notify_email"],
                       subject=subject, html_content=html)
        resp = sg.send(message)
        return True, f"Status {resp.status_code}"
    except Exception as e:
        return False, str(e)

st.markdown(
    f"""
    <div style="padding:24px;border-radius:24px;background:linear-gradient(135deg,#eef2ff,#ffffff,#ecfdf5);border:1px solid rgba(15,23,42,0.12)">
      <div style="display:flex;align-items:center;gap:12px;">
        {f'<img src="{LOGO.as_posix()}" alt="logo" style="height:36px;border-radius:8px"/>' if LOGO.exists() else ''}
        <span style="display:inline-block;padding:6px 10px;border-radius:999px;background:#4f46e5;color:#fff;font-size:12px">永傳家族傳承導師</span>
      </div>
      <h2 style="margin:12px 0 8px 0;font-size:22px;line-height:1.3;color:#1e3a8a;font-weight:700">
        AI × 財稅 × 傳承：<br/>您的「數位家族辦公室」入口
      </h2>
      <p style="color:#475569;margin:0;font-size:14px">以顧問式陪伴，結合 AI 工具，快速看見稅務風險、傳承缺口與現金流安排。<br/>我們不推商品，只推動「讓重要的人真的被照顧到」。</p>
    </div>
    """, unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)
c1.metric("快速掌握傳承全貌", "約 7 分鐘")
c2.metric("顧問端效率", "提升 3×")
c3.metric("隱私保護", "本地試算")

st.write("---")
st.subheader("用 AI 先看見，再決定")

tab1, tab2, tab3 = st.tabs(["遺產稅｜快速估算", "傳承地圖｜需求快照（PDF）", "預約顧問｜一對一諮詢"])

with tab1:
    st.caption("輸入大致資產與扣除額，立即看見稅額區間（示意用途，實務請由顧問確認）")
    col1, col2 = st.columns(2)
    with col1:
        estate = st.number_input("估算總資產（TWD）", min_value=0, step=1_000_000, value=120_000_000)
    with col2:
        deduct = st.number_input("可扣除額（TWD）", min_value=0, step=500_000, value=0)
    free_amount = 12_000_000
    taxable = max(estate - deduct - free_amount, 0)
    tax = 0
    if taxable <= 50_000_000:
        tax = taxable * 0.10
    elif taxable <= 100_000_000:
        tax = 5_000_000 + (taxable - 50_000_000) * 0.15
    else:
        tax = 12_500_000 + (taxable - 100_000_000) * 0.20
    st.success(f"預估遺產稅額：約 NT$ {tax:,.0f}")
    st.caption("💡 以壽險承接＋指定受益搭配信託，可望進一步優化稅務與風險（需個案評估）。")

with tab2:
    st.caption("先把最重要的人放進地圖，再談工具（PDF 供內部討論用）")
    with st.form("legacy_form"):
        who = st.text_input("想優先照顧的人（例如：太太／兒女／長輩）")
        assets = st.text_area("主要資產（公司股權、不動產、金融資產、保單、海外資產、其他）")
        concerns = st.text_area("傳承顧慮（稅負、婚前財產、接班、現金流、遺囑或信託等）")
        email_for_pdf = st.text_input("（可選）留下 Email，方便我們把快照寄給您")
        submitted = st.form_submit_button("生成傳承快照 PDF")
    if submitted:
        buf = BytesIO()
        c = canvas.Canvas(buf, pagesize=A4)
        w, h = A4

        def line(text, size=12, gap=18, bold=False):
            font = FONT_NAME if FONT.exists() else ("Helvetica-Bold" if bold else "Helvetica")
            c.setFont(font, size)
            y = line.y
            for seg in text.split("\n"):
                c.drawString(60, y, seg)
                y -= gap
            line.y = y
        line.y = h - 72

        c.setTitle("永傳｜傳承快照")
        line("永傳影響力傳承平台｜傳承快照", 16, 24, bold=True)
        line(f"日期：{datetime.now().strftime('%Y-%m-%d %H:%M')}", 11, 16)
        line.y -= 8
        line("想優先照顧的人：", 12, 18, bold=True); line(who or "（尚未填寫）", 12, 18)
        line.y -= 6
        line("主要資產：", 12, 18, bold=True)
        for row in (assets or "（尚未填寫）").split("\n"):
            line(f"• {row}", 11, 16)
        line.y -= 6
        line("傳承顧慮：", 12, 18, bold=True)
        for row in (concerns or "（尚未填寫）").split("\n"):
            line(f"• {row}", 11, 16)
        line.y -= 18
        c.setFont(FONT_NAME if FONT.exists() else "Helvetica-Oblique", 9)
        c.drawString(60, line.y, "＊本文件為教育用途，不構成任何金融商品或法律稅務建議。最終規劃以顧問與專業人士協作結果為準。")
        c.showPage()
        c.save()

        st.download_button("下載 PDF", data=buf.getvalue(), file_name="永傳_傳承快照.pdf", mime="application/pdf")
        st.success("已生成 PDF，適合作為與導師討論的起點。")

        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if INTEGRATIONS["has_gsheet"]:
            ok, msg = append_row("Leads", [ts, "", email_for_pdf or "", "", f"who:{who}; concerns:{(concerns or '')[:60]}", "legacy_snapshot"])
            if ok:
                st.toast("✅ 已記錄到 Google Sheet：Leads")
            else:
                st.warning(f"⚠️ Google Sheet 寫入失敗：{msg}")

with tab3:
    st.caption("7 分鐘工具體驗後，預約深入討論更有感")
    with st.form("booking_form"):
        name = st.text_input("您的稱呼")
        email = st.text_input("Email")
        phone = st.text_input("聯絡電話")
        note = st.text_area("想優先解決的問題（例如：稅負、現金流、指定受益、跨境等）")
        ok = st.form_submit_button("送出預約需求")
    if ok:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if INTEGRATIONS["has_gsheet"]:
            ok1, msg1 = append_row("Bookings", [ts, name, email, phone, note, "web_form"])
            if ok1:
                st.toast("✅ 已寫入 Google Sheet：Bookings")
            else:
                st.warning(f"⚠️ Google Sheet 寫入失敗：{msg1}")
        if INTEGRATIONS["has_sendgrid"] and INTEGRATIONS["notify_email"]:
            subject = f"【永傳預約】{name or '未留名'}"
            html = f"""<p>時間：{ts}</p><p>姓名：{name}</p><p>Email：{email}</p><p>電話：{phone}</p><p>需求：{note}</p>"""
            ok2, msg2 = send_email(subject, html)
            if ok2:
                st.toast("📧 已寄出 Email 通知")
            else:
                st.warning(f"⚠️ Email 發送失敗：{msg2}")
        st.success("我們已收到您的預約需求。工作日內會與您聯繫，安排 20–30 分鐘初談。")
        if not INTEGRATIONS["has_sendgrid"]:
            mailto = f"mailto:123@gracefo.com?subject=【永傳預約】{name or '未填名'}&body=" + f"Email:{email}%0A電話:{phone}%0A需求:{note}"
            st.markdown(f"[或直接寄信通知我們]({mailto})")

st.write("---")
lcol, rcol = st.columns([2,1])
with lcol:
    st.markdown("""
**永傳家族傳承導師**  
傳承，不只是資產的安排，更是讓關心的人，在需要時真的被照顧到。
""")
with rcol:
    st.markdown("""
**聯絡**
- 官網：gracefo.com  
- 信箱：123@gracefo.com  
- LINE／QR：請置入圖片（images/line_qr.png）
""")
st.caption(f"© {datetime.now().year} 《影響力》傳承策略平台｜永傳家族辦公室")
