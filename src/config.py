
from dataclasses import dataclass
from datetime import date
from pathlib import Path

APP_TITLE = "《影響力》傳承策略平台"
APP_ICON = "📦"
APP_LAYOUT = "wide"

AUTHORIZED_USERS = {
    "admin": {"name": "管理者", "password": "xxx", "role": "admin", "start_date": "2025-01-01", "end_date": "2026-12-31"},
    "grace": {"name": "Grace", "password": "xxx", "role": "vip", "start_date": "2025-01-01", "end_date": "2026-12-31"},
    "user1": {"name": "使用者一", "password": "xxx", "role": "member", "start_date": "2025-05-01", "end_date": "2025-10-31"},
}

BRAND = {
    "logo_path": str(Path(__file__).resolve().parent.parent / "assets" / "logo.png"),
    "footer": "《影響力》傳承策略平台｜永傳家族辦公室  •  https://gracefo.com  •  聯絡信箱：123@gracefo.com",
}

@dataclass
class UserSession:
    username: str
    display_name: str
    role: str
    start_date: str
    end_date: str

def is_within(date_str: str) -> bool:
    try:
        s = date.fromisoformat(date_str)
        return s <= date.today()
    except Exception:
        return True

def not_expired(date_str: str) -> bool:
    try:
        e = date.fromisoformat(date_str)
        return date.today() <= e
    except Exception:
        return True
