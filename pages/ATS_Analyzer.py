import streamlit as st
from utils.resume_parser import extract_text_from_resume
from utils.ats_scoring import analyze_resume

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(page_title="ATS Analyzer", layout="wide")


# -------------------------------------------------------
# LOGIN PROTECTION
# -------------------------------------------------------
if "LOGGED_IN" not in st.session_state or not st.session_state["LOGGED_IN"]:
    st.warning("Please login to access the ATS Analyzer.")
    st.stop()


# -------------------------------------------------------
# PAGE STYLE (same modern design)
# -------------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: radial-gradient(circle at top left, #283e51, #0a2342);
}

.block-container {
    padding-top: 25px !important;
}

.ats-wrapper {
    display: flex;
    justify-content: center;
    width: 100%;
}

.ats-card {
    width: 1000px;
    padding: 35px;
    border-radius: 12px;
    background: rgba(10, 12, 30, 0.92);
    border: 1px solid rgba(255,255,255,0.06);
    box-shadow: 0 14px 40px rgba(0, 0, 0, 0.55);
    color: white;
}

.ats-title {
    font-size: 30px;
    font-weight: 800;
    letter-spacing: 0.5px;
}

.ats-subtitle {
    font-size: 14px;
    color: #c3c9ff;
    margin-bottom: 16px;
}

.ats-divider {
    height: 1px;
    border: none;
    margin: 20px 0;
    background: linear-gradient(90deg, #4a68ff, transparent);
}

.section-header {
    font-size: 19px;
    font-weight: 700;
    color: #f0f3ff;
    margin-top: 25px;
}

.score-box-main {
    padding: 20px;
    border-radius: 10px;
    background: linear-gradient(135deg, #243b55, #141e30);
}

.score-main-value {
    font-size: 40px;
    font-weight: 800;
    color: #64ffda;
}

.sub-score-label {
    font-size: 14px;
    color: #d0d6ff;
    margin-top: 8px;
}

.sub-score-value {
    font-size: 20px;
    font-weight: 700;
}

.skill-tag {
    display: inline-block;
    padding: 5px 10px;
    border-radius: 999px;
    background: #1e2a44;
    margin-right: 5px;
    margin-bottom: 5px;
    font-size: 12px;
    color: #9fc6ff;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------------
# PAGE LAYOUT
# -------------------------------------------------------

st.markdown('<div class="ats-wrapper">', unsafe_allow_html=True)
st.markdown('<div class="ats-card">', unsafe_allow_html=True)

st.markdown('<div class="ats-title">ATS Resume Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="ats-subtitle">Analyze your resume for ATS compatibility, structure, skills match, achievements and overall impact.</div>', unsafe_allow_html=True)
st.markdown('<hr class="ats-divider" />', unsafe_allow_html=True)


# -------------------------------------------------------
# FILE UPLOAD
# -------------------------------------------------------

st.markdown('<div class="section-header">1. Upload Resume</div>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload your resume (PDF or DOCX)",
    type=["pdf", "docx"],
    label_visibility="collapsed"
)


if uploaded_file:

    # Extract text
    resume_text = extract_text_from_resume(uploaded_file)

    if not resume_text.strip():
        st.error("Unable to extract text from your resume. Try another file or simpler formatting.")
    else:

        # Save to session for job recommendation
        st.session_state["resume_text"] = resume_text

        # -------------------------------------------------------
        # RUN IMPROVED ATS SCORING
        # -------------------------------------------------------
        scores, suggestions, matched_skills, missing_skills = analyze_resume(resume_text)

        # -------------------------------------------------------
        # Display Extracted Text
        # -------------------------------------------------------
        st.markdown('<div class="section-header">2. Extracted Resume Text</div>', unsafe_allow_html=True)

        with st.expander("View extracted text"):
            st.write(resume_text)

        # -------------------------------------------------------
        # MAIN ATS SCORE
        # -------------------------------------------------------
        st.markdown('<div class="section-header">3. ATS Score Overview</div>', unsafe_allow_html=True)

        st.markdown('<div class="score-box-main">', unsafe_allow_html=True)

        col1, col2 = st.columns([1, 2])

        with col1:
            st.markdown(f'<div class="score-main-value">{scores["final"]}</div>', unsafe_allow_html=True)
            st.caption("Overall ATS Score (0 – 100)")

        with col2:
            st.markdown(f'<div class="sub-score-label">Parseability</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="sub-score-value">{scores["parseability"]}</div>', unsafe_allow_html=True)

            st.markdown(f'<div class="sub-score-label">Sections</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="sub-score-value">{scores["sections"]}</div>', unsafe_allow_html=True)

            st.markdown(f'<div class="sub-score-label">Length</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="sub-score-value">{scores["length"]}</div>', unsafe_allow_html=True)

            st.markdown(f'<div class="sub-score-label">Achievements</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="sub-score-value">{scores["achievements"]}</div>', unsafe_allow_html=True)

            st.markdown(f'<div class="sub-score-label">Skills Match</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="sub-score-value">{scores["skills"]}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)



        # -------------------------------------------------------
        # SKILL MATCH
        # -------------------------------------------------------
        st.markdown('<div class="section-header">4. Skill Analysis</div>', unsafe_allow_html=True)

        st.write("**Matched Skills:**")
        if matched_skills:
            for skill in matched_skills[:30]:
                st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)
        else:
            st.write("No recognizable skills detected.")

        st.write("")
        st.write("**Missing or Recommended Skills:**")
        for skill in missing_skills[:30]:
            st.markdown(f'<span class="skill-tag">{skill}</span>', unsafe_allow_html=True)


        # -------------------------------------------------------
        # IMPROVEMENT SUGGESTIONS
        # -------------------------------------------------------
        st.markdown('<div class="section-header">5. Suggestions to Improve</div>', unsafe_allow_html=True)

        if suggestions:
            for tip in suggestions:
                st.markdown(f"• {tip}")
        else:
            st.success("Your resume looks strong based on ATS analysis!")


        st.markdown('<hr class="ats-divider" />', unsafe_allow_html=True)


        # -------------------------------------------------------
        # NEXT STEP BUTTON
        # -------------------------------------------------------
        st.markdown('<div class="section-header">6. Next Step</div>', unsafe_allow_html=True)
        st.write("Get job recommendations tailored to your resume.")

        if st.button("Go to Job Recommendations"):
            st.switch_page("pages/Job_Recommendation.py")

else:
    st.info("Upload your resume to begin ATS analysis.")


st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
