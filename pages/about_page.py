import streamlit as st

def about_page():
    st.title("📘 About Our Project")

    st.markdown("""
    ### Resume Analyzer - Smart ATS Compatibility Checker

    This platform helps job seekers evaluate how well their resume matches job descriptions
    using AI-powered ATS (Applicant Tracking System) analysis.

    #### 🚀 What It Does:
    - Analyzes resume text and calculates ATS score  
    - Suggests missing keywords for improvement  
    - Finds companies hiring for your matching skills  

    #### 💡 Built With:
    - **Python, Streamlit, NLP, ML**
    - **Data Analysis & Resume Parsing**

    #### 👨‍💻 Developed By:
    **Arunjith JB**  
    📞 80756 88735  
    🎓 Boston Institute of Analytics (Technopark, Trivandrum)
    """)

    st.markdown("---")
    if st.button("Go to ATS Resume Checker ▶️"):
        st.session_state.page = "ats_checker"
        st.rerun()

    if st.button("Logout"):
        st.session_state.logged_in_user = None
        st.session_state.page = "login"
        st.rerun()
