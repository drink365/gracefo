import streamlit as st
from datetime import datetime
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from pathlib import Path
from PIL import Image
import base64

# ----------------------------
# 檔案與字型路徑
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
# 全域樣式（低調標籤）
# ----------------------------
st.markdown("""
<style>
button[role="tab"]{
  background:#f1f5f9; color:#1e293b; font-weight:600;
  padding:6px 12px; border-radius:8px 8px 0 0; margin-right:4px; border:0;
}
button[role="tab"][aria-selected="true"]{ background:#2563eb !important; color:#fff !important; }
div[data-testid="stMetricValue"]{font-size:20px !important; font-weight:700 !important; color:#1e40af !important;}
div[data-testid="stMetricLabel"]{font-size:18px !important; font-weight:700 !important; color:#1e293b !important;}
div.stButton > button:first-child, div.stDownloadButton > button{
  background:#2563eb; color:#fff; border-radius:8px; padding:.5em 1em; font-weight:600;
}
div.stButton > button:first-child:hover, div.stDownloadButton > button:hover{ background:#1d4ed8; color:#fff; }

/* 低調橫向勾選列 */
.inline-checks{ display:flex; flex-wrap:wrap; gap:14px; margin:6px 0 6px 0; }
.inline-checks label{ font-size:13px; color:#334155; cursor:pointer; }
.inline-checks label:hover{ text-decoration: underline; }
.inline-checks input{ transform: scale(1.0); margin-right:6px; }

/* 圓角輸入元件 */
div[data-baseweb="select"] > div, textarea, input[type="text"]{ border-radius:8px; }
</style>
""", unsafe_allow_html=True)

# ----------------------------
# PDF 字型
# ----------------------------
FONT_NAME = "NotoSansTC"
if FONT.exists():
    try:
        pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONT)))
    except Exception:
        st.sidebar.warning("⚠️ 無法載入字型（PDF 仍可生成，但可能無法顯示繁體中文）")
else:
    st.sidebar.info("提示：放入 NotoSansTC-Regular.ttf 以支援 PDF 繁中")

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

# 亮點
c1, c2, c3 = st.columns(3)
c1.metric("快速掌握傳承全貌", "約 7 分鐘")
c2.metric("顧問端效率", "提升 3×")
c3.metric("隱私保護", "本地試算")

st.write("---")
st.subheader("用 AI 先看見，再決定")

# ----------------------------
# Tabs
# ----------------------------
tab1, tab2, tab3 = st.tabs(["遺產稅｜快速估算", "傳承地圖｜需求快照（PDF）", "預約顧問｜一對一諮詢"])

