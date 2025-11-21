import streamlit as st

st.set_page_config(
    page_title="Resume ATS Analyzer",
    page_icon="📄",
    layout="wide",
)

st.title("📄 Resume ATS Analyzer")

st.write(
    """
Welcome!  

Use the **Authentication** page in the sidebar to sign up or log in.  
After logging in you can:

1. Analyze your resume using the **ATS Analyzer** page.
2. Get personalized **Job Recommendations** based on your resume.
"""
)

st.page_link("pages/auth_page.py", label="Go to Authentication", icon="🔐")
st.page_link("pages/ATS_Analyzer.py", label="Go to ATS Analyzer", icon="📊")
st.page_link("pages/Job_Recommendation.py", label="Go to Job Recommendation", icon="💼")
