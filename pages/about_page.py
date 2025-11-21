import streamlit as st

# ---------------------------------------------------------
#                 PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(layout="wide")

# ---------------------------------------------------------
#                 CUSTOM STYLING (DARK MODE + WHITE TEXT)
# ---------------------------------------------------------
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&family=Inter:wght@300;400;500;700&display=swap" rel="stylesheet">

<style>

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #0D0D0D !important;
    color: white !important;
}

/* Gradient Title */
.gradient-title {
    font-size: 60px !important;
    font-weight: 800;
    background: linear-gradient(90deg, #FFFFFF, #EAF8FF, #DDF5FF);
    -webkit-background-clip: text;
    color: transparent !important;
    padding-bottom: 20px;
    margin-top: -30px;
}

/* Section Titles */
.section-header {
    font-size: 36px !important;
    font-weight: 700;
    color: #FFFFFF !important;
    margin-top: 45px;
    margin-bottom: 15px;
}

/* Main Paragraph Text */
.big-text {
    font-size: 22px !important;
    line-height: 1.95;
    text-align: justify;
    color: #FFFFFF !important;
}

/* Content Card */
.content-card {
    background-color: #1A1A1A;
    padding: 45px;
    border-radius: 18px;
    box-shadow: 0px 4px 30px rgba(255,255,255,0.08);
    margin-top: 25px;
    color: #FFFFFF !important;
}

/* Highlight Boxes */
.highlight-box {
    background: #2E2E2E;
    padding: 25px;
    border-left: 6px solid #66CCFF;
    border-radius: 12px;
    margin: 25px 0;
    color: #FFFFFF !important;
}

/* Force All Elements to White */
p, span, div, label, h1, h2, h3, h4, h5, h6 {
    color: #FFFFFF !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
#                     PAGE TITLE
# ---------------------------------------------------------
st.markdown('<h1 class="gradient-title">About This Project</h1>', unsafe_allow_html=True)

# ---------------------------------------------------------
#                   CONTENT CONTAINER
# ---------------------------------------------------------
st.markdown('<div class="content-card">', unsafe_allow_html=True)

# ---------------------------------------------------------
#      YOUR FULL ABOUT PAGE CONTENT IN WHITE TEXT
# ---------------------------------------------------------

st.markdown("""
<div class="big-text">

## <span class="section-header">Introduction</span>  

My name is **Arunjith JB**, and this project—**the Resume ATS Analyzer and Job Recommendation System**—is a work of passion, dedication, and the desire to help job seekers overcome the invisible barriers created by modern hiring technologies. As a student of **Boston Institute of Athletics, Calcutta, near Technoparks**, pursuing **Basic Computer Science**, I have always seen computers and software development as a gateway to solving real-world problems. This project is the start of that journey, built from scratch through consistent curiosity, experimentation, and the belief that technology should empower people.

---

## <span class="section-header">My Aim & Vision</span>

My aim is simple but powerful:  
**Give every job seeker a fair chance.**

Modern hiring systems use **Applicant Tracking Systems (ATS)** to filter resumes long before a human sees them. Skilled applicants are rejected automatically because their resume does not contain enough keywords or proper structure.

I wanted to build something that:

- Reads your resume like a real ATS  
- Scores it using **Machine Learning**  
- Shows missing keywords  
- Suggests improvements  
- Helps you understand how hiring systems think  
- Recommends jobs based on real skills  

This project reflects that vision.

---

## <span class="section-header">How My Idea Started</span>

The idea came from observing friends who were constantly rejected from jobs without explanation.  
Recruiters never saw their resumes—ATS silently filtered them out.

This felt unfair.

So I decided to study:

- How ATS works  
- How resumes are parsed  
- Why keywords matter  
- Why formatting matters  
- Why talented people still get rejected  

This curiosity started the journey that eventually became this project.

---

## <span class="section-header">Technologies Used</span>

### ✔ **Python** — Backend & ML  
### ✔ **Streamlit** — User Interface  
### ✔ **Scikit-learn** — Machine Learning Model  
### ✔ **TF-IDF Vectorizer** — NLP processing  
### ✔ **PyPDF2** / **python-docx** — Resume parsing  
### ✔ **Custom JSON job database**  
### ✔ **Custom Authentication System**  
### ✔ **Google Fonts + Premium CSS** — Stylish UI  
### ✔ **Dark Mode Design**  

Every line of code, every module, and every UI component was hand-built.

---

## <span class="section-header">How I Built the ATS Analyzer</span>

The ATS Analyzer is powered by:

- Text extraction (PDF/DOCX)  
- TF-IDF vectorization  
- Logistic Regression ML model  
- Keyword detection  
- Missing-skill detection  
- Resume density analysis  

The ML model reads resume text and predicts:

- Resume quality  
- Resume strength  
- Keyword match level  
- Professional structure  

Then it generates:

- ATS Score  
- Suggestions  
- Missing skills  

---

## <span class="section-header">How I Built the Job Recommender</span>

The recommender:

- Extracts skills from the resume  
- Compares them with job requirement data  
- Calculates a skill-match score  
- Sorts jobs by relevance  
- Displays the best matches  

This ensures users get **smart, skill-based job suggestions**.

---

## <span class="section-header">Future Plans</span>

Planned upgrades include:

- **AI-driven resume builder**  
- **Deep learning ATS evaluator (BERT/RoBERTa)**  
- **Real-time job scraping**  
- **Career roadmap generator**  
- **Interview preparation module**  
- **Cover letter generator**  
- **Portfolio project suggestions**  
- **ATS compatibility checker per company**  
- **Dashboard with saved scores & history**  

This is only the beginning.

---

## <span class="section-header">Final Message</span>

This project is more than software.  
It is my journey, my learning, my vision.  

I am **Arunjith JB**,  
Student at **Boston Institute of Athletics, Calcutta**,  
Creator of the **Resume ATS Analyzer & Job Recommendation System**,  
And this is only the start of what I aim to build for the future.

</div>
""", unsafe_allow_html=True)

# End card
st.markdown("</div>", unsafe_allow_html=True)
