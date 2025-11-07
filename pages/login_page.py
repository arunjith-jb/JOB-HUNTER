import streamlit as st
import time

def login_page():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in st.session_state.users and st.session_state.users[username] == password:
            st.session_state.logged_in_user = username
            st.success(f"Welcome, {username}!")
            time.sleep(1)
            st.session_state.page = "about"
            st.rerun()
        else:
            st.error("Invalid username or password")

    st.markdown("---")
    if st.button("Go to Sign Up"):
        st.session_state.page = "signup"
        st.rerun()
