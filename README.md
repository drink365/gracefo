
# 《影響力》傳承策略平台 — 模組化重構樣板

**重點：**
- 功能模組化：`src/modules/*`
- 計算服務分層：`src/services/*`
- 介面元件集中：`src/ui/components.py`
- 登入＋效期提示：`src/utils/auth.py`
- 隱藏 Streamlit 預設按鈕維持品牌一致

## 使用
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 你可直接調整：
- `src/config.py`：品牌、授權名單、App 參數
- `src/modules/*.py`：各模組頁面
- `src/services/*.py`：核心計算
- `src/ui/components.py`：Topbar / Footer / CSS

> 範例計算為示意，實務請以最新法規與精算假設更新。
