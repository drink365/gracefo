import streamlit as st
from datetime import datetime
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from pathlib import Path
import base64
from PIL import Image

# ----------------------------
# 檔案與字型
# ----------------------------
LOGO = Path("logo.png")
FAVICON = Path("logo2.png")
FONT = Path("NotoSansTC-Regular.ttf")

def get_base64_of_file(path: Path) -> str | None:
    try:
        if path.exists() and path.stat().st_size > 0:
            return base64.b64encode(path.read_bytes()).decode()
    except Exception:
        pass
    return None

# ----------------------------
# 頁面設定
# ----------------------------
st.set_page_config(
    page_title="永傳影響力傳承平台｜客戶入口",
    page_icon=str(FAVICON) if FAVICON.exists() else "✨",
    layout="wide",
)

# ----------------------------
# PDF 字型
# ----------------------------
FONT_NAME = "NotoSansTC"
if FONT.exists():
    try:
        pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONT)))
    except:
        pass

# ----------------------------
# 頂部區塊
# ----------------------------
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
      <h2 style="margin:12px 0 8px 0;font-size:22px;line-height:1.3;color:#1e3a8a;font-weight:700">
        AI × 財稅 × 傳承：您的「數位家族辦公室」入口
      </h2>
      <p style="color:#475569;margin:0;font-size:14px">
        以顧問式陪伴，結合 AI 工具，快速看見稅務風險、傳承缺口與現金流安排。
      </p>
    </div>
    <br/>
    """,
    unsafe_allow_html=True
)

# ============================================================
# Tab2: PDF 生成功能（只示範這一段）
# ============================================================
who = st.text_input("想優先照顧的人")
assets = st.text_area("主要資產")
concerns = st.text_area("傳承顧慮")

if st.button("生成傳承快照 PDF"):
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    w, h = A4
    x_pad, y_top, y_footer = 60, h - 60, 36

    # ====== Logo 顯示（用 Pillow 轉成 RGB 確保能讀）======
    text_y = y_top
    if LOGO.exists():
        try:
            pil_img = Image.open(str(LOGO)).convert("RGB")
            pil_buf = BytesIO()
            pil_img.save(pil_buf, format="PNG")
            pil_buf.seek(0)
            logo_img = ImageReader(pil_buf)
            logo_h = 40
            c.drawImage(logo_img, x_pad, y_top - logo_h,
                        height=logo_h, preserveAspectRatio=True, mask="auto")
            text_y = y_top - logo_h - 10
        except Exception as e:
            st.warning(f"⚠️ Logo 載入失敗：{e}")

    # ====== 文字工具 ======
    TITLE_FONT = FONT_NAME if FONT.exists() else "Helvetica-Bold"
    BODY_FONT = FONT_NAME if FONT.exists() else "Helvetica"

    def line(text, size=12, gap=18, bold=False):
        font = TITLE_FONT if bold else BODY_FONT
        c.setFont(font, size)
        y = line.y
        for seg in (text or "").split("\n"):
            c.drawString(x_pad, y, seg)
            y -= gap
        line.y = y
    line.y = text_y

    # ====== 內容 ======
    c.setTitle("永傳｜傳承快照")
    line("永傳影響力傳承平台｜傳承快照", 16, 24, bold=True)
    line(f"日期：{datetime.now().strftime('%Y-%m-%d %H:%M')}", 11, 18)
    line.y -= 6

    line("想優先照顧的人：", 12, 18, bold=True); line(who or "（尚未填寫）", 12, 18)
    line.y -= 6
    line("主要資產：", 12, 18, bold=True)
    for row in (assets or "（尚未填寫）").split("\n"):
        if row.strip():
            line(f"• {row}", 11, 16)
    line.y -= 6
    line("傳承顧慮：", 12, 18, bold=True)
    for row in (concerns or "（尚未填寫）").split("\n"):
        if row.strip():
            line(f"• {row}", 11, 16)

    # ====== 暖心收尾（緊接在文案最後）======
    line.y -= 12
    line("永傳家族傳承導師", 12, 18, bold=True)
    line("傳承，不只是資產的安排，更是讓關心的人，在需要時真的被照顧到。", 11, 18)

    # ====== 版權（最底）======
    c.setFont(BODY_FONT, 10)
    c.drawRightString(w - x_pad, y_footer, "© 2025 《影響力》傳承策略平台｜永傳家族辦公室")

    c.showPage()
    c.save()

    st.download_button("下載 PDF", data=buf.getvalue(),
                       file_name="永傳_傳承快照.pdf", mime="application/pdf")
    st.success("已生成 PDF（含 Logo 與暖心收尾文字）。")
