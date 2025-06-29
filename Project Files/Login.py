import streamlit as st

def login_page():
    st.set_page_config(page_title="Login - CitizenAI")

    st.title("🔐 Citizen Login")
    st.subheader("Please log in to continue")

    # 🟢 Initialize session state
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    if "remember" not in st.session_state:
        st.session_state["remember"] = False
    if "login_success" not in st.session_state:
        st.session_state["login_success"] = False

    # ✅ Always show login form
    username = st.text_input("Username", value=st.session_state["username"] if st.session_state["remember"] else "")
    password = st.text_input("Password", type="password")
    remember_me = st.checkbox("Remember Me", value=st.session_state["remember"])

    if st.button("Login", key="login_btn"):
        if username == "chaitu@gmail.com" and password == "admin123":
            st.session_state["authenticated"] = True
            st.session_state["username"] = username
            st.session_state["remember"] = remember_me
            st.session_state["login_success"] = True
            st.rerun()
        else:
            st.error("❌ Invalid credentials. Please try again.")

    # ✅ Show success message just below the form
    if st.session_state["authenticated"] and st.session_state["login_success"]:
        st.success("✅ Login successful!")
        st.session_state["login_success"] = False
