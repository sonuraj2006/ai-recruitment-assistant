# 🤖 AI Recruitment Assistant

An AI-powered recruitment assistant for resume screening, candidate matching, ranking, assessment workflows, interview scheduling, and recruitment communication — purpose-built for the **Indian Tech Recruitment** market.

---

## 📌 Project Overview

The **AI Recruitment Assistant** helps recruiters automate the most time-consuming parts of the candidate screening and hiring workflow — from parsing resumes to scheduling interviews.

### Core Capabilities

- 📄 Upload and parse resumes (PDF & DOCX)
- 🧠 Extract candidate information (name, email, phone, skills)
- 🔍 Extract technical skills and job requirements
- 🎯 Match candidates with jobs and calculate match scores
- 🏆 Rank candidates by fit
- 🗄️ Store and manage candidates in SQLite
- 📊 Track candidate pipeline status
- 💻 Create coding assessments
- 📅 Schedule interviews
- ✉️ Generate recruitment communication templates

> **Track:** Option A1 — *Indian Tech Recruitment Specialist*

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Core Language | Python |
| NLP / Skill Extraction | spaCy |
| AI/LLM Workflow | LangChain |
| Dashboard | Streamlit |
| PDF Parsing | pypdf |
| DOCX Parsing | python-docx |
| Database | SQLite |
| Assessments | HackerEarth Integration Layer |
| Communication | Mock Email Service |
| Version Control | Git / GitHub |

---

## 📁 Project Structure

```
ai_recruitment_assistant/
│
├── backend/
│   ├── __init__.py
│   │
│   ├── resume_parser/
│   │   ├── __init__.py
│   │   ├── extractor.py
│   │   ├── keyword_extractor.py
│   │   └── parser.py
│   │
│   ├── matching/
│   │   ├── __init__.py
│   │   ├── matcher.py
│   │   └── ranking.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   ├── scheduling/
│   │   ├── __init__.py
│   │   └── scheduler.py
│   │
│   ├── communication/
│   │   ├── __init__.py
│   │   └── templates.py
│   │
│   └── integrations/
│       ├── __init__.py
│       ├── assessment_tool.py
│       ├── hackerearth.py
│       └── email_tool.py
│
├── frontend/
│   └── app.py
│
├── tests/
│   ├── __init__.py
│   ├── test_parser.py
│   ├── test_extractor.py
│   ├── test_keywords.py
│   ├── test_matching.py
│   ├── test_ranking.py
│   ├── test_database.py
│   ├── test_scheduling.py
│   ├── test_communication.py
│   ├── test_assessment_tool.py
│   ├── test_hackerearth.py
│   └── test_pipeline.py
│
├── recruitment.db
├── Sonu_Raj_Resume.pdf
├── README.md
└── .gitignore
```

---

## 🚀 Getting Started

```bash
# Clone the repository
git clone <your-repo-url>
cd ai_recruitment_assistant

# Install dependencies
pip install spacy langchain streamlit pypdf python-docx

# Download the spaCy English model
python -m spacy download en_core_web_sm

# Run the Streamlit dashboard
streamlit run frontend/app.py
```

---

## 🧭 Workflow

```
Upload Resume
      ↓
Enter Job Description
      ↓
Analyze Candidate
      ↓
View Screening Result
      ↓
Rank & Manage Pipeline
```

---

## 📅 Development Timeline

### Week 1–2

- ✅ GitHub repository & project structure
- ✅ Development environment (Python, spaCy, LangChain, Streamlit, pypdf, python-docx, SQLite)
- ✅ spaCy `en_core_web_sm` model configured
- ✅ Basic resume screening chatbot (Streamlit)
- ✅ Resume parsing (PDF & DOCX) — extracts name, email, phone, resume text, skills
- ✅ Technical skill keyword extraction (Python, Java, SQL, ML, FastAPI, React, JavaScript, Git, Docker, AWS, TensorFlow, PyTorch)
- ✅ Candidate scoring against job requirements
- ✅ SQLite candidate database (`recruitment.db`)
- ✅ Streamlit recruiter dashboard
- ⏳ Streamlit Cloud deployment
- ⏳ 2-minute demo video

**Match Score Formula**

```
Match Score = (Matched Required Skills / Total Required Skills) × 100
```

**Example**

| | Skills |
|---|---|
| Required | Python, SQL, Machine Learning, Git, FastAPI |
| Candidate | Python, SQL, Machine Learning, Git |
| Matched | Python, SQL, Machine Learning, Git |
| Missing | FastAPI |
| **Match Score** | **80%** |

### Week 3–4

- ✅ Candidate ranking algorithm (highest match score → highest rank)
- ✅ Job requirement extraction and matching (Required / Matched / Missing skills + score)
- ✅ Interview scheduling (candidate name, email, date, time, type — Online / In-person / Phone)
- ✅ PDF and DOCX resume support, fully tested
- ✅ Communication templates: Interview Invitation, Shortlist, Rejection, Interview Reminder

**Example Ranking**

```
Rank 1: Candidate B - 95%
Rank 2: Candidate C - 84%
Rank 3: Candidate A - 72%
```

### Week 5–6 — Option A1: Indian Tech Recruitment Specialist

- ✅ HackerEarth assessment integration layer (mock — see note below)
- ✅ SQLite candidate pipeline management (Applied → Shortlisted → Assessment → Interview → Selected/Rejected)
- ⏳ Indian tech-specific skill matching
- ⏳ Notice period & salary expectations
- ⏳ Indian education recognition
- ⏳ Regional preferences & relocation

**HackerEarth Integration Example**

```
Candidate: Sonu Raj
Email: sonu@example.com
Job Role: Python Developer
Assessment ID: HE-SONURAJ
Status: Created
Platform: HackerEarth
```

> **Note:** The current HackerEarth integration is a **mock layer**, since live API credentials/access have not yet been configured. It is structured so a real API connection can be dropped in later without changing the calling code.

**Pipeline Example**

```
Applied → Shortlisted

Candidate: Pipeline Test Candidate
Score: 85.0
Status: Shortlisted
```


