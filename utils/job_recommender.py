import json
from typing import List, Dict


def load_job_database(path: str = "data/job_database.json") -> list:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def recommend_jobs(resume_text: str,
                   jobs_db: List[Dict],
                   top_k: int = 5) -> List[Dict]:
    """
    Very simple rule-based recommender:
    counts overlap of required skills with resume text.
    """
    resume_lower = resume_text.lower()

    scored = []
    for job in jobs_db:
        skills = job.get("skills", [])
        match_count = sum(1 for s in skills if s.lower() in resume_lower)
        if match_count > 0:
            job_copy = job.copy()
            job_copy["match_score"] = match_count
            scored.append(job_copy)

    scored.sort(key=lambda j: j["match_score"], reverse=True)
    return scored[:top_k]
