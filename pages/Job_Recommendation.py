# pages/Job_Recommendation.py
import streamlit as st
from math import ceil

st.set_page_config(page_title="Job Recommendation", layout="centered")

st.title("💼 Job Recommendation Portal")

if "ats_score" not in st.session_state or "resume_text" not in st.session_state:
    st.warning("⚠️ Please analyze your resume first using the ATS Analyzer page.")
    st.stop()

resume_text = st.session_state["resume_text"].lower()
ats_score = st.session_state["ats_score"]

# small mock job list with keywords (expandable)
JOBS = [
    {"company":"TCS","role":"Data Analyst","keywords":["python","sql","excel","power bi"]},
    {"company":"Infosys","role":"Python Developer","keywords":["python","django","api","git"]},
    {"company":"Accenture","role":"ML Engineer","keywords":["machine learning","tensorflow","scikit-learn"]},
    {"company":"Wipro","role":"Frontend Dev","keywords":["javascript","react","css","html"]},
]

def match_score(resume, job_kws):
    matched = [k for k in job_kws if k in resume]
    return ceil((len(matched)/len(job_kws))*100), matched

st.subheader(f"Your ATS Score: {ats_score}/100")
st.divider()

for job in JOBS:
    score, matched = match_score(resume_text, job["keywords"])
    st.markdown(f"**{job['company']} — {job['role']}**")
    st.progress(score/100)
    st.write(f"Match: {score}% — Matched skills: {', '.join(matched) if matched else 'None'}")
    # estimate hiring chance: mix ATS score and job match
    chance = int(min(100, (0.6*score) + (0.4*ats_score)))
    st.write(f"Estimated chance: **{chance}%**")
    st.markdown("---")

if st.button("← Back to ATS Analyzer"):
    st.switch_page("pages/ATS_Analyzer.py")
