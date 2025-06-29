import streamlit as st
import Home
import About
import Chat
import Dashboard
import Login

# ✅ Step 1: Set page config
st.set_page_config(page_title="Citizen AI Assistant", layout="wide")

# ✅ Step 2: Initialize session state
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# ✅ Step 3: Inject CSS for box-style buttons
st.markdown("""
    <style>
    .sidebar-button {
        display: block;
        padding: 0.6rem 1rem;
        margin-bottom: 0.5rem;
        text-align: center;
        background-color: #ffffff;
        border: 2px solid #1a73e8;
        color: #1a73e8;
        font-weight: bold;
        border-radius: 10px;
        text-decoration: none;
        transition: 0.2s ease-in-out;
    }
    .sidebar-button:hover {
        background-color: #e8f0fe;
    }
    .sidebar-button.selected {
        background-color: #1a73e8;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# ✅ Step 4: Sidebar Title
st.sidebar.markdown("## 📚 Navigation")

# ✅ Step 5: Define navigation options
pages = {
    "🏠 Home": "Home",
    "ℹ️ About": "About",
    "💬 Chat": "Chat",
    "📊 Dashboard": "Dashboard",
    "🔐 Login": "Login"
}

# ✅ Step 6: Display buttons in sidebar (as links with CSS styling)
for label, name in pages.items():
    is_selected = st.session_state["page"] == name
    button_style = "sidebar-button selected" if is_selected else "sidebar-button"
    button_html = f'<a href="#" class="{button_style}" onclick="window.location.reload();">{label}</a>'
    if st.sidebar.markdown(button_html, unsafe_allow_html=True):
        st.session_state["page"] = name

# ✅ Step 7: Route to selected page
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
