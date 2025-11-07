import streamlit as st
import time

def signup_page():
    st.title("📝 Create Account")

    username = st.text_input("Create Username")
    password = st.text_input("Create Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if not username or not password:
            st.error("Please fill in all fields.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        elif username in st.session_state.users:
            st.warning("Username already exists. Please log in.")
        else:
            st.session_state.users[username] = password
            st.success("Account created successfully!")
            time.sleep(1)
            st.session_state.page = "login"
            st.rerun()

    st.markdown("---")
    st.caption("Already have an account?")
    if st.button("Go to Login"):
        st.session_state.page = "login"
        st.rerun()
