import streamlit as st
import json
import re

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(page_title="Job Recommendations", layout="wide")

# -------------------------------------------------------
# AUTH GUARD
# -------------------------------------------------------
if "LOGGED_IN" not in st.session_state or not st.session_state["LOGGED_IN"]:
    st.warning("Please login to access Job Recommendations.")
    st.stop()

# Ensure ATS analysis was done
if "resume_text" not in st.session_state:
    st.warning("Please complete the ATS Analysis first.")
    st.stop()

resume_text = st.session_state["resume_text"]

# -------------------------------------------------------
# CUSTOM STYLING – MATCH ATS PAGE DESIGN
# -------------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* Background Gradient */
.stApp {
    background: radial-gradient(circle at top left, #2b5876, #0f2027);
}

/* Remove default padding */
.block-container {
    padding-top: 20px !important;
}

/* Wrapper */
.job-wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
}

/* Main card */
.job-card {
    width: 1000px;
    padding: 35px 40px;
    border-radius: 12px;

    background: rgba(10, 12, 30, 0.92);
    border: 1px solid rgba(255,255,255,0.06);
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.55);

    color: white;
    animation: slideIn 0.7s ease-out;
}

/* Title */
.job-title {
    font-size: 32px;
    font-weight: 800;
    color: #ffffff;
}

/* Subtitle */
.job-subtitle {
    font-size: 14px;
    color: #c6d2ff;
    margin-bottom: 20px;
}

/* Divider */
.job-divider {
    height: 1px;
    border: none;
    background: linear-gradient(90deg, #4a90e2, transparent);
    margin: 10px 0 25px;
}

/* Job card surface */
.job-box {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 18px 20px;
    border-radius: 10px;

    margin-bottom: 15px;
    transition: 0.25s ease-in-out;
}

/* Hover effect */
.job-box:hover {
    background: rgba(255,255,255,0.12);
    transform: translateY(-3px);
}

/* Job Title */
.job-head {
    font-size: 20px;
    font-weight: 700;
    color: #d9e3ff;
    margin-bottom: 3px;
}

/* Company / Location */
.job-meta {
    font-size: 14px;
    color: #b7c4ff;
    margin-bottom: 8px;
}

/* Keywords */
.keyword {
    display: inline-block;
    background: #1e2a44;
    padding: 3px 10px;
    border-radius: 6px;
    margin-right: 5px;
    margin-bottom: 4px;
    font-size: 12px;
    color: #9fc6ff;
}

/* Fade-in Animation */
@keyframes slideIn {
    0% { opacity: 0; transform: translateY(22px); }
    100% { opacity: 1; transform: translateY(0); }
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# SAMPLE JOB DATABASE (CAN BE REPLACED WITH REAL API)
# -------------------------------------------------------
jobs_data = [
    {
        "title": "Python Developer",
        "company": "TechNova Solutions",
        "location": "Bangalore, India",
        "skills": ["python", "django", "api", "rest", "sql"]
    },
    {
        "title": "Data Analyst",
        "company": "Insight Analytics",
        "location": "Hyderabad, India",
        "skills": ["excel", "sql", "python", "powerbi"]
    },
    {
        "title": "Machine Learning Engineer",
        "company": "AI Genesis Labs",
        "location": "Remote",
        "skills": ["python", "machine learning", "tensorflow", "pandas"]
    },
    {
        "title": "Full-Stack Developer",
        "company": "Skyline Tech",
        "location": "Chennai, India",
        "skills": ["javascript", "react", "python", "nodejs"]
    },
]

# -------------------------------------------------------
# MATCHING ALGORITHM
# -------------------------------------------------------
resume_lower = resume_text.lower()

def job_match_score(job):
    score = 0
    for skill in job["skills"]:
        if skill.lower() in resume_lower:
            score += 1
    return score

# Rank jobs highest → lowest
sorted_jobs = sorted(jobs_data, key=job_match_score, reverse=True)

# -------------------------------------------------------
# PAGE BODY
# -------------------------------------------------------
st.markdown('<div class="job-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="job-card">', unsafe_allow_html=True)

st.markdown('<div class="job-title">Job Recommendations</div>', unsafe_allow_html=True)
st.markdown('<div class="job-subtitle">Based on your resume content, here are curated job roles matched to your skills.</div>', unsafe_allow_html=True)
st.markdown('<hr class="job-divider" />', unsafe_allow_html=True)

# -------------------------------------------------------
# SHOW JOBS
# -------------------------------------------------------
for job in sorted_jobs:
    matches = job_match_score(job)

    st.markdown('<div class="job-box">', unsafe_allow_html=True)

    st.markdown(f'<div class="job-head">{job["title"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="job-meta">{job["company"]} • {job["location"]}</div>', unsafe_allow_html=True)

    # Skills as tags
    st.markdown('<div style="margin-bottom: 8px;">Required Skills:</div>', unsafe_allow_html=True)
    for skill in job["skills"]:
        st.markdown(f'<span class="keyword">{skill}</span>', unsafe_allow_html=True)

    # Match score
    st.markdown(f"<div style='margin-top:10px; font-size:13px; color:#c7d7ff;'>Match Score: {matches} / {len(job['skills'])}</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
