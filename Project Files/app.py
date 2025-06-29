import streamlit as st
import Home
import About
import Chat
import Dashboard
import Login

# ✅ Set page config
st.set_page_config(page_title="Citizen AI Assistant", layout="wide")

# ✅ Maintain current page in session
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# ✅ Inject EXACT CSS matching your Get Started button
st.markdown("""
    <style>
    .get-started-button {
        display: block;
        width: 100%;
        padding: 10px 16px;
        margin: 8px 0;
        background-color: white;
        color: #1a73e8;
        border: 2px solid #1a73e8;
        border-radius: 12px;
        font-weight: 600;
        text-align: center;
        text-decoration: none;
        transition: all 0.2s ease-in-out;
        box-shadow: 1px 2px 5px rgba(0,0,0,0.05);
    }
    .get-started-button:hover {
        background-color: #e8f0fe;
        color: #1a73e8;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Sidebar title
st.sidebar.markdown("## 📚 Navigation")

# ✅ Navigation button creator (HTML styled exactly like Get Started)
def nav_link(label, page_key):
    if st.sidebar.button(label, key=page_key):
        st.session_state["page"] = page_key

# ✅ Sidebar buttons (styled like Get Started)
nav_link("🏠 Home", "Home")
nav_link("ℹ️ About", "About")
nav_link("💬 Chat", "Chat")
nav_link("📊 Dashboard", "Dashboard")
nav_link("🔐 Login", "Login")

# ✅ Routing logic
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