# ============================================================
# Tab1: 遺產稅快速估算
# ============================================================
with tab1:
    st.caption("輸入資產（萬）與家庭狀況，依民法第1138條推算法定繼承人，並計算扣除額與遺產稅（示意用途）。")

    total_wan = st.number_input("總資產（萬）", min_value=0, step=100, value=30000)
    estate = total_wan * 10_000

    st.divider()
    st.markdown("### 請輸入家庭成員")

    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        has_spouse = st.checkbox("是否有配偶（扣除額 553 萬）", value=False)
    with col2:
        children_count = st.number_input("直系血親卑親屬人數（每人 56 萬）", min_value=0, step=1, value=0)
    with col3:
        parents_count = st.number_input("父母人數（每人 138 萬，最多 2 人）", min_value=0, max_value=2, step=1, value=0)

    col4, col5 = st.columns([1,1])
    with col4:
        has_siblings = st.checkbox("是否有兄弟姊妹（無扣除額）", value=False)
    with col5:
        has_grandparents = st.checkbox("祖父母是否健在（無扣除額）", value=False)

    BASE_EXEMPTION_WAN = 1333
    FUNERAL_EXPENSE_WAN = 138
    deduction_wan = BASE_EXEMPTION_WAN + FUNERAL_EXPENSE_WAN
    if has_spouse: deduction_wan += 553
    if children_count > 0: deduction_wan += children_count * 56
    if parents_count > 0: deduction_wan += min(parents_count, 2) * 138
    deductions = deduction_wan * 10_000

    heirs = []
    if children_count > 0: heirs = ["子女"]
    elif parents_count > 0: heirs = ["父母"]
    elif has_siblings: heirs = ["兄弟姊妹"]
    elif has_grandparents: heirs = ["祖父母"]
    if has_spouse: heirs = ["配偶"] + heirs
    heirs_str = "、".join(heirs) if heirs else "（無繼承人 → 遺產歸國庫）"

    st.info(f"👉 法定繼承人（民法1138條示意）：{heirs_str}")
    st.success(f"👉 扣除額合計：約 NT$ {deductions:,.0f}")

    with st.expander("查看扣除額明細", expanded=False):
        st.write(f"- 基本免稅額：1,333 萬")
        st.write(f"- 喪葬費用：138 萬")
        if has_spouse: st.write(f"- 配偶扣除額：553 萬")
        if children_count > 0: st.write(f"- 子女扣除額：{children_count} × 56 萬 = {children_count * 56} 萬")
        if parents_count > 0: st.write(f"- 父母扣除額：{min(parents_count,2)} × 138 萬 = {min(parents_count,2) * 138} 萬")

    shares = {}
    if heirs:
        if "子女" in heirs:
            total_persons = children_count + (1 if has_spouse else 0)
            if total_persons > 0:
                if has_spouse: shares["配偶"] = 1 / total_persons
                if children_count > 0: shares["子女（合計）"] = (total_persons - (1 if has_spouse else 0)) / total_persons
        elif "父母" in heirs:
            shares["配偶"] = 0.5 if has_spouse else 0.0
            shares["父母（合計）"] = 0.5 if has_spouse else 1.0
        elif "兄弟姊妹" in heirs:
            shares["配偶"] = 0.5 if has_spouse else 0.0
            shares["兄弟姊妹（合計）"] = 0.5 if has_spouse else 1.0
        elif "祖父母" in heirs:
            shares["配偶"] = 2/3 if has_spouse else 0.0
            shares["祖父母（合計）"] = 1/3 if has_spouse else 1.0

    if shares:
        st.markdown("### 應繼分（比例示意）")
        for k, v in shares.items():
            if v > 0: st.write(f"- {k}：{v:.2%}")

    BRACKET1 = 56_210_000
    BRACKET2 = 112_420_000
    RATE1, RATE2, RATE3 = 0.10, 0.15, 0.20
    taxable = max(estate - deductions, 0)

    if taxable <= BRACKET1:
        tax = RATE1 * taxable
        bracket_used = f"10% × {taxable:,.0f}"
        part1, part2, part3 = f"10% × {taxable:,.0f} = {tax:,.0f}", None, None
    elif taxable <= BRACKET2:
        tax = RATE1 * BRACKET1 + RATE2 * (taxable - BRACKET1)
        part1 = f"10% × {BRACKET1:,.0f} = {RATE1*BRACKET1:,.0f}"
        part2 = f"15% × ({taxable:,.0f} − {BRACKET1:,.0f}) = {RATE2*(taxable-BRACKET1):,.0f}"
        part3 = None
        bracket_used = "10% / 15%"
    else:
        tax = (RATE1 * BRACKET1 + RATE2 * (BRACKET2 - BRACKET1) + RATE3 * (taxable - BRACKET2))
        part1 = f"10% × {BRACKET1:,.0f} = {RATE1*BRACKET1:,.0f}"
        part2 = f"15% × ({BRACKET2:,.0f} − {BRACKET1:,.0f}) = {RATE2*(BRACKET2-BRACKET1):,.0f}"
        part3 = f"20% × ({taxable:,.0f} − {BRACKET2:,.0f}) = {RATE3*(taxable-BRACKET2):,.0f}"
        bracket_used = "10% / 15% / 20%"

    st.success(f"預估遺產稅額：約 NT$ {tax:,.0f}")
    with st.expander("查看遺產稅計算明細", expanded=False):
        st.write(f"- 輸入總資產：{total_wan:,} 萬 ＝ NT$ {estate:,.0f}")
        st.write(f"- 扣除額合計：{deduction_wan:,} 萬 ＝ NT$ {deductions:,.0f}")
        st.write(f"- 應稅遺產淨額：NT$ {taxable:,.0f}")
        st.write(f"- 套用級距：{bracket_used}")
        st.write("— — —")
        if part1: st.write(part1)
        if part2: st.write(part2)
        if part3: st.write(part3)
        st.write("— — —")
        st.write(f"＝ 預估遺產稅額：NT$ {tax:,.0f}")
    st.caption("＊示意計算，請依最新法規與個案確認。")

