import streamlit as st
# ---- Force-hide Sidebar & header buttons ----
st.markdown("""
<style>
/* Sidebar & its toggle */
[data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="collapsedControl"] { display: none !important; }
/* Header default buttons (Deploy/Settings/Rerun) */
.stAppDeployButton, button[kind="header"], [data-testid="BaseButton-header"], [data-testid="stToolbar"] { display: none !important; }
/* Ensure main stretches wide */
[data-testid="stAppViewContainer"] .main .block-container {
  max-width: 1600px; padding-left: 24px; padding-right: 24px;
}
</style>
""", unsafe_allow_html=True)
# --- Page config: apply favicon.png if available (must be first Streamlit call) ---
from pathlib import Path as _Path
_fav = _Path(__file__).parent / "favicon.png"
if _fav.exists():
    st.set_page_config(page_title="永傳家族傳承導師｜影響力傳承平台", page_icon=str(_fav), layout="wide")
else:
    st.set_page_config(page_title="永傳家族傳承導師｜影響力傳承平台", page_icon="✨", layout="wide")
import base64

# 設定頁面
# 讀取 logo
def load_logo_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

try:
    logo_base64 = load_logo_base64("logo.png")
    st.markdown(f"""
    <div style='text-align: center;'>
        <img src='data:image/png;base64,{logo_base64}' width='200'><br>
    </div>
    """, unsafe_allow_html=True)
except:
    st.warning("⚠️ 無法載入 logo.png，請確認檔案存在")

# --- 品牌標語區 ---
st.markdown("""
<div style='text-align: center; margin-top: 2em;'>
    <h1 style='font-size: 36px; font-weight: bold;'>《影響力》</h1>
    <p style='font-size: 24px; color: #333; font-weight: bold; letter-spacing: 0.5px;'>
        高資產家庭的 <span style="color:#006666;">傳承策略平台</span>
    </p>
    <p style='font-size: 18px; color: #888; margin-top: -10px;'>
        讓每一分資源，都成為你影響力的延伸
    </p>
</div>
""", unsafe_allow_html=True)

# --- 品牌開場語 ---
st.markdown("""
<div style='text-align: center; margin-top: 3em; font-size: 18px; line-height: 1.8;'>
    《影響力》是一個專為高資產家庭打造的傳承策略平台。<br>
    我們陪你設計每一分資源的去向，<br>
    讓它能守護最重要的人，延續你真正的價值。
</div>
""", unsafe_allow_html=True)

# --- 三大價值主張 ---
st.markdown("""
<div style='display: flex; justify-content: center; gap: 40px; margin-top: 3em; flex-wrap: wrap;'>
    <div style='width: 280px; text-align: center;'>
        <h3>🏛️ 富足結構</h3>
        <p>為資產設計流動性與穩定性，讓財富更有效率地守護人生階段。</p>
    </div>
    <div style='width: 280px; text-align: center;'>
        <h3>🛡️ 風險預備</h3>
        <p>從保單、稅源到信託制度，設計資產的防禦系統與轉移機制。</p>
    </div>
    <div style='width: 280px; text-align: center;'>
        <h3>🌱 價值傳遞</h3>
        <p>不只是金錢，更是精神、信任與選擇，成就跨世代的連結。</p>
    </div>
</div>
""", unsafe_allow_html=True)

# --- 使用者分流 ---
st.markdown("---")
st.markdown("### 🧭 請選擇您的身份：")

col1, col2 = st.columns(2)
with col1:
    if st.button("🙋 我是客戶", use_container_width=True):
        st.switch_page("pages/client_home.py")
with col2:
    if st.button("🧑‍💼 我是顧問", use_container_width=True):
        st.switch_page("pages/advisor_home.py")

# --- 聯絡資訊 ---
st.markdown("---")
st.markdown(
    """
    <div style='display: flex; justify-content: center; align-items: center; gap: 1.5em; font-size: 14px; color: gray;'>
      <a href='?' style='color:#006666; text-decoration: underline;'>《影響力》傳承策略平台</a>
      <a href='https://gracefo.com' target='_blank'>永傳家族辦公室</a>
      <a href='mailto:123@gracefo.com'>123@gracefo.com</a>
    </div>
    """,
    unsafe_allow_html=True
)


# ---- Optional Slack Webhook notify ----
def _slack_notify(text: str) -> tuple[bool, str]:
    try:
        cfg = st.secrets.get("slack", {})
        url = cfg.get("webhook")
        if not url:
            return False, "未設定 slack.webhook"
        try:
            import requests
        except Exception:
            return False, "缺少 requests 套件"
        resp = requests.post(url, json={"text": text}, timeout=10)
        if 200 <= resp.status_code < 300:
            return True, "Slack OK"
        return False, f"Slack {resp.status_code}: {resp.text[:200]}"
    except Exception as e:
        return False, f"Slack 錯誤：{e}"
