import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Resume Analyzer", layout="wide")

# ---- SESSION STATE ----
if "page" not in st.session_state:
    st.session_state.page = "signup"

def go_to(page):
    st.session_state.page = page
    st.rerun()

# ---- PAGES ----
def signup_page():
    st.title("📝 Sign Up")
    st.subheader("Create your account to continue")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if password != confirm:
            st.error("❌ Passwords do not match")
        elif username and password:
            st.session_state.username = username
            st.success("✅ Account created successfully! Please log in.")
            go_to("login")
        else:
            st.warning("Please fill all fields")

    st.write("Already have an account?")
    if st.button("Login here"):
        go_to("login")

def login_page():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == st.session_state.get("username") and password:
            st.session_state.logged_in = True
            go_to("about")
        else:
            st.error("❌ Invalid credentials")

    st.write("Don't have an account?")
    if st.button("Sign Up here"):
        go_to("signup")

def about_page():
    st.title("💼 About Our Project")
    st.write("""
    ### Resume Analyzer by **Arunjith JB**
    📍 Created at Boston Institute of Analytics, Technopark  
    📞 Contact: 8075-688-735  
    ---
    This platform helps job seekers:
    - ✅ Analyze resumes with **real ATS systems**
    - 🧠 Identify **missing keywords**
    - 💪 Get personalized **improvement recommendations**
    - 🧭 Discover companies hiring for their skillset  

    Built using **Streamlit**, **Python**, and **AI models** to deliver accurate results.
    """)

    st.divider()
    st.subheader("Navigation")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📄 Go to ATS Resume Checker"):
            go_to("ats")
    with col2:
        if st.button("🏢 Job Recommendations"):
            go_to("jobs")

def ats_analyzer_page():
    st.switch_page("pages/ATS_Analyzer.py")

def job_recommendation_page():
    st.switch_page("pages/Job_Recommendation.py")

# ---- PAGE ROUTER ----
if st.session_state.page == "signup":
    signup_page()
elif st.session_state.page == "login":
    login_page()
elif st.session_state.page == "about":
    about_page()
elif st.session_state.page == "ats":
    ats_analyzer_page()
elif st.session_state.page == "jobs":
    job_recommendation_page()
