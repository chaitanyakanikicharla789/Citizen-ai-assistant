import streamlit as st

def login_page():
    st.set_page_config(page_title="Login - CitizenAI")

    st.title("🔐 Citizen Login")
    st.subheader("Please log in to continue")

    # Initialize session state
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    if "remember" not in st.session_state:
        st.session_state["remember"] = False

    # Sidebar Navigation
    st.sidebar.header("📚 Navigation")
    st.sidebar.markdown("- 🏠 Home")
    st.sidebar.markdown("- 💬 Chat")
    st.sidebar.markdown("- 📊 Dashboard")
    st.sidebar.markdown("- ℹ️ About")
    st.sidebar.markdown("- 🔐 Login")

    # Login form
    username = st.text_input("Username", value=st.session_state["username"] if st.session_state["remember"] else "")
    password = st.text_input("Password", type="password")
    remember_me = st.checkbox("Remember Me", value=st.session_state["remember"])

    if st.button("Login", key="login_btn"):
        if username == "chaitu@gmail.com" and password == "admin123":
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.session_state["remember"] = remember_me
            st.success("✅ Login successful! You can now use the sidebar.")
        else:
            st.error("❌ Invalid credentials. Please try again.")

    # After login
    if st.session_state["authenticated"]:
        st.sidebar.success(f"✅ Logged in as {st.session_state['username']}")

        if st.sidebar.button("🚪 Logout"):
            confirm = st.sidebar.checkbox("✅ Confirm Logout")
            if confirm:
                st.session_state["authenticated"] = False
                st.session_state["username"] = ""
                st.session_state["remember"] = False
                st.success("✅ Logged out successfully.")
                st.rerun()
