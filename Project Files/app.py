import streamlit as st
import Home
import About
import Chat
import Dashboard
import Login

# Page config
st.set_page_config(page_title="Citizen AI Assistant", layout="wide")

# ✅ Maintain session state to handle navigation & Get Started button
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# ✅ Sidebar Title
st.sidebar.markdown("## 📚 Navigation")

# Sidebar with emoji-based options
navigation_options = {
    "🏠 Home": "Home",
    "ℹ️ About": "About",
    "💬 Chat": "Chat",
    "📊 Dashboard": "Dashboard",
    "🔐 Login": "Login"
}

# Find default index based on current session page
default_index = list(navigation_options.values()).index(st.session_state["page"])

# Show radio in sidebar
selected_label = st.sidebar.radio("Go to:", list(navigation_options.keys()), index=default_index)

# Update session state based on selection
st.session_state["page"] = navigation_options[selected_label]

# ✅ Routing to actual page
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