# ============================================================
# Tab2: 傳承快照 PDF（每主題：標題 → 低調標籤 → 輸入框）
# ============================================================
with tab2:
    st.caption("勾選幾個關鍵點，補充你的文字，生成傳承快照 PDF。")

    def inline_checks(title:str, options:list[str], key_prefix:str, default:list[str]=None):
        if default is None: default = []
        st.markdown(f"### {title}")
        selected = []
        cols = st.columns(min(6, max(1, len(options))))
        for i, opt in enumerate(options):
            with cols[i % len(cols)]:
                checked = st.checkbox(opt, key=f"{key_prefix}_{i}", value=(opt in default))
                if checked: selected.append(opt)
        st.markdown('<div class="inline-checks"></div>', unsafe_allow_html=True)
        return selected

    # 1) 想優先照顧的人
    who_options = ["配偶", "子女", "父母", "兄弟姊妹", "祖父母", "其他"]
    who_selected = inline_checks("想優先照顧的人（例如：太太／兒女／長輩）", who_options, "who")
    who = st.text_input("（可自行補充）", value="、".join(who_selected), key="who_free")

    st.write("")

    # 2) 主要資產
    assets_options = ["公司股權", "不動產", "金融資產", "保單", "海外資產", "其他"]
    assets_selected = inline_checks("主要資產（可自行補充）", assets_options, "assets")
    assets = st.text_area("（可自行補充）", value="\n".join(assets_selected), height=120, key="assets_free")

    st.write("")

    # 3) 傳承顧慮
    concerns_options = ["稅負過高", "婚前財產隔離", "企業接班", "現金流不足", "遺囑設計", "信託安排"]
    concerns_selected = inline_checks("傳承顧慮（可自行補充）", concerns_options, "concerns")
    concerns = st.text_area("（可自行補充）", value="\n".join(concerns_selected), height=120, key="concerns_free")

    # 生成 PDF
    if st.button("生成傳承快照 PDF"):
        buf = BytesIO()
        c = canvas.Canvas(buf, pagesize=A4)
        w, h = A4
        x_pad, y_top, y_footer = 60, h - 60, 36

        TITLE_FONT = FONT_NAME if FONT.exists() else "Helvetica-Bold"
        BODY_FONT  = FONT_NAME if FONT.exists() else "Helvetica"

        # Logo 三層保險嵌入
        text_y = y_top
        logo_drawn = False
        if LOGO.exists():
            try:
                pil_img = Image.open(str(LOGO)).convert("RGB")
                pil_buf = BytesIO(); pil_img.save(pil_buf, format="PNG"); pil_buf.seek(0)
                c.drawInlineImage(pil_buf, x_pad, y_top - 40, height=40, preserveAspectRatio=True)
                text_y = y_top - 50; logo_drawn = True
            except Exception:
                try:
                    logo_reader = ImageReader(Image.open(str(LOGO)).convert("RGB"))
                    c.drawImage(logo_reader, x_pad, y_top - 40, height=40, preserveAspectRatio=True, mask="auto")
                    text_y = y_top - 50; logo_drawn = True
                except Exception:
                    try:
                        b64 = get_base64_of_file(LOGO)
                        if b64:
                            raw = BytesIO(base64.b64decode(b64))
                            logo_reader = ImageReader(raw)
                            c.drawImage(logo_reader, x_pad, y_top - 40, height=40, preserveAspectRatio=True, mask="auto")
                            text_y = y_top - 50; logo_drawn = True
                    except Exception:
                        pass
        if not logo_drawn:
            c.setLineWidth(0.6); c.rect(x_pad, y_top-28, 80, 24)
            c.setFont("Helvetica", 8); c.drawString(x_pad+6, y_top-20, "LOGO")
            text_y = y_top - 40
            st.warning("⚠️ PDF 無法嵌入 logo.png，已以占位符代替。")

        def line(text, size=12, gap=18, bold=False):
            font = TITLE_FONT if bold else BODY_FONT
            c.setFont(font, size)
            y = line.y
            for seg in (text or "").split("\n"):
                c.drawString(x_pad, y, seg)
                y -= gap
            line.y = y
        line.y = text_y

        c.setTitle("永傳｜傳承快照")
        line("永傳影響力傳承平台｜傳承快照", 16, 24, bold=True)
        line(f"日期：{datetime.now().strftime('%Y-%m-%d %H:%M')}", 11, 18)
        line.y -= 6

        line("想優先照顧的人：", 12, 18, bold=True); line(who or "（尚未填寫）", 12, 18)
        line.y -= 6
        line("主要資產：", 12, 18, bold=True)
        for row in (assets or "（尚未填寫）").split("\n"):
            row = row.strip()
            if row: line(f"• {row}", 11, 16)
        line.y -= 6
        line("傳承顧慮：", 12, 18, bold=True)
        for row in (concerns or "（尚未填寫）").split("\n"):
            row = row.strip()
            if row: line(f"• {row}", 11, 16)

        line.y -= 8
        c.setStrokeColorRGB(0.82, 0.84, 0.88)
        c.setLineWidth(0.6)
        c.line(x_pad, line.y, w - x_pad, line.y)
        line.y -= 14
        line("永傳家族傳承導師", 12, 18, bold=True)
        line("傳承，不只是資產的安排，更是讓關心的人，在需要時真的被照顧到。", 11, 18)

        c.setFont(BODY_FONT, 10)
        c.drawRightString(w - x_pad, y_footer, "© 2025 《影響力》傳承策略平台｜永傳家族辦公室")

        c.showPage(); c.save()
        st.download_button("下載傳承快照 PDF", data=buf.getvalue(),
                           file_name="永傳_傳承快照.pdf", mime="application/pdf")
        st.success("已生成 PDF（含 Logo、分隔線與暖心收尾）。")

# ============================================================
# Tab3: 預約顧問
# ============================================================
with tab3:
    st.caption("7 分鐘工具體驗後，預約深入討論更有感")
    name = st.text_input("您的稱呼")
    email = st.text_input("Email")
    phone = st.text_input("聯絡電話")
    note = st.text_area("想優先解決的問題（自由輸入）", height=120)
    if st.button("送出預約需求"):
        st.success("我們已收到您的預約需求。工作日內會與您聯繫，安排 20–30 分鐘初談。")

# ----------------------------
# Footer
# ----------------------------
st.write("---")
left, right = st.columns([2,1])
with left:
    st.markdown("""
**永傳家族傳承導師**  
傳承，不只是資產的安排，更是讓關心的人，在需要時真的被照顧到。
""")
with right:
    st.markdown("""
**聯絡**
- 官網：gracefo.com  
- 信箱：123@gracefo.com  
- LINE／QR：請置入圖片（images/line_qr.png）
""")
st.caption(f"© {datetime.now().year} 《影響力》傳承策略平台｜永傳家族辦公室")
