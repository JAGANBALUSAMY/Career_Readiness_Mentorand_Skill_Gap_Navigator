# 🤖 Career Readiness Mentor and Skill Gap Navigator
<div align="center">

[![Python](https://img.shields.io/badge/Python_3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

### AI-Powered Career Mentorship & Skill Gap Analysis Platform
Multi-Agent Architecture • LangChain • RAG • LLMs

</div>

---

## 🌟 Overview

Career Readiness Mentor and Skill Gap Navigator is an AI-powered career assistance platform that helps users:

- Improve resume quality
- Identify skill gaps
- Prepare for interviews
- Generate cover letters and emails
- Get personalized career guidance

The system is built using modern GenAI architecture with multiple specialized agents orchestrated using LangChain and Retrieval-Augmented Generation (RAG).

## 👨‍💻 About This Project

This project was designed and developed by Jagan B as an independent portfolio and academic project to demonstrate:

- Multi-agent AI system design
- LangChain orchestration
- RAG-based context retrieval
- LLM integration using Groq (LLaMA 3)
- Streamlit-based application development
- End-to-end AI product thinking

This is not a cloned product and not affiliated with any company or program.
It is intended for learning, experimentation, and portfolio demonstration.

---

## 🏗️ System Architecture

### 🔁 High-Level Workflow

1. User uploads or pastes resume and job description
2. Streamlit UI sends input to orchestration layer
3. PDF parser / scraper extracts structured text
4. Multi-agent system processes the data:
   - Resume optimization
   - Skill gap analysis
   - Interview preparation
5. LangChain manages prompts, memory, and execution
6. RAG layer retrieves contextual examples from vector store
7. Groq LLM (LLaMA 3) generates optimized outputs
8. Results are exported as PDF / TXT / CSV
9. Session data is cached for analytics and reuse

### 🤖 Multi-Agent System

The platform uses 7 specialized AI agents:

- **🧾 Resume Optimizer**
  - Improves ATS compatibility
  - Injects job-specific keywords

- **💌 Cover Letter Agent**
  - Generates personalized cover letters
  - Aligns tone with role and company

- **🎯 Interview Preparation Agent**
  - Generates STAR-based Q&A
  - Focuses on role-specific scenarios

- **🧠 Skill Gap Analyzer**
  - Compares resume skills with job requirements
  - Suggests learning roadmap

- **🔗 LinkedIn Optimizer**
  - Improves headline and About section
  - Enhances recruiter visibility

- **✉️ Email Generator**
  - Creates professional follow-up and outreach emails

- **🗣️ Career Coach Agent**
  - Provides conversational career guidance
  - Maintains session context

---

## 🚀 Features

- Resume optimization with ATS-friendly structure
- Skill gap identification with learning suggestions
- Interview preparation using STAR framework
- Personalized cover letter generation
- LinkedIn profile optimization
- Professional email templates
- AI career coaching with conversational memory
- Multi-format export (PDF / TXT / CSV)

---

## 🛠️ Technology Stack

### 🤖 AI / ML
- Groq (LLaMA 3)
- LangChain
- Retrieval-Augmented Generation (RAG)
- ChromaDB
- Sentence Transformers

### ⚙️ Backend
- Python 3.11
- Multi-agent architecture
- Prompt engineering

### 🎨 Frontend
- Streamlit
- Custom CSS
- Plotly

### 📊 Data Processing
- Pandas
- pdfplumber
- PyPDF2
- BeautifulSoup4

### 📄 Export
- ReportLab (PDF generation)
- TXT / CSV export

---

## 🚀 Quick Start

### 📋 Prerequisites

- Python 3.11+
- Groq API key
- Git

### ⚙️ Installation

```bash
git clone https://github.com/JAGANBALUSAMY/Career_Readiness_Mentorand_Skill_Gap_Navigator.git
cd Career_Readiness_Mentorand_Skill_Gap_Navigator

python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux / Mac

pip install -r requirements.txt
streamlit run app.py
```

---

## ⚙️ Environment Configuration

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama3-70b-8192
TEMPERATURE=0.4
```

---

## 📁 Project Structure

```
Career_Readiness_Mentorand_Skill_Gap_Navigator/
│
├── app.py
├── requirements.txt
├── config/
│   └── settings.py
├── src/
│   ├── agents/
│   │   ├── resume_optimizer.py
│   │   ├── cover_letter_agent.py
│   │   ├── interview_agent.py
│   │   ├── skill_gap_agent.py
│   │   ├── linkedin_agent.py
│   │   ├── email_agent.py
│   │   └── career_chat_agent.py
│   ├── utils/
│   │   └── pdf_parser.py
│   └── pdf_exporter.py
└── .streamlit/
    └── config.toml
```

---

## 💡 Usage Guide

1. Upload or paste resume
2. Upload, paste, or scrape job description
3. Enter job details (role, company, location)
4. Select required features
5. Click Generate
6. Review results across tabs
7. Download outputs in required format

---

## 📊 Performance (Internal Testing)

- Resume parsing: < 2 seconds
- Resume optimization: ~8–12 seconds
- Cover letter generation: ~6–8 seconds
- Interview preparation: ~10–15 seconds
- Full workflow: ~30 seconds

Metrics are based on internal testing and demo usage.

---

## 📈 Roadmap

Planned enhancements:

- User authentication and profiles
- Job portal integrations
- Multi-language support
- Mobile application
- Video interview preparation
- Salary negotiation assistant
- Enterprise collaboration features

---

## 🤝 Contributing

This project is open for learning-focused contributions.

```bash
git checkout -b feature/new-feature
git commit -m "Add new feature"
git push origin feature/new-feature
```

---

## 📄 License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

Jagan B

- GitHub: https://github.com/JAGANBALUSAMY
- LinkedIn: https://www.linkedin.com/in/jagan-b-1aa945323
- Email: jaganbalusamy@gmail.com

---

## 🙏 Acknowledgments

- Open-source community
- LangChain documentation
- Streamlit documentation
- Groq API documentation

---

<div align="center">

### ⭐ Star this repository if you find it useful

**Built by Jagan B**

</div>