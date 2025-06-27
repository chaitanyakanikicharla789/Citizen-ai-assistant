# ✅ Home.py (Landing page with sidebar instructions)
import streamlit as st

def home_page():
    st.title("🏡 Welcome to Citizen AI Assistant")

    st.markdown("""
    ### 🙋‍♂️ Empowering Citizens with AI

    This assistant helps you:
    - 💬 Ask civic-related questions
    - 📊 View sentiment insights
    - 🛠️ Report local civic issues

    ---

    ➡️ **Use the sidebar** to navigate to:
    - 🧠 Chat
    - 📊 Dashboard
    - ℹ️ About
    - 🔐 Login
    """)
