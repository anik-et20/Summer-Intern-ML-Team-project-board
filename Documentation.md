# Applicant Tracking System (ATS) – Company Project Documentation

## Project Overview

This backend-only **Applicant Tracking System (ATS)** intelligently ranks multiple candidates against a **single job description (JD)** using **Large Language Models (LLMs)**. It receives a **JD (text)** and **resumes (PDFs)** via API, analyzes each resume, and returns a downloadable **Excel or CSV file** containing:

* Candidate rank
* Match score
* Summary
* Key strengths
* Areas for improvement

There is no frontend. The system is **accessed securely through an API key** and optimized for accuracy, speed, and scalability.

---

## Objective

Build a **scalable, secure, production-grade ATS backend** that:

* Accepts **1 JD** and **multiple PDF resumes**
* Uses **LLMs** for analysis and scoring
* Returns a structured **CSV/Excel** ranking sheet
* Supports **API key-based authentication**
* Follows **modern Python, testing, and architectural best practices**

---

## Key Functionalities

* Parse and extract text from PDF resumes
* Use LLMs to evaluate resumes against the JD
* Assign a match score and generate insights
* Rank candidates by score
* Export a CSV/Excel report

---

## Technology Stack

### Language & Framework

* **Language:** Python 3.11+
* **Framework:** FastAPI (high-performance, async)
* **ASGI Server:** Uvicorn with Gunicorn (for deployment)

### Document Handling

* `pdfplumber`, `PyMuPDF` (fitz), or `pdfminer.six` for resume parsing
* `pandas` for tabular data manipulation
* `openpyxl`, `csv` for exporting Excel/CSV files

### LLM Integration

* OpenAI (GPT-4 Turbo), Claude 3, or Gemini via API
* Prompt engineering or embedding-based scoring

### Security

* API key-based authentication (`x-api-key`)
* HTTPS enforcement
* Environment variable–based secret management

### Testing & Validation

* **Testing:** `pytest`, `httpx`, `pytest-cov`
* **Linting:** `ruff` or `flake8`
* **Type Checking:** `mypy`
* **Formatting:** `black`, `isort`

### Docs & Dev Tools

* Swagger UI / ReDoc (via FastAPI)
* Docker for containerization
* GitHub Actions for CI/CD and test automation
* Logging with `loguru` or standard `logging`

---

## Security Design

### API Key Authentication

All endpoints are protected using a custom FastAPI middleware that checks for a valid API key in the header:

```http
x-api-key: YOUR_SECRET_KEY
```

Unauthorized or missing keys return `403 Forbidden`.

### Additional Practices

* Rotate API keys using ENV variables
* Reject unsafe or malformed files
* Avoid storing resumes (in-memory only)
* Enable CORS policy if extending access

---

## Resume Scoring Logic

Each resume is evaluated against the JD using a custom LLM prompt like:

> Given this job description: `[JD]`, analyze this resume: `[Resume text]`. Return:
>
> * Match Score (0–100)
> * 2–3 sentence summary
> * Key Strengths
> * Areas for Improvement

The LLM response is parsed and stored in a DataFrame, then ranked by score.

---

## API Design

### `POST /v1/rank`

**Headers:**

```
x-api-key: YOUR_SECRET_KEY
Content-Type: multipart/form-data
```

**Body:**

* `job_description`: string
* `resumes`: list of PDF files

**Response:**

* `200 OK` → `.xlsx` or `.csv` download
* `403 Forbidden` → invalid API key
* `422 Unprocessable` → validation error

---

## Output Format

| Rank | Name       | Match Score | Summary              | Key Strengths      | Areas to Improve     |
| ---- | ---------- | ----------- | -------------------- | ------------------ | -------------------- |
| 1    | Jane Doe   | 92%         | Well-aligned with JD | Leadership, Python | Limited AWS exposure |
| 2    | John Smith | 87%         | Good frontend fit    | React, UX          | Weak backend skills  |

---

## Folder Structure

```
ats/
├── app/
│   ├── api/            # API routes
│   ├── services/       # LLM evaluator, PDF parser, ranker
│   ├── models/         # Pydantic schemas
│   ├── utils/          # File handling, formatter
│   ├── middleware/     # API key logic
│   └── main.py
├── tests/              # Unit + integration tests
├── .env
├── Dockerfile
├── requirements.txt
├── README.md
```

---

## Testing Strategy

* **Unit Testing:** Pytest + mock LLM APIs
* **Integration Testing:** HTTPX client tests
* **Test Coverage Goal:** ≥ 85%
* **CI Pipeline:** GitHub Actions

  * Linting, formatting, and test runs on each push

---

## Optimizations

| Category        | Best Practices                                    |
| --------------- | ------------------------------------------------- |
| **LLM Calls**   | Use parallel processing with `asyncio` or `trio`  |
| **PDF Parsing** | Cache clean texts, strip headers/footers          |
| **Memory**      | Process resumes in memory; avoid file I/O/storage |
| **Rate Limits** | Enforce LLM call limits + retries with backoff    |
| **Prompting**   | Use structured prompts with system/user roles     |
| **Security**    | Validate file size, type, and content             |
| **Exports**     | Stream file generation if handling many resumes   |

---

## Deliverables

1. Secure, containerized FastAPI backend
2. API endpoint for ranking resumes
3. LLM-based scoring engine
4. Validated CSV/Excel export logic
5. Unit + integration tests
6. README with setup and usage
7. Example output file
8. Swagger UI docs
9. `.env.template` file for secrets

---

## Summary

This ATS project is focused on **developer-grade quality, security, and performance**, delivering a smart, LLM-powered resume ranking service for companies. The backend-only API can be integrated easily with job portals or other systems and is future-proofed for scalable production usage.
