# 永傳影響力傳承平台（Streamlit｜Safe Branding 版）

這個版本：logo 壞檔／缺檔不會讓 App 當機；favicon 缺檔時自動退回；PDF 若無字型檔會自動退回 Helvetica。

## 使用
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 部署（GitHub → Streamlit Cloud）
上傳到 GitHub → share.streamlit.io → New app → 指向 `app.py`。

## 小提醒
將 `logo.png`、`logo2.png`、`NotoSansTC-Regular.ttf` 放在根目錄以啟用品牌與繁中字型。
