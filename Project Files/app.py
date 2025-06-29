import streamlit as st
import Home
import About
import Chat
import Dashboard
import Login

st.set_page_config(page_title="Citizen AI Assistant", layout="wide")

# ✅ Maintain page state to support "Get Started" button
if "page" not in st.session_state:
    st.session_state["page"] = "Home"

# Sidebar selection
page = st.sidebar.radio("🔽 Navigate", ["Home", "About", "Chat", "Dashboard", "Login"],
                        index=["Home", "About", "Chat", "Dashboard", "Login"].index(st.session_state["page"]))

# Display the selected page
if page == "Home":
    Home.home_page()
elif page == "About":
    About.about_page()
elif page == "Chat":
    Chat.chat_page()
elif page == "Dashboard":
    Dashboard.dashboard_page()
elif page == "Login":
    Login.login_page()
