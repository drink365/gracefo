import streamlit as st
from datetime import datetime
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path
import base64

# ----------------------------
# 檔案路徑
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

# CSS 樣式
st.markdown("""
<style>
button[role="tab"]{
    background:#f1f5f9; color:#1e293b; font-weight:600;
    padding:6px 12px; border-radius:8px 8px 0 0; margin-right:4px;
    border:0;
}
button[role="tab"][aria-selected="true"]{
    background:#2563eb !important; color:#fff !important;
}
div[data-testid="stMetricValue"]{
    font-size:20px !important; font-weight:700 !important; color:#1e40af !important;
}
div[data-testid="stMetricLabel"]{
    font-size:18px !important; font-weight:700 !important; color:#1e293b !important;
}
div.stButton > button:first-child,
div.stDownloadButton > button{
    background:#2563eb; color:#fff; border-radius:8px; padding:.5em 1em; font-weight:600;
}
div.stButton > button:first-child:hover,
div.stDownloadButton > button:hover{
    background:#1d4ed8; color:#fff;
}
div[data-baseweb="select"] > div{ border-radius:8px; }
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
        st.sidebar.warning("⚠️ 無法載入字型")
else:
    st.sidebar.info("提示：放入 NotoSansTC-Regular.ttf 以支援 PDF 繁中")

# ----------------------------
# 頂部框
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
      <h2 style="margin:12px 0 8px 0;font-size:22px;line-height:1.3;
                 color:#1e3a8a;font-weight:700">
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

# 亮點區
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
    st.caption("輸入資產（萬）與家庭狀況，系統依民法第1138條推算法定繼承人，並計算扣除額與遺產稅。")

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

    # ✅ 扣除額：含基本免稅額 1333 萬
    BASE_EXEMPTION_WAN = 1333
    deduction_wan = BASE_EXEMPTION_WAN
    if has_spouse:
        deduction_wan += 553
    if children_count > 0:
        deduction_wan += children_count * 56
    if parents_count > 0:
        deduction_wan += min(parents_count, 2) * 138
    deductions = deduction_wan * 10_000

    # 法定繼承人
    heirs = []
    if children_count > 0:
        heirs = ["子女"]
    elif parents_count > 0:
        heirs = ["父母"]
    elif has_siblings:
        heirs = ["兄弟姊妹"]
    elif has_grandparents:
        heirs = ["祖父母"]
    if has_spouse:
        heirs = ["配偶"] + heirs

    heirs_str = "、".join(heirs) if heirs else "（無繼承人 → 遺產歸國庫）"

    st.info(f"👉 法定繼承人（民法1138條示意）：{heirs_str}")
    st.success(f"👉 扣除額合計（含基本免稅額 1,333 萬）：約 NT$ {deductions:,.0f}")

    # 稅額試算
    taxable = max(estate - deductions, 0)
    if taxable <= 50_000_000:
        tax = taxable * 0.10
    elif taxable <= 100_000_000:
        tax = 5_000_000 + (taxable - 50_000_000) * 0.15
    else:
        tax = 12_500_000 + (taxable - 100_000_000) * 0.20

    st.success(f"預估遺產稅額：約 NT$ {tax:,.0f}")
    st.caption("＊示意計算，請依最新法規與個案確認。")

# ============================================================
# Tab2: 傳承快照 PDF
# ============================================================
with tab2:
    st.caption("快速點選＋輸入，生成傳承快照 PDF（供內部討論用）")

    assets_options = ["公司股權", "不動產", "金融資產", "保單", "海外資產", "其他"]
    assets_selected = st.multiselect("主要資產（可點選快速加入）", assets_options, default=[])

    concerns_options = ["稅負過高", "婚前財產隔離", "企業接班", "現金流不足", "遺囑設計", "信託安排"]
    concerns_selected = st.multiselect("傳承顧慮（可點選快速加入）", concerns_options, default=[])

    with st.form("legacy_form"):
        who = st.text_input("想優先照顧的人")
        assets = st.text_area("主要資產", value="\n".join(assets_selected), height=120)
        concerns = st.text_area("傳承顧慮", value="\n".join(concerns_selected), height=120)
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
        line("想優先照顧的人：", 12, 18, bold=True); line(who or "（未填）", 12, 18)
        line("主要資產：", 12, 18, bold=True)
        for row in (assets or "（未填）").split("\n"):
            line(f"• {row}", 11, 16)
        line("傳承顧慮：", 12, 18, bold=True)
        for row in (concerns or "（未填）").split("\n"):
            line(f"• {row}", 11, 16)

        c.showPage(); c.save()
        st.download_button("下載 PDF", data=buf.getvalue(),
                           file_name="永傳_傳承快照.pdf", mime="application/pdf")

# ============================================================
# Tab3: 預約顧問
# ============================================================
with tab3:
    st.caption("體驗後，若想深入討論可預約顧問")

    needs_options = ["稅負規劃", "現金流安排", "保單傳承", "跨境資產", "企業接班"]
    needs_selected = st.multiselect("常見需求（可快速選擇）", needs_options, default=[])

    with st.form("booking_form"):
        name = st.text_input("您的稱呼")
        email = st.text_input("Email")
        phone = st.text_input("聯絡電話")
        note = st.text_area("想優先解決的問題", value="\n".join(needs_selected), height=120)
        ok = st.form_submit_button("送出預約需求")
    if ok:
        st.success("我們已收到您的需求，將於工作日內與您聯繫。")

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
- LINE／QR：請置入圖片
""")
st.caption(f"© {datetime.now().year} 《影響力》傳承策略平台｜永傳家族辦公室")
