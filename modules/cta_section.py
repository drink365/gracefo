# modules/cta_section.py — 全站 CTA（導向預約頁＋mailto 備援）
import streamlit as st

def render_cta():
    st.markdown("---")
    st.markdown("### 🌿 為未來畫出藍圖，現在就是最好的時機。")
    st.markdown(
        """
        每一次認真思考未來，都是為家人創造安心的開始。  
        若您希望我們陪您進一步釐清資產、保障與家族規劃方向，  
        歡迎預約 1 對 1 對談，從今天開始為家族建立更確定的未來。

        👉 **[預約 1 對 1 規劃](/4_contact)**　｜　📬 <a href="mailto:123@gracefo.com?subject=我想預約退休與傳承規劃諮詢&body=您好，我剛完成了永傳《影響力》傳承規劃平台的體驗，希望預約進一步諮詢...">寄信預約</a>
        """,
        unsafe_allow_html=True,
    )
