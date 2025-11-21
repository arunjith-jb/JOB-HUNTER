# utils/ats_scoring.py

import re
from typing import Dict, List, Tuple


# -----------------------------------------------------------------
# MEDIUM SKILL BANK (~300 skills) – FAST + ACCURATE
# -----------------------------------------------------------------

TECH_SKILLS = [
    # Programming Languages
    "python", "java", "c", "c++", "javascript", "typescript",
    "php", "swift", "kotlin", "go", "ruby", "r", "scala",
    "matlab", "bash", "shell scripting",

    # Frameworks / Libraries
    "react", "node.js", "django", "flask", "spring boot", "express",
    "fastapi", "angular", "vue", "laravel", "flutter", "tensorflow",
    "pytorch", "keras", "scikit-learn", "pandas", "numpy", "opencv",

    # Cloud
    "aws", "azure", "gcp", "google cloud", "cloud computing",

    # DevOps
    "docker", "kubernetes", "jenkins", "ci/cd", "git", "github", "gitlab",

    # Databases
    "mysql", "postgresql", "sqlite", "mongodb", "redis", "firebase",
    "elasticsearch",

    # Data / Analytics
    "sql", "power bi", "tableau", "excel", "data analysis",
    "statistics", "machine learning", "deep learning",
    "etl", "data visualization"
]

BUSINESS_SKILLS = [
    "project management", "business analysis", "requirements gathering",
    "stakeholder management", "presentation", "documentation",
    "market research", "sales", "marketing", "finance", "budgeting",
    "accounting", "strategic planning", "operations management",
    "customer service", "negotiation", "leadership",
]

TOOLS_SKILLS = [
    "jira", "confluence", "slack", "notion", "asana", "trello",
    "microsoft office", "word", "excel", "powerpoint",
    "figma", "adobe xd"
]

SOFT_SKILLS = [
    "communication", "teamwork", "leadership", "critical thinking",
    "problem solving", "creativity", "adaptability", "time management",
    "attention to detail", "collaboration", "decision making",
]

ALL_SKILLS = list(set(TECH_SKILLS + BUSINESS_SKILLS + TOOLS_SKILLS + SOFT_SKILLS))


# -----------------------------------------------------------------
# SECTION DETECTION
# -----------------------------------------------------------------
SECTION_KEYWORDS = {
    "experience": ["experience", "work history", "employment", "professional experience"],
    "skills": ["skills", "technical skills", "core competencies"],
    "education": ["education", "academics", "qualification"],
    "projects": ["projects", "project work", "academic projects"],
    "summary": ["summary", "profile", "objective"],
    "contact": ["contact", "email", "phone", "linkedin"]
}


def section_score(text: str) -> Tuple[float, List[str]]:
    text = text.lower()
    present = []
    missing = []

    important_sections = ["experience", "skills", "education", "projects", "contact"]

    for section, keywords in SECTION_KEYWORDS.items():
        if any(k in text for k in keywords):
            present.append(section)
        else:
            missing.append(section)

    score = (len(present) / len(important_sections)) * 100
    return min(score, 100), missing


# -----------------------------------------------------------------
# PARSEABILITY SCORE
# -----------------------------------------------------------------
def parseability_score(text: str) -> float:
    lines = text.split("\n")
    non_empty = [l.strip() for l in lines if l.strip()]

    if len(lines) == 0:
        return 0.0

    ratio = len(non_empty) / len(lines)

    # Bullet detection
    bullets = [l for l in non_empty if l.startswith(("-", "*", "•"))]
    bullet_ratio = len(bullets) / len(non_empty) if non_empty else 0

    score = (ratio * 60) + (bullet_ratio * 40)
    return min(score, 100)


# -----------------------------------------------------------------
# LENGTH SCORE
# -----------------------------------------------------------------
def length_score(word_count: int) -> float:
    if 350 <= word_count <= 800:
        return 100.0
    if 250 <= word_count < 350 or 800 < word_count <= 1000:
        return 70.0
    if 150 <= word_count < 250 or 1000 < word_count <= 1300:
        return 40.0
    return 20.0


# -----------------------------------------------------------------
# ACHIEVEMENT SCORE
# -----------------------------------------------------------------
def achievements_score(text: str) -> Tuple[float, int]:
    bullet_lines = [l.lower() for l in text.split("\n") if l.strip().startswith(("-", "*", "•"))]

    if not bullet_lines:
        return 20, 0

    pattern = re.compile(r"(\d+%|\d+|\$|₹)")
    metrics = sum(1 for line in bullet_lines if pattern.search(line))

    ratio = metrics / len(bullet_lines)
    return min(ratio * 100, 100), metrics


# -----------------------------------------------------------------
# SKILL MATCH SCORE
# -----------------------------------------------------------------
def skill_match_score(text: str) -> Tuple[float, List[str], List[str]]:
    text = text.lower()
    matched = [skill for skill in ALL_SKILLS if skill in text]
    missing = [skill for skill in ALL_SKILLS if skill not in text]

    score = (len(matched) / len(ALL_SKILLS)) * 100
    return min(score, 100), matched, missing


# -----------------------------------------------------------------
# FINAL ATS ANALYSIS FUNCTION
# -----------------------------------------------------------------
def analyze_resume(text: str):
    text_clean = text.strip()
    word_count = len(text_clean.split())

    # 1. Parseability
    pscore = parseability_score(text_clean)

    # 2. Sections
    sscore, missing_sections = section_score(text_clean)

    # 3. Length
    lscore = length_score(word_count)

    # 4. Achievements
    ascore, metric_count = achievements_score(text_clean)

    # 5. Skills
    kscore, matched_skills, missing_skills = skill_match_score(text_clean)

    # Weighted final
    final = (
        pscore * 0.25 +
        sscore * 0.25 +
        lscore * 0.15 +
        ascore * 0.15 +
        kscore * 0.20
    )

    scores = {
        "parseability": round(pscore, 1),
        "sections": round(sscore, 1),
        "length": round(lscore, 1),
        "achievements": round(ascore, 1),
        "skills": round(kscore, 1),
        "final": round(final, 1)
    }

    # Suggestions
    suggestions = []

    if pscore < 70:
        suggestions.append("Improve resume formatting. Avoid columns, tables, images, and use simple bullet points.")

    if sscore < 80:
        suggestions.append(f"Missing important sections: {', '.join(missing_sections)}. Add them for a complete resume.")

    if lscore < 70:
        if word_count < 300:
            suggestions.append("Resume is too short. Add more responsibilities, projects, and measurable achievements.")
        else:
            suggestions.append("Resume is too long. Remove irrelevant experience and focus on key achievements.")

    if ascore < 50:
        suggestions.append("Add more measurable achievements like numbers, percentages, revenue impact, or timelines.")

    if kscore < 60:
        suggestions.append("Add missing relevant skills for better ATS performance.")

    return scores, suggestions, matched_skills, missing_skills
