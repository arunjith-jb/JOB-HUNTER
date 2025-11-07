# pages/ATS_Analyzer.py
import streamlit as st
import re
from PyPDF2 import PdfReader

st.set_page_config(page_title="ATS Resume Analyzer", layout="centered")

# ---------- Helpers ----------
def extract_text_from_pdf(uploaded_file):
    try:
        reader = PdfReader(uploaded_file)
        text = ""
        for p in reader.pages:
            page_text = p.extract_text()
            if page_text:
                text += page_text + "\n"
        return text
    except Exception:
        return ""

def normalize(text):
    return re.sub(r'\s+', ' ', text).strip().lower()

def calculate_ats_score(text):
    # (simple realistic scoring example)
    sections = ["education", "experience", "skills", "projects", "certifications", "summary"]
    found_sections = sum(1 for s in sections if s in text)
    section_score = (found_sections / len(sections)) * 30

    it_keywords = [
        "python","sql","excel","power bi","machine learning","data analysis",
        "java","javascript","react","aws","azure","docker","kubernetes","git"
    ]
    keyword_hits = sum(1 for k in it_keywords if k in text)
    keyword_score = min((keyword_hits / len(it_keywords)) * 50, 50)

    penalty = 10 if any(b in text for b in ["table", "graphic", "image", "screenshot"]) else 0

    length = len(text.split())
    if length < 120:
        length_score = 5
    elif length < 300:
        length_score = 12
    else:
        length_score = 20

    score = section_score + keyword_score + length_score - penalty
    return int(max(0, min(100, round(score))))

def suggest_improvements(text):
    # return missing keywords and high-level advice
    all_skills = ["python","sql","excel","power bi","machine learning","data analysis",
                  "java","javascript","react","aws","docker","kubernetes","git"]
    missing = [k for k in all_skills if k not in text]
    return missing[:12]  # short list

# ---------- UI ----------
st.title("📄 ATS Resume Analyzer (IT roles)")

if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
    st.warning("Please log in first (Signup → Login).")
    st.stop()

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    raw = extract_text_from_pdf(uploaded_file)
    if not raw.strip():
        st.error("Couldn't extract text. Try another PDF (text-based, not scanned).")
        st.stop()

    text = normalize(raw)

    # detect best role (simple heuristic)
    # you can extend to multiple roles; here we just compute score for IT broadly
    ats_score = calculate_ats_score(text)
    missing_skills = suggest_improvements(text)

    # SAVE to session_state for Job Recommendation page
    st.session_state["resume_text"] = raw            # raw text (not normalized) for better display later
    st.session_state["ats_score"] = ats_score
    st.session_state["missing_skills"] = missing_skills

    # SHOW only ATS score + recommendations (as you requested)
    st.subheader("🎯 ATS Score")
    st.metric(label="Compatibility (out of 100)", value=f"{ats_score} / 100")

    if ats_score >= 90:
        st.success("✅ Excellent — ATS-ready. No major changes required.")
    elif ats_score >= 60:
        st.info("👍 Decent — add missing skills and standard sections to push to 90+.")
    else:
        st.warning("⚠️ Low — simplify formatting, add sections and role keywords to improve.")

    st.divider()
    st.subheader("🛠 Recommendations to improve your ATS score")
    if missing_skills:
        st.write("Add or emphasize these skills in your resume (examples):")
        st.write(", ".join(missing_skills))
    else:
        st.write("No major skill gaps detected.")

    st.write("- Ensure headings: Experience, Education, Skills, Projects.")
    st.write("- Avoid tables, images, or multiple columns (ATS may skip them).")
    st.write("- Use simple bullet points for achievements with numbers/results.")
    st.divider()

    # NAVIGATE to Job Recommendation (do NOT use query params)
    if st.button("🔍 Go to Job Recommendation"):
        # session state already has resume_text and ats_score — Job page will read them
        st.switch_page("pages/Job_Recommendation.py")

else:
    st.info("Please upload a PDF resume (text-based) to analyze.")
