
import streamlit as st
from datetime import datetime
from modules.pdf_generator import make_simple_pdf

st.set_page_config(page_title="🧭 傳承風險檢測", page_icon="🧭", layout="centered")

st.title("🧭 傳承風險 6 題檢測")
st.caption("結果為教育性初評，非稅務或投資建議；需由顧問複核。")

with st.form("risk6"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.selectbox("您的年齡區間", ["50以下", "50-60", "60-70", "70以上"])
        cross = st.selectbox("家族是否涉及跨國資產/居住", ["否", "是"])
        real_estate_ratio = st.selectbox("不動產占整體資產比重", ["低於30%", "30%-60%", "60%以上"])
    with col2:
        heirs = st.selectbox("潛在繼承人數（含配偶/子女）", ["1人", "2-3人", "4人以上"])
        will = st.selectbox("是否已有遺囑/信託/受益人指定", ["尚未", "部分有", "規劃完整"])
        liquidity = st.selectbox("是否有可支應稅捐/債務的流動資金", ["不足", "勉強足夠", "充足"])

    note = st.text_area("想補充的情況（選填）", height=80)
    ok = st.form_submit_button("查看檢測結果")

if ok:
    score = 0
    score += {"50以下":0, "50-60":1, "60-70":2, "70以上":3}[age]
    score += {"否":0, "是":2}[cross]
    score += {"低於30%":0, "30%-60%":1, "60%以上":2}[real_estate_ratio]
    score += {"1人":0, "2-3人":1, "4人以上":2}[heirs]
    score += {"規劃完整":0, "部分有":1, "尚未":2}[will]
    score += {"充足":0, "勉強足夠":1, "不足":2}[liquidity]

    if score <= 2:
        level = "A（風險低）"
        advice = "目前整體風險偏低，建議每年檢視一次，重點在文件與受益人是否更新。"
    elif score <= 6:
        level = "B（中度風險）"
        advice = "建議進行「傳承地圖」設計，完善受益人/遺囑/信託與保單配置。"
    else:
        level = "C（高風險）"
        advice = "優先處理現金流與稅源準備，並規劃保單/信託以確保交棒秩序。"

    st.success(f"檢測結果：{level}")
    st.write("建議：", advice)
    st.divider()

    st.subheader("下載初步建議報告（PDF）")
    pdf_bytes = make_simple_pdf(
        title="傳承風險初步建議",
        fields={
            "年齡區間": age,
            "跨國因素": cross,
            "不動產占比": real_estate_ratio,
            "潛在繼承人數": heirs,
            "是否有遺囑/信託": will,
            "流動資金": liquidity,
            "檢測等級": level,
            "系統建議": advice,
            "備註": note or "-"
        }
    )
    st.download_button("📄 下載 PDF 報告", data=pdf_bytes, file_name=f"legacy_risk_{datetime.now().date()}.pdf", mime="application/pdf")

    st.info("想更具體了解您的方案？請返回首頁預約顧問或與我們聯繫：hello@gracefo.com")
