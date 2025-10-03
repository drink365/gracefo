import streamlit as st
from datetime import datetime
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path
import base64

# === 檔案路徑 ===
LOGO = Path("logo.png")
FAVICON = Path("logo2.png")
FONT = Path("NotoSansTC-Regular.ttf")

# === 工具：base64 讀檔 ===
def get_base64_of_file(path: Path) -> str | None:
    try:
        if path.exists() and path.stat().st_size > 0:
            return base64.b64encode(path.read_bytes()).decode()
    except Exception:
        pass
    return None

# === 頁面設定 ===
st.set_page_config(
    page_title="永傳影響力傳承平台｜客戶入口",
    page_icon=str(FAVICON) if FAVICON.exists() else "✨",
    layout="wide",
)

# === CSS ===
st.markdown("""
<style>
/* 亮點數字 */
div[data-testid="stMetricValue"] {
    font-size: 20px !important;
    font-weight: 700 !important;
    color: #1e40af !important;
}
/* 亮點標籤 */
div[data-testid="stMetricLabel"] {
    font-size: 18px !important;
    font-weight: 700 !important;
    color: #1e293b !important;
}
/* 按鈕樣式 */
div.stButton > button:first-child,
div.stDownloadButton > button {
    background-color: #2563eb;
    color: white;
    border-radius: 8px;
    padding: 0.5em 1em;
    font-weight: 600;
}
div.stButton > button:first-child:hover,
div.stDownloadButton > button:hover {
    background-color: #1d4ed8;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# === PDF 繁中字型 ===
FONT_NAME = "NotoSansTC"
if FONT.exists():
    try:
        pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONT)))
    except Exception:
        st.sidebar.warning("⚠️ 無法載入字型")

# === 頂部框 ===
logo_b64 = get_base64_of_file(LOGO)
logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="height:42px"/>' if logo_b64 else ""

st.markdown(
    f"""
    <div style="padding:24px;border-radius:24px;
                background:linear-gradient(135deg,#eef2ff,#ffffff,#ecfdf5);
                border:1px solid rgba(15,23,42,0.12)">
      <div style="display:flex;align-items:center;gap:12px;">
        {logo_html}
        <span style="display:inline-block;padding:6px 10px;border-radius:999px;
                     background:#4f46e5;color:#fff;font-size:12px">
            永傳家族傳承導師
        </span>
      </div>
      <h2 style="margin:12px 0 8px 0;font-size:22px;line-height:1.3;
                 color:#1e3a8a;font-weight:700">
        AI × 財稅 × 傳承：<br/>您的「數位家族辦公室」入口
      </h2>
      <p style="color:#475569;margin:0;font-size:14px">
        以顧問式陪伴，結合 AI 工具，快速看見稅務風險、傳承缺口與現金流安排。
      </p>
    </div>
    <br/>
    """,
    unsafe_allow_html=True
)

# === 亮點區 ===
c1, c2, c3 = st.columns(3)
c1.metric("快速掌握傳承全貌", "約 7 分鐘")
c2.metric("顧問端效率", "提升 3×")
c3.metric("隱私保護", "本地試算")

st.write("---")
st.subheader("用 AI 先看見，再決定")

# === Tabs ===
tab1, tab2, tab3 = st.tabs(["遺產稅｜快速估算", "傳承地圖｜需求快照（PDF）", "預約顧問｜一對一諮詢"])

# === Tab1: 遺產稅快速估算 ===
with tab1:
    st.caption("輸入大致資產，系統自動計算稅額，並根據家庭狀況顯示扣除額。")

    col1, col2 = st.columns(2)
    with col1:
        estate = st.number_input("估算總資產（TWD）", min_value=0, step=1_000_000, value=120_000_000)
    with col2:
        family_type = st.selectbox(
            "請選擇家庭狀況",
            ["未婚無子女", "已婚有配偶無子女", "已婚有配偶與子女", "有父母健在", "單身有子女"]
        )

    heirs = ""
    deductions = 12_000_000  # 基本免稅額
    if family_type == "未婚無子女":
        heirs = "父母、兄弟姊妹"
        deductions += 4_000_000
    elif family_type == "已婚有配偶無子女":
        heirs = "配偶、父母"
        deductions += 4_000_000 + 4_000_000
    elif family_type == "已婚有配偶與子女":
        heirs = "配偶、子女"
        deductions += 4_000_000 + 2_000_000 * 2
    elif family_type == "有父母健在":
        heirs = "父母"
        deductions += 4_000_000
    elif family_type == "單身有子女":
        heirs = "子女"
        deductions += 2_000_000 * 2

    st.info(f"👉 法定繼承人：{heirs}")
    st.success(f"👉 可適用扣除額：約 NT$ {deductions:,.0f}")

    taxable = max(estate - deductions, 0)
    if taxable <= 50_000_000:
        tax = taxable * 0.10
    elif taxable <= 100_000_000:
        tax = 5_000_000 + (taxable - 50_000_000) * 0.15
    else:
        tax = 12_500_000 + (taxable - 100_000_000) * 0.20

    st.success(f"預估遺產稅額：約 NT$ {tax:,.0f}")

# === Tab2: 傳承快照 PDF ===
with tab2:
    st.caption("快速輸入／點選，生成傳承快照 PDF")

    # --- 快速詞彙 ---
    st.caption("常見的傳承顧慮（可點選快速加入）")
    suggested_concerns = ["稅負過高", "婚前財產隔離", "企業接班", "現金流不足", "遺囑設計", "信託安排"]
    if "concerns" not in st.session_state:
        st.session_state.concerns = ""

    cols = st.columns(len(suggested_concerns))
    for i, word in enumerate(suggested_concerns):
        if cols[i].button(word, key=f"concern_{i}"):
            st.session_state.concerns += ("" if st.session_state.concerns == "" else "\n") + word

    with st.form("legacy_form"):
        who = st.text_input("想優先照顧的人（例如：太太／兒女／長輩）")
        assets = st.text_area("主要資產（公司股權、不動產、金融資產、保單、海外資產、其他）")
        concerns = st.text_area("傳承顧慮（可自行補充）", value=st.session_state.concerns)
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

        c.showPage(); c.save()

        st.download_button("下載 PDF", data=buf.getvalue(), file_name="永傳_傳承快照.pdf", mime="application/pdf")
        st.success("已生成 PDF，可作為與導師討論的起點。")

# === Tab3: 預約 ===
with tab3:
    with st.form("booking_form"):
        name = st.text_input("您的稱呼")
        email = st.text_input("Email")
        phone = st.text_input("聯絡電話")
        note = st.text_area("想優先解決的問題")
        ok = st.form_submit_button("送出預約需求")
    if ok:
        st.success("我們已收到您的預約需求。")
