import streamlit as st
import Home
import About
import Chat
import Dashboard
import Login

# ✅ Page Config
st.set_page_config(page_title="Citizen AI Assistant", layout="wide")

# ✅ Session State Defaults
if "page" not in st.session_state:
    st.session_state["page"] = "Home"
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""
if "remember" not in st.session_state:
    st.session_state["remember"] = False
if "logout_success" not in st.session_state:
    st.session_state["logout_success"] = False

# ✅ Sidebar Title
st.sidebar.markdown("## 📚 Navigation")

# ✅ Sidebar Navigation Buttons
def nav_button(label, page_name):
    if st.sidebar.button(label):
        st.session_state["page"] = page_name

nav_button("🏠 Home", "Home")
nav_button("ℹ️ About", "About")
nav_button("💬 Chat", "Chat")
nav_button("📊 Dashboard", "Dashboard")
nav_button("🔐 Login", "Login")

# ✅ Show Logout Button in Sidebar Only After Login
if st.session_state["authenticated"]:
    st.sidebar.markdown("---")
    st.sidebar.success(f"👋 Logged in as: {st.session_state['username']}")

    if st.sidebar.button("🚪 Logout"):
        st.session_state["authenticated"] = False
        st.session_state["username"] = ""
        st.session_state["remember"] = False
        st.session_state["logout_success"] = True
        st.session_state["page"] = "Home"
        st.rerun()

# ✅ Show logout success message only on Home page
if st.session_state.get("logout_success", False) and st.session_state["page"] == "Home":
    st.success("✅ Logged out successfully.")
    st.session_state["logout_success"] = False

# ✅ Routing to Pages (Login page will not show logout itself)
if st.session_state["page"] == "Home":
    Home.home_page()
elif st.session_state["page"] == "About":
    About.about_page()
elif st.session_state["page"] == "Chat":
    Chat.chat_page()
elif st.session_state["page"] == "Dashboard":
    Dashboard.dashboard_page()
elif st.session_state["page"] == "Login":
    Login.login_page()
