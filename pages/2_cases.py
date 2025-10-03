import streamlit as st
# Anchor for CTA jump
st.markdown('<a id="booking"></a>', unsafe_allow_html=True)
# ---- Topbar (welcome + CTA) ----
_user_name = "Grace"
_user_expiry = "2026-12-31"
st.markdown(f"""
<div class="topbar">
  <div class="left">👋 歡迎回來，<b>{_user_name}</b>（到期日：{_user_expiry}）</div>
  <div class="right">
    <a href="#booking">預約 30 分鐘傳承健檢</a>
  </div>
</div>
""", unsafe_allow_html=True)
# ---- Global brand style & cleanup ----
st.markdown("""
<style>
/* Hide Sidebar & its toggle */
[data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="collapsedControl"] {
  display: none !important;
}
/* Hide default header buttons */
.stAppDeployButton, button[kind="header"], [data-testid="BaseButton-header"] {
  display: none !important;
}
:root {
  --brand:#145DA0; --accent:#2E8BC0; --gold:#F9A826; --bg:#F7FAFC; --ink:#1A202C;
}
html, body, .stApp { background: var(--bg); color: var(--ink); }
.topbar {
  display:flex; align-items:center; justify-content:space-between;
  padding:10px 16px; margin-bottom:8px; border-bottom:1px solid #E2E8F0; background:#fff; border-radius:12px;
}
.topbar .right a { margin-left:8px; text-decoration:none; padding:10px 16px; border-radius:999px; background:var(--brand); color:#fff; }
.topbar .right a:hover { background:#0F4D88; }
.section-card { background:#fff; border:1px solid #E2E8F0; border-radius:16px; padding:20px; }
.footer { color:#4A5568; font-size:14px; margin-top:40px; }
</style>
""", unsafe_allow_html=True)

# 頁面設定
st.set_page_config(
    page_title="《影響力》｜傳承案例分享",
    page_icon="📚",
    layout="centered"
)

# 標題與副標（置中）
st.markdown("""
<div style='text-align: center;'>
    <h1 style='font-size: 36px;'>📚《影響力》傳承案例分享</h1>
    <p style='font-size: 18px; color: gray;'>從真實故事，看見更多選擇的可能</p>
</div>
""", unsafe_allow_html=True)

# 內容開始
st.markdown("""
這裡集結了不同家庭的傳承故事，  
有些是企業主的思索，有些是高齡長輩的轉念，  
也有些，是家人之間終於開始的那場對話。

每一則案例，都是《影響力》陪伴過程中真實發生的片段，  
我們已去識別化處理，只保留當事人面對選擇時的思緒與智慧。

---

### 👨‍👩‍👧‍👦 案例一：孩子不接班，公司怎麼辦？

一位創辦人經營公司數十年，卻發現兩位子女都對家業沒興趣：  
一位喜歡藝術，另一位想做自己的事。

他說：「我不做了，這公司還能留下來嗎？」  
最後，他找到信任的專業經理人協助經營，  
並用保險與信託安排股權，照顧家人的未來生活。

> 「即使孩子不接班，我也希望這家公司能活下去，  
>  更希望家人之間不會因為錢而傷感情。」

---

### 👵 案例二：年紀大了，才發現自己什麼都沒有

這位八十多歲的女創辦人，一生奉獻給事業，卻忽略了自己。  
所有資產都綁在公司名下，醫療與生活費從未規劃。

直到健康亮起紅燈，她才正視自己的未來。  
透過高現金值保單與信託安排，她為自己建立了退休金與醫療保障。

> 她說：「終於可以安心養老，不靠孩子，也不怕沒人照顧我了。」

---

### 💰 案例三：沒有稅源，怎麼傳承？

一位企業主驟逝後，家人準備繼承資產時，才發現無法繳清遺產稅。  
現金不夠、帳戶被凍結、公司股權卡住，整個家庭陷入混亂。

後來他們才知道：早幾年用保險或信託預留稅源，  
就能避免這些衝擊。

> 這個故事提醒我們：  
> 「傳承不是只看資產總額，更要考慮稅金與現金流。」

---

### 🏠 案例四：爸爸不說，孩子不問，誤解悄悄累積

這個家庭的父親是公司創辦人，對未來想法很多，卻從不開口。  
孩子們也不敢問，怕觸動敏感議題。

直到一次家族聚會，小孩無意提起傳承話題，才發現彼此想法天差地遠。  
後來在顧問協助下，他們終於開啟對話、釐清誤解，也建立了家族溝通的橋樑。

> 「其實我一直很在意孩子怎麼想，  
> 就是不知道怎麼說出口。」

---

### 📝 案例五：一句「我只是想說說我的故事」

一位長輩在設計傳承時說：「我想留下的不只是錢，而是我的故事。」

他寫下創業歷程，請孫子幫忙錄音、剪輯成影片，  
做成一本家族故事專輯，送給每一位家人。

> 「我知道我不會永遠在，  
>  但我希望他們永遠記得我是誰。」

---

💌 如果您也願意分享自己的經歷（可匿名），我們非常歡迎來信。  
📧 <a href="mailto:123@gracefo.com">123@gracefo.com</a>

---

# --- 聯絡資訊 ---
st.markdown("---")
st.markdown("""
<div style='display: flex; justify-content: center; align-items: center; gap: 1.5em; font-size: 14px; color: gray;'>
  <!-- 根路徑“/”會帶回到 app.py -->
  <a href='/' style='color:#006666; text-decoration: underline;'>《影響力》傳承策略平台</a>
  <a href='https://gracefo.com' target='_blank'>永傳家族辦公室</a>
  <a href='mailto:123@gracefo.com'>123@gracefo.com</a>
</div>
""", unsafe_allow_html=True)
