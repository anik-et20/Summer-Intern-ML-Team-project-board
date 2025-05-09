import spacy
import re
from typing import Dict, List

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Optional: Predefined keyword lists (can be extended or loaded from a CSV)
TECH_KEYWORDS = [
    "Python", "Java", "JavaScript", "Django", "Flask", "AWS", "Docker", 
    "SQL", "React", "Node.js", "REST APIs", "Git", "Kubernetes", "HTML", "CSS"
]
DEGREES = ["Bachelor", "Master", "PhD", "B.Tech", "M.Tech", "MBA", "BSc", "MSc"]

# --- Main function ---
def extract_key_requirements(text: str) -> Dict[str, List[str]]:
    doc = nlp(text)

    skills = set()
    education = set()
    experience = []

    # Extract skills based on keyword matching
    for token in doc:
        if token.text in TECH_KEYWORDS:
            skills.add(token.text)

    # Extract experience using regex
    exp_patterns = [
        r"(\d+)\+?\s+years? of experience",
        r"minimum of (\d+)\s+years",
        r"at least (\d+)\s+years"
    ]
    for pattern in exp_patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        experience.extend(matches)

    # Extract degrees
    for sent in doc.sents:
        for deg in DEGREES:
            if deg.lower() in sent.text.lower():
                education.add(sent.text.strip())

    return {
        "skills": list(skills),
        "experience_years": list(set(experience)),
        "education": list(education),
    }

# Example usage
if __name__ == "__main__":
    jd_text = """
    We are seeking a Software Engineer with 3+ years of experience in Python and Django.
    Familiarity with Docker and AWS is required. A Bachelor's degree in Computer Science is necessary.
    """

    result = extract_key_requirements(jd_text)
    print("Extracted Key Requirements:")
    print(result)
