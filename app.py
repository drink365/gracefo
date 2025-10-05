import streamlit as st
from pathlib import Path as _Path
_fav = _Path(__file__).parent / "favicon.png"
if _fav.exists():
    st.set_page_config(page_title="永傳家族傳承導師｜影響力傳承平台", page_icon=str(_fav), layout="wide")
else:
    st.set_page_config(page_title="永傳家族傳承導師｜影響力傳承平台", page_icon="✨", layout="wide")

# ==== HOME: Hero + Values + Roles + Tools + Success + CTA ====
st.markdown('''
<div class="hero">
  <h1>面向監管與市場週期的家族治理解決方案</h1>
  <p>以合規為底、以現金流為骨、以家族共識為核心，為企業家打造可預期的交棒路徑。</p>
  <p style="margin: 16px 0;">
    <a class="cta" href="#booking">預約健檢</a>
    <span style="margin-left:12px;">
      <a class="tool-link" href="/?download=governance-checklist">索取治理清單 →</a>
    </span>
  </p>
  <div class="note">線上或現場皆可｜守秘合規</div>
</div>
''', unsafe_allow_html=True)

# --- 三大價值 ---
st.markdown('<div class="section-title">我們的三大價值</div>', unsafe_allow_html=True)
v1, v2, v3 = st.columns(3)
with v1:
    st.markdown('<div class="card"><h3>專業</h3><p>跨境法稅 × 保單 × 信託整合，由美國 CPA 與實務團隊把關。</p></div>', unsafe_allow_html=True)
with v2:
    st.markdown('<div class="card"><h3>智能</h3><p>AI 傳承導師｜工具箱，將模糊問題變成可決策的選項。</p></div>', unsafe_allow_html=True)
with v3:
    st.markdown('<div class="card"><h3>永續</h3><p>為家業、家產、家風設計長期穩定現金流與治理機制。</p></div>', unsafe_allow_html=True)

# --- 你是誰（角色導向） ---
st.markdown('<div class="section-title">你是誰？我們怎麼幫你</div>', unsafe_allow_html=True)
r1, r2 = st.columns(2)
with r1:
    st.markdown('''
<div class="card">
  <h3>創辦人一代<span class="badge">交棒設計</span></h3>
  <p>稅負可預期、交棒有秩序、關鍵資產不外流。</p>
  <p><a class="cta" href="#booking">談談您的情況</a></p>
</div>
''' , unsafe_allow_html=True)
with r2:
    st.markdown('''
<div class="card">
  <h3>二代接班<span class="badge">治理升級</span></h3>
  <p>權責清楚、分配公平、治理不失速。</p>
  <p><a class="cta" href="#booking">預約顧問</a></p>
</div>
''' , unsafe_allow_html=True)

r3, r4 = st.columns(2)
with r3:
    st.markdown('''
<div class="card">
  <h3>跨境資產<span class="badge">合規路徑</span></h3>
  <p>稅務合規、文件齊備、傳承路徑清楚。</p>
  <p><a class="cta" href="#booking">了解作法</a></p>
</div>
''' , unsafe_allow_html=True)
with r4:
    st.markdown('''
<div class="card">
  <h3>長輩照顧<span class="badge">保障安排</span></h3>
  <p>照護資金有安排、分期給付、避免爭產。</p>
  <p><a class="cta" href="#booking">開始規劃</a></p>
</div>
''' , unsafe_allow_html=True)

# --- 工具箱 ---
st.markdown('<div class="section-title">工具箱（立即可用）</div>', unsafe_allow_html=True)
g1, g2 = st.columns(2)
with g1:
    st.markdown('''
<div class="card">
  <h3>📦 保單策略規劃</h3>
  <p>用 20% 的保費守護 100% 的資產。</p>
  <p><a class="cta tool-link" href="/?tool=policy">立即試用</a>　<a class="tool-link" href="#booking">諮詢顧問 →</a></p>
</div>
''' , unsafe_allow_html=True)
with g2:
    st.markdown('''
<div class="card">
  <h3>⚖️ 遺產稅秒算</h3>
  <p>快速試算、看見差額，做出好決策。</p>
  <p><a class="cta tool-link" href="/?tool=estate">立即試算</a>　<a class="tool-link" href="#booking">諮詢顧問 →</a></p>
</div>
''' , unsafe_allow_html=True)

g3, g4 = st.columns(2)
with g3:
    st.markdown('''
<div class="card">
  <h3>🗺️ 傳承地圖</h3>
  <p>資產六大類 × 風險雷達，一張圖看全局。</p>
  <p><a class="cta tool-link" href="/?tool=map">開始製作</a>　<a class="tool-link" href="#booking">諮詢顧問 →</a></p>
</div>
''' , unsafe_allow_html=True)
with g4:
    st.markdown('''
<div class="card">
  <h3>💬 顧問對話庫</h3>
  <p>讓家族對話更順暢。</p>
  <p><a class="cta tool-link" href="/?tool=dialog">看看範例</a>　<a class="tool-link" href="#booking">諮詢顧問 →</a></p>
</div>
''' , unsafe_allow_html=True)

# --- 成功案例（結果導向） ---
st.markdown('<div class="section-title">成功案例（結果導向）</div>', unsafe_allow_html=True)
c1, c2 = st.columns(2)
with c1:
    st.markdown('''
<div class="card">
  <h3>90 歲長輩 5 億保額傳承</h3>
  <p>壓縮贈與、指定第三代、婚前財產隔離。</p>
  <p><a class="tool-link" href="#booking">閱讀重點 →</a></p>
</div>
''' , unsafe_allow_html=True)
with c2:
    st.markdown('''
<div class="card">
  <h3>製造業二代交棒</h3>
  <p>股權信託 + 保單現金流，兼顧治理與流動性。</p>
  <p><a class="tool-link" href="#booking">閱讀重點 →</a></p>
</div>
''' , unsafe_allow_html=True)

# --- 底部 CTA ---
st.markdown('''
<div class="section-card">
  <h3>預約 30 分鐘傳承健檢（免費）</h3>
  <p>已協助超過 <b>XXX</b> 位企業家完成跨境傳承規劃（勞動部／產投授課講師）。</p>
  <a class="cta" href="#booking">立即預約</a>
</div>
''' , unsafe_allow_html=True)
# ==== END HOME ====
import streamlit as st
import base64

# 設定頁面
st.set_page_config(
    page_title="《影響力》 | 高資產家庭的傳承策略入口",
    page_icon="🌿",
    layout="centered"
)

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
