import streamlit as st
import Home
import About
import Chat
import Dashboard
import Login

# Page config
st.set_page_config(page_title="Citizen AI Assistant", layout="wide")

# ✅ Maintain session state for page switching
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# ✅ Inject Custom CSS for box-style sidebar buttons
st.markdown("""
    <style>
    /* --- Sidebar radio → Box-style buttons --- */
    div[data-baseweb="radio"] > div {
        display: flex;
        flex-direction: column;
        gap: 0.6rem;
    }
    div[data-baseweb="radio"] label {
        border: 2px solid #1a73e8;
        border-radius: 0.75rem;
        padding: 0.55rem 1rem;
        font-weight: 600;
        color: #1a73e8;
        background: #ffffff;
        transition: all 120ms ease-in-out;
        cursor: pointer;
    }
    div[data-baseweb="radio"] label:hover {
        background: #e8f0fe;
    }
    div[data-baseweb="radio"] input:checked + div {
        background: #1a73e8 !important;
        color: #ffffff  !important;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Sidebar Title
st.sidebar.markdown("## 📚 Navigation")

# Emoji-based menu
navigation_options = {
    "🏠 Home": "Home",
    "ℹ️ About": "About",
    "💬 Chat": "Chat",
    "📊 Dashboard": "Dashboard",
    "🔐 Login": "Login"
}

# Get index of current page
default_index = list(navigation_options.values()).index(st.session_state["page"])

# Sidebar radio menu (now styled)
selected_label = st.sidebar.radio("Go to:", list(navigation_options.keys()), index=default_index)

# Update session state
st.session_state["page"] = navigation_options[selected_label]

# ✅ Page routing
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
