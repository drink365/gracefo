# 永傳影響力傳承平台（Streamlit｜統合＋安全版｜含真實品牌素材）

整合內容：
- ✅ 真實品牌素材：`logo.png`、`logo2.png`（favicon）、`NotoSansTC-Regular.ttf`
- ✅ 產生 PDF（優先用繁中 NotoSansTC，失敗自動退回 Helvetica）
- ✅ 表單寫入 Google Sheets（啟用 Secrets 後）
- ✅ SendGrid Email 通知（啟用 Secrets 後）
- ✅ 圖片壞檔／缺檔不會當機

## 本機執行
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 部署到 Streamlit Cloud
1. 建 GitHub Repo，上傳本專案檔案。
2. share.streamlit.io → **New app** → 指向 `app.py` → Deploy。

## 啟用整合（Secrets, TOML）
```toml
SHEET_ID = "你的_SHEET_ID"
NOTIFY_EMAIL = "你要收通知的信箱（也作為寄件者）"

[gcp_service_account]
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "-----BEGIN PRIVATE KEY-----\nXXX\n-----END PRIVATE KEY-----\n"
client_email = "your-sa@project.iam.gserviceaccount.com"
client_id = "xxx"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/your-sa%40project.iam.gserviceaccount.com"

# 若要啟用 Email 通知
SENDGRID_API_KEY = "你的_API_KEY"
```
