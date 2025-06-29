# ✅ Home.py (Landing page with sidebar instructions)
import streamlit as st

def home_page():
    st.set_page_config(page_title="Home - Citizen AI Assistant")

    st.title("🏡 Welcome to Citizen AI Assistant")

    st.markdown("""
    ### 🙋‍♂️ Empowering Citizens with AI

    This assistant helps you:
    - 💬 Ask civic-related questions
    - 📊 View sentiment insights
    - 🛠️ Report local civic issues

    ---

    ➡️ **Use the sidebar** to navigate to:
    - ℹ️ About
    - 💬 Chat
    - 📊 Dashboard
    - 🔐 Login
    """)

    st.markdown("---")
    st.markdown("### 🚀 Ready to begin?")

    # ✅ "Get Started" button
    if st.button("🚀 Get Started"):
        st.session_state["page"] = "Chat"  # sets next page
        st.experimental_rerun()            # reloads app to go there
