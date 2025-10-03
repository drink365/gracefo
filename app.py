import streamlit as st
from datetime import datetime
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path

try:
    from PIL import UnidentifiedImageError
except Exception:
    class UnidentifiedImageError(Exception): ...
LOGO = Path("logo.png")
FAVICON = Path("logo2.png")
FONT = Path("NotoSansTC-Regular.ttf")
FONT_NAME = "NotoSansTC"

st.set_page_config(
    page_title="永傳影響力傳承平台｜客戶入口",
    page_icon=str(FAVICON) if FAVICON.exists() else "✨",
    layout="wide",
)

if LOGO.exists():
    try:
        st.sidebar.image(str(LOGO), width=200)
    except UnidentifiedImageError:
        st.sidebar.warning("⚠️ logo.png 檔案格式無法辨識，請改用有效的 PNG/JPG。")
else:
    st.sidebar.info("提示：找不到 logo.png（請將檔案放在專案根目錄）。")

if FONT.exists():
    try:
        pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONT)))
        PDF_FONT = FONT_NAME
    except Exception as e:
        st.sidebar.warning(f"⚠️ 無法載入字型：{e}；暫以 Helvetica 生成 PDF（可能有中文亂碼）。")
        PDF_FONT = "Helvetica"
else:
    st.sidebar.info("提示：未找到 NotoSansTC-Regular.ttf；PDF 可能出現中文亂碼。")
    PDF_FONT = "Helvetica"

st.markdown(
    f"""
    <div style="padding:24px;border-radius:24px;background:linear-gradient(135deg,#eef2ff,#ffffff,#ecfdf5);border:1px solid rgba(15,23,42,0.12)">
      <div style="display:flex;align-items:center;gap:12px;">
        {f'<img src="{LOGO.as_posix()}" alt="logo" style="height:36px;border-radius:8px"/>' if LOGO.exists() else ''}
        <span style="display:inline-block;padding:6px 10px;border-radius:999px;background:#4f46e5;color:#fff;font-size:12px">永傳家族傳承導師</span>
      </div>
      <h1 style="margin:12px 0 8px 0;font-size:28px;line-height:1.2">AI × 財稅 × 傳承：<br/>您的「數位家族辦公室」入口</h1>
      <p style="color:#475569;margin:0">以顧問式陪伴，結合 AI 工具，快速看見稅務風險、傳承缺口與現金流安排。<br/>我們不推商品，只推動「讓重要的人真的被照顧到」。</p>
    </div>
    """, unsafe_allow_html=True
)

tab1, tab2, tab3 = st.tabs(["遺產稅｜快速估算", "傳承地圖｜需求快照（PDF）", "預約顧問｜一對一諮詢"])

with tab1:
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

with tab2:
    from datetime import datetime
    st.caption("先把最重要的人放進地圖，再談工具（PDF 供內部討論用）")
    with st.form("legacy_form"):
        who = st.text_input("想優先照顧的人（例如：太太／兒女／長輩）")
        assets = st.text_area("主要資產（公司股權、不動產、金融資產、保單、海外資產、其他）")
        concerns = st.text_area("傳承顧慮（稅負、婚前財產、接班、現金流、遺囑或信託等）")
        submitted = st.form_submit_button("生成傳承快照 PDF")
    if submitted:
        buf = BytesIO()
        c = canvas.Canvas(buf, pagesize=A4)

        def line(text, size=12, gap=18, bold=False):
            c.setFont(PDF_FONT, size)
            y = line.y
            for seg in text.split("\n"):
                c.drawString(60, y, seg)
                y -= gap
            line.y = y
        line.y = A4[1] - 72

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
        c.setFont(PDF_FONT, 9)
        c.drawString(60, line.y, "＊本文件為教育用途，不構成任何金融商品或法律稅務建議。最終規劃以顧問與專業人士協作結果為準。")
        c.showPage()
        c.save()

        st.download_button("下載 PDF", data=buf.getvalue(), file_name="永傳_傳承快照.pdf", mime="application/pdf")
        st.success("已生成 PDF，適合作為與導師討論的起點。")

with tab3:
    with st.form("booking_form"):
        name = st.text_input("您的稱呼")
        email = st.text_input("Email")
        phone = st.text_input("聯絡電話")
        note = st.text_area("想優先解決的問題（例如：稅負、現金流、指定受益、跨境等）")
        ok = st.form_submit_button("送出預約需求")
    if ok:
        st.success("我們已收到您的預約需求。工作日內會與您聯繫，安排 20–30 分鐘初談。")

st.write("---")
st.caption(f"© {datetime.now().year} 《影響力》傳承策略平台｜永傳家族辦公室")
