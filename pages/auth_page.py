import streamlit as st
from utils.auth import signup_user, login_user

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(page_title="Login / Sign In", layout="wide")

# -------------------------------------------------------
# PROFESSIONAL CORPORATE STYLE
# -------------------------------------------------------
st.markdown("""
<style>

/* REMOVE ALL EXTRA TOP SPACE */
.block-container {
    padding-top: 0 !important;
    margin-top: 0 !important;
}

/* CLEAN GRADIENT BACKGROUND */
.stApp {
    background: linear-gradient(135deg, #0a0a23, #1b1b4d, #2e2e74);
    background-size: cover;
    background-position: center;
}

/* FORM CONTAINER AT TOP */
.auth-wrapper {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: flex-start !important;
    padding-top: 40px !important;
    margin-top: 0 !important;
}

/* PROFESSIONAL RECTANGLE AUTH BOX */
.auth-box {
    width: 460px;
    padding: 40px 45px;
    border-radius: 8px;

    background: #ffffff15;
    border: 1px solid rgba(255,255,255,0.18);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);

    box-shadow: 0 6px 28px rgba(0, 0, 0, 0.45);
}

/* TITLE */
.auth-title {
    font-size: 54px;
    font-weight: 700;
    color: white;
    text-align: center;
    letter-spacing: 1px;
    margin-bottom: 70px;
}

/* TABS (No emojis, clean style) */
.stTabs [role="tablist"] button {
    font-size: 18px !important;
    font-weight: 700 !important;
    padding: 10px !important;
    color: #dfe6ff !important;
}

.stTabs [role="tablist"] button[data-baseweb="tab"]:hover {
    color: white !important;
    border-bottom: 2px solid white !important;
}

/* LABEL TEXT */
label {
    font-size: 48px !important;
    color: white !important;
}

/* INPUT FIELDS */
input[type="text"], input[type="password"] {
    width: 100% !important;
    padding: 12px !important;
    font-size: 18px !important;
    border-radius: 6px !important;
    border: 1px solid #cccccc55 !important;
    background: rgba(255,255,255,0.12) !important;
    color: white !important;
}

/* 3D PROFESSIONAL BUTTON */
.stButton button {
    width: 100%;
    margin-top: 15px;
    padding: 14px;
    font-size: 19px !important;
    font-weight: 700 !important;

    border-radius: 6px !important;
    border: none;

    background: linear-gradient(135deg, #4a68ff, #2e46d8);
    color: white !important;

    box-shadow:
        3px 3px 10px rgba(0,0,0,0.45),
        -2px -2px 6px rgba(255,255,255,0.12);

    transition: 0.25s ease-in-out;
}

/* Hover effect */
.stButton button:hover {
    transform: translateY(-3px);
    background: linear-gradient(135deg, #5c7aff, #3a53f0);
}

/* Press effect */
.stButton button:active {
    transform: translateY(2px);
    box-shadow:
        inset 3px 3px 10px rgba(0,0,0,0.5),
        inset -3px -3px 10px rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# PAGE LAYOUT
# -------------------------------------------------------

st.markdown('<div class="auth-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="auth-box">', unsafe_allow_html=True)

st.markdown('<h1 class="auth-title">Account Access</h1>', unsafe_allow_html=True)

tab_login, tab_signup = st.tabs(["Login", "Sign Up"])

# -------------------------------------------------------
# LOGIN FORM
# -------------------------------------------------------
with tab_login:
    st.write("")  # small spacing

    login_user_input = st.text_input("Username", key="login_user")
    login_pass_input = st.text_input("Password", type="password", key="login_pass")

    if st.button("Login"):
        ok, msg = login_user(login_user_input, login_pass_input)
        if ok:
            st.success("Login Successful!")
            st.session_state["LOGGED_IN"] = True
            st.session_state["USER"] = login_user_input
            st.switch_page("pages/ATS_Analyzer.py")
        else:
            st.error(msg)

# -------------------------------------------------------
# SIGNUP FORM
# -------------------------------------------------------
with tab_signup:
    st.write("")

    signup_user_input = st.text_input("Create Username", key="signup_user")
    signup_pass_input = st.text_input("Create Password", type="password", key="signup_pass")

    if st.button("Create Account"):
        ok, msg = signup_user(signup_user_input, signup_pass_input)
        if ok:
            st.success("Account Created! Please Login.")
        else:
            st.error(msg)

st.markdown("</div></div>", unsafe_allow_html=True)
