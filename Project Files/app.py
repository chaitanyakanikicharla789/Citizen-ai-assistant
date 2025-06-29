import streamlit as st
import Home
import About
import Chat
import Dashboard
import Login

# ✅ STEP 1: Inject CSS FIRST
st.markdown("""
    <style>
    /* Sidebar radio buttons → styled like boxes */
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
        color: #ffffff !important;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ STEP 2: Set page config
st.set_page_config(page_title="Citizen AI Assistant", layout="wide")

# ✅ STEP 3: Maintain session state for navigation
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# ✅ STEP 4: Sidebar title
st.sidebar.markdown("## 📚 Navigation")

# ✅ STEP 5: Define navigation options (with emoji labels)
navigation_options = {
    "🏠 Home": "Home",
    "ℹ️ About": "About",
    "💬 Chat": "Chat",
    "📊 Dashboard": "Dashboard",
    "🔐 Login": "Login"
}

# ✅ STEP 6: Get default index for sidebar
default_index = list(navigation_options.values()).index(st.session_state["page"])

# ✅ STEP 7: Show radio button sidebar menu
selected_label = st.sidebar.radio("Go to:", list(navigation_options.keys()), index=default_index)

# ✅ STEP 8: Update current page
st.session_state["page"] = navigation_options[selected_label]

# ✅ STEP 9: Route to selected page
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
