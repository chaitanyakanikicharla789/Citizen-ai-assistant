# app.py
import streamlit as st
from Home import home_page
from Chat import chat_page
from Dashboard import dashboard_page
from About import about_page
from Login import login_page

# Set up default page
if "page" not in st.session_state:
    st.session_state.page = "home"

# Top-level sidebar navigation (manual routing)
st.sidebar.header("📚 Navigation")
if st.sidebar.button("🏠 Home"):
    st.session_state.page = "home"
if st.sidebar.button("💬 Chat"):
    st.session_state.page = "chat"
if st.sidebar.button("📊 Dashboard"):
    st.session_state.page = "dashboard"
if st.sidebar.button("ℹ About"):
    st.session_state.page = "about"
if st.sidebar.button("🔐 Login"):
    st.session_state.page = "login"

# Page Routing
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "chat":
    chat_page()
elif st.session_state.page == "dashboard":
    dashboard_page()
elif st.session_state.page == "about":
    about_page()
elif st.session_state.page == "login":
    login_page()