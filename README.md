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

## 📋 Table of Contents
- [Overview](#-overview)
- [About This Project](#-about-this-project)
- [System Architecture](#-system-architecture)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Quick Start](#-quick-start)
- [Environment Configuration](#-environment-configuration)
- [Project Structure](#-project-structure)
- [Usage Guide](#-usage-guide)
- [Performance](#-performance-internal-testing)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
- [License](#-license)
- [Author](#-author)
- [Acknowledgments](#-acknowledgments)

---

## 🌟 Overview

Career Readiness Mentor and Skill Gap Navigator is an AI-powered career assistance platform that helps users:

- Improve resume quality
- Identify skill gaps
- Prepare for interviews
- Generate cover letters and emails
- Get personalized career guidance

The system is built using modern GenAI architecture with multiple specialized agents orchestrated using LangChain and Retrieval-Augmented Generation (RAG).

### 📊 Key Metrics

<div align="center">

| Metric | Value | Description |
|:------:|:-----:|:------------|
| ⚡ Speed | ~30s | Full workflow completion time |
| 🎯 ATS Score | ~90% | Target ATS compatibility (internal testing) |
| 📈 Accuracy | 95%+ | PDF extraction success rate |
| 🤖 Agents | 7 | Specialized AI agents |

</div>

*Metrics are based on internal testing and heuristic evaluation.*

## 🎯 Who Is This For?

- Students preparing for placements
- Fresh graduates and job seekers
- Professionals switching roles
- Anyone seeking AI-assisted career guidance

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
  → Improves ATS compatibility
  → Injects job-specific keywords

- **💌 Cover Letter Agent**
  → Generates personalized cover letters
  → Aligns tone with role and company

- **🎯 Interview Preparation Agent**
  → Generates STAR-based Q&A
  → Focuses on role-specific scenarios

- **🧠 Skill Gap Analyzer**
  → Compares resume skills with job requirements
  → Suggests learning roadmap

- **🔗 LinkedIn Optimizer**
  → Improves headline and About section
  → Enhances recruiter visibility

- **✉️ Email Generator**
  → Creates professional follow-up and outreach emails

- **🗣️ Career Coach Agent**
  → Provides conversational career guidance
  → Maintains session context

---

## 🚀 Features

<div align="center">

| 📄 **Resume Optimization** | 🎯 **Interview Prep** | 🧠 **Skill Gap Analysis** |
|:-------------------------:|:--------------------:|:------------------------:|
| ATS-friendly structure | STAR framework Q&A | Gap identification |
| Keyword injection | Role-specific scenarios | Learning roadmap |
| 92%+ ATS score | Confidence building | Course recommendations |

</div>

<div align="center">

| 🔗 **LinkedIn Optimization** | ✉️ **Email Templates** | 💬 **AI Career Coach** |
|:---------------------------:|:----------------------:|:---------------------:|
| Profile enhancement | Professional emails | Conversational guidance |
| Headline optimization | Follow-ups & outreach | Context-aware responses |
| Recruiter visibility | Thank you notes | Memory retention |

</div>

---

## 🛠️ Technology Stack

### 🤖 AI / ML
<div align="center">

![Groq](https://img.shields.io/badge/Groq-LLaMA%203-black) 
![LangChain](https://img.shields.io/badge/LangChain-Framework-blue) 
![RAG](https://img.shields.io/badge/RAG-Context%20Retrieval-purple) 
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20DB-orange) 
![SentenceTransformers](https://img.shields.io/badge/Sentence%20Transformers-Embeddings-green)

</div>

### ⚙️ Backend
<div align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue) 
![Architecture](https://img.shields.io/badge/Architecture-Multi--Agent-yellow) 
![Prompt](https://img.shields.io/badge/Prompt%20Engineering-Optimized-lightgrey)

</div>

### 🎨 Frontend
<div align="center">

![Streamlit](https://img.shields.io/badge/Streamlit-UI-red) 
![CSS](https://img.shields.io/badge/CSS-Custom-blueviolet) 
![Plotly](https://img.shields.io/badge/Plotly-Visualization-darkblue)

</div>

### 📊 Data Processing
<div align="center">

![Pandas](https://img.shields.io/badge/Pandas-Data-orange) 
![PDF](https://img.shields.io/badge/PDF-Parsing-red) 
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web%20Scraping-green)

</div>

### 📄 Export
<div align="center">

![ReportLab](https://img.shields.io/badge/ReportLab-PDF-blue) 
![CSV](https://img.shields.io/badge/Export-TXT%20%7C%20CSV-lightgrey)

</div>

---

## 🚀 Quick Start

### 📋 Prerequisites

<div align="center">

| Requirement | Version | Download / Get |
|:------------|:--------|:---------------|
| **Python** | 3.11+ | [python.org](https://www.python.org/downloads/) |
| **Groq API Key** | Free tier | [console.groq.com](https://console.groq.com/keys) |
| **Git** | Latest | [git-scm.com](https://git-scm.com/downloads) |

</div>

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

<div align="center">

| Operation | Time | Status |
|:----------|:-----|:-------|
| 📄 **PDF Extraction** | < 2 seconds | ✅ Optimized |
| 🧾 **Resume Optimization** | 8-12 seconds | ✅ Fast |
| ✉️ **Cover Letter** | 6-8 seconds | ✅ Quick |
| 🎯 **Interview Prep** | 10-15 seconds | ✅ Efficient |
| **⚡ Total Processing** | **~30 seconds** | **✅ Stable (Demo / Portfolio)** |

</div>

Metrics are based on internal testing and demo usage.

> This application is intended for educational and portfolio use.

---

## 📈 Roadmap

<div align="center">

| Category | Planned Features |
|:---------|:-----------------|
| 🔐 **User Features** | Authentication • Profile management • Preferences |
| 🔗 **Integrations** | LinkedIn API • Naukri • Indeed • Job boards |
| 🌐 **Localization** | Hindi • Tamil • Telugu • Multi-language support |
| 📱 **Mobile** | React Native app • iOS • Android |
| 🎥 **Advanced** | Video interview prep • Speech analysis • Salary negotiator |
| 🏢 **Enterprise** | Company culture analysis • Team collaboration |

</div>

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

<div align="center">

### Jagan B

| ECE Graduate | AI Enthusiast |

[![GitHub](https://img.shields.io/badge/GitHub-JAGANBALUSAMY-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JAGANBALUSAMY)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jagan-b-1aa945323)
[![Email](https://img.shields.io/badge/Email-Contact-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:jaganbalusamy@gmail.com)

</div>

---

## 🙏 Acknowledgments

<div align="center">

| Organization | Contribution |
|:-------------|:-------------|
| **Groq AI** | Fast LLM capabilities and generous API access |
| **Streamlit** | Excellent web framework for rapid development |
| **LangChain** | AI orchestration tools and agent frameworks |
| **Open Source Community** | Libraries, tools, and continuous support |

</div>

---

<div align="center">

### ⭐ Star this repository if you find it useful!

**Built by Jagan B**

[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jagan-b-1aa945323)

</div>