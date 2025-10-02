# 永傳影響力傳承平台（Streamlit｜統合版）

- ✅ 品牌：logo（logo.png）、favicon（logo2.png）、PDF 繁中（NotoSansTC-Regular.ttf）
- ✅ Google Sheets 收件、SendGrid Email 通知（透過 secrets 啟用）
- ✅ 傳承快照 PDF、預約表單

## 使用
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 部署（GitHub → Streamlit Cloud）
上傳到 GitHub → share.streamlit.io → New app → 指向 `app.py`。

## Secrets（TOML）
```toml
SHEET_ID = "你的_SHEET_ID"
NOTIFY_EMAIL = "收通知的信箱"

[gcp_service_account]
type = "service_account"
project_id = "..."
private_key_id = "..."
private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
client_email = "your-sa@project.iam.gserviceaccount.com"
client_id = "..."
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/your-sa%40project.iam.gserviceaccount.com"

SENDGRID_API_KEY = "你的_API_KEY"
```
