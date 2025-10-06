
import os
import streamlit as st

def ensure_page_config():
    """Set global page config and inject global CSS once per session."""
    if not st.session_state.get("_page_config_done", False):
        favicon_path = os.path.join(os.path.dirname(__file__), "favicon.png")
        try:
            st.set_page_config(
                page_title="《影響力》傳承策略平台｜永傳家族傳承導師",
                page_icon=favicon_path if os.path.exists(favicon_path) else "💠",
                layout="wide"
            )
        except Exception:
            # In case set_page_config is called elsewhere
            pass

        # Global CSS: hide Streamlit chrome for a clean, branded look
        st.markdown("""<style>
  /* Hide hamburger, deploy btn, toolbar, and sidebar toggle */
  [data-testid="stToolbar"],
  .stAppDeployButton,
  button[kind="header"],
  [data-testid="collapsedControl"] { display: none !important; }

  /* Optional: soften page background a bit */
  .stApp { background-color: #fbfbfd; }

  /* Basic container width and typography tuning */
  .section { padding: 24px 0; }
  .section-centered { text-align: center; }
  .hero h1 { font-size: 2.1rem; margin-bottom: 0.35rem; }
  .hero p  { font-size: 1.05rem; opacity: 0.9; }
  .cta { display:inline-block; padding: 10px 16px; border-radius: 10px;
         background: #2E8BC0; color: white; text-decoration: none; font-weight: 600; }
  .cta:hover { filter: brightness(0.92); }
  .card { border-radius: 16px; background: white; padding: 18px;
          box-shadow: 0 4px 18px rgba(0,0,0,0.06); }
  .muted { color: #667085; font-size: 0.95rem; }
</style>
""", unsafe_allow_html=True)

        st.session_state["_page_config_done"] = True
