
import streamlit as st
from ..config import AUTHORIZED_USERS, UserSession, is_within, not_expired

def login_block() -> UserSession | None:
    st.markdown("#### 🔐 登入")
    u = st.text_input("帳號", key="auth_user")
    p = st.text_input("密碼", type="password", key="auth_pass")
    login = st.button("登入", use_container_width=True, key="auth_login_btn")
    if login:
        user = AUTHORIZED_USERS.get(u)
        if not user:
            st.error("查無此用戶")
            return None
        if user["password"] != p:
            st.error("密碼錯誤")
            return None
        if not is_within(user["start_date"]) or not not_expired(user["end_date"]):
            st.error("帳號未生效或已過期")
            return None
        ses = UserSession(username=u, display_name=user["name"], role=user["role"],
                          start_date=user["start_date"], end_date=user["end_date"])
        st.session_state["user"] = ses
        st.rerun()
    return None

def get_user() -> UserSession | None:
    return st.session_state.get("user")
