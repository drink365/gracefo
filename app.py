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

# === 全域 CSS（Tabs / Metrics / Buttons / Tag-like multiselect） ===
st.markdown("""
<style>
/* Tabs 樣式（選中有底色） */
div[data-baseweb="tab-list"] { gap: 4px; }
div[data-baseweb="tab"] {
    background: #f1f5f9;
    padding: 6px 12px;
    border-radius: 8px 8px 0 0;
    color: #1e293b;
    font-weight: 600;
}
div[data-baseweb="tab"][aria-selected="true"] {
    background: #2563eb !important;
    color: white !important;
}

/* 亮點數字與標籤 */
div[data-testid="stMetricValue"] {
    font-size: 20px !important;
    font-weight: 700 !important;
    color: #1e40af !important;
}
div[data-testid="stMetricLabel"] {
    font-size: 18px !important;
    font-weight: 700 !important;
    color: #1e293b !important;
}

/* 主要按鈕底色 */
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

/* multiselect 更像低調的 tag 區（不搶視覺） */
div[data-baseweb="select"] > div { 
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# === PDF 繁中字型 ===
FONT_NAME = "NotoSansTC"
if FONT.exists():
    try:
        pdfmetrics.registerFont(TTFont(FONT_NAME, str(FONT)))
    except Exception:
        st.sidebar.warning("⚠️ 無法載入字型（PDF 仍可生成，但可能無法顯示繁體中文）")
else:
    st.sidebar.info("提示：放入 NotoSansTC-Regular.ttf 以在 PDF 正確顯示繁體中文。")

# === 頂部框（中央 logo 以 Base64 嵌入；標題同一行顯示） ===
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

# === 亮點區 ===
c1, c2, c3 = st.columns(3)
c1.metric("快速掌握傳承全貌", "約 7 分鐘")
c2.metric("顧問端效率", "提升 3×")
c3.metric("隱私保護", "本地試算")

st.write("---")
st.subheader("用 AI 先看見，再決定")

# === Tabs ===
tab1, tab2, tab3 = st.tabs(["遺產稅｜快速估算", "傳承地圖｜需求快照（PDF）", "預約顧問｜一對一諮詢"])

# ----------------------------
# Tab1: 遺產稅快速估算（家庭狀況更精準）
# ----------------------------
with tab1:
    st.caption("輸入大致資產並依家庭狀況計算扣除額與預估稅額（示意用途，實務請由專業人員確認）")

    estate = st.number_input("估算總資產（TWD）", min_value=0, step=1_000_000, value=120_000_000)

    col1, col2, col3 = st.columns(3)
    with col1:
        has_spouse = st.radio("有無配偶", ["有", "無"], index=0, horizontal=True)
    with col2:
        children = st.number_input("子女人數", min_value=0, value=0, step=1)
    with col3:
        has_parents = st.radio("父母健在", ["是", "否"], index=1, horizontal=True)

    # 扣除額（簡化示意）：基本免稅額 + 配偶扣除 + 子女扣除 + 父母扣除
    deductions = 12_000_000  # 基本免稅額（示意）
    if has_spouse == "有":
        deductions += 4_000_000            # 配偶扣除（示意）
    if children > 0:
        deductions += children * 2_000_000 # 每名子女（示意）
    if has_parents == "是":
        deductions += 4_000_000            # 父母扣除（示意）

    # 法定繼承人（民法無遺囑時之簡化邏輯）
    heirs = []
    if children > 0:
        heirs.append("子女")
        if has_spouse == "有":
            heirs.insert(0, "配偶")
    elif has_parents == "是":
        heirs.append("父母")
        if has_spouse == "有":
            heirs.insert(0, "配偶")
    else:
        heirs.append("兄弟姊妹")
        if has_spouse == "有":
            heirs.insert(0, "配偶")
    heirs_str = "、".join(heirs)

    st.info(f"👉 法定繼承人（簡化示意）：{heirs_str}")
    st.success(f"👉 估計可適用扣除額：約 NT$ {deductions:,.0f}")

    # 稅額（示意級距）
    taxable = max(estate - deductions, 0)
    if taxable <= 50_000_000:
        tax = taxable * 0.10
    elif taxable <= 100_000_000:
        tax = 5_000_000 + (taxable - 50_000_000) * 0.15
    else:
        tax = 12_500_000 + (taxable - 100_000_000) * 0.20

    st.success(f"預估遺產稅額：約 NT$ {tax:,.0f}")
    st.caption("＊本工具為教育示意，實務仍須依個案詳算與法規更新調整。")

# ----------------------------
# Tab2: 傳承快照 PDF（快選字在輸入框正上方，低調不搶視覺）
# ----------------------------
with tab2:
    st.caption("快速點選＋輸入，生成傳承快照 PDF（供內部討論用）")

    # 快選：主要資產（輸入框正上方）
    assets_options = ["公司股權", "不動產", "金融資產", "保單", "海外資產", "其他"]
    assets_selected = st.multiselect("主要資產（可點選快速加入）", assets_options, default=[], placeholder="選擇一到多項…")

    # 快選：傳承顧慮（輸入框正上方）
    concerns_options = ["稅負過高", "婚前財產隔離", "企業接班", "現金流不足", "遺囑設計", "信託安排"]
    concerns_selected = st.multiselect("傳承顧慮（可點選快速加入）", concerns_options, default=[], placeholder="選擇一到多項…")

    # 表單
    with st.form("legacy_form"):
        who = st.text_input("想優先照顧的人（例如：太太／兒女／長輩）")
        # 將快選合併成預填內容，使用者仍可任意加字/改行
        assets_text = "\n".join(assets_selected)
        concerns_text = "\n".join(concerns_selected)
        assets = st.text_area("主要資產（可自行補充）", value=assets_text, height=120)
        concerns = st.text_area("傳承顧慮（可自行補充）", value=concerns_text, height=120)
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

        st.download_button("下載 PDF", data=buf.getvalue(),
                           file_name="永傳_傳承快照.pdf", mime="application/pdf")
        st.success("已生成 PDF，可作為與導師討論的起點。")

# ----------------------------
# Tab3: 預約顧問（一樣把快選字放在輸入框上方＋同風格）
# ----------------------------
with tab3:
    st.caption("7 分鐘工具體驗後，預約深入討論更有感")

    needs_options = ["稅負規劃", "現金流安排", "保單傳承", "跨境資產", "企業接班"]
    needs_selected = st.multiselect("常見需求（可點選快速加入）", needs_options, default=[], placeholder="選擇一到多項…")

    with st.form("booking_form"):
        name = st.text_input("您的稱呼")
        email = st.text_input("Email")
        phone = st.text_input("聯絡電話")
        note_prefill = "\n".join(needs_selected)
        note = st.text_area("想優先解決的問題（可自行補充）", value=note_prefill, height=120)
        ok = st.form_submit_button("送出預約需求")
    if ok:
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
