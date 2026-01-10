"""Resume Optimization & ATS Scoring Agents"""

import httpx
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from config.settings import settings


class AtsScoringAgent:
    """
    Agent responsible for calculating ATS score
    using keyword overlap between resume and job description.
    """

    def calculate(self, resume: str, job_description: str) -> float:
        resume_words = set(resume.lower().split())
        jd_words = set(job_description.lower().split())

        if not jd_words:
            return 0.0

        match = len(resume_words.intersection(jd_words))
        score = min((match / len(jd_words)) * 100, 95)

        return round(score, 1)


class ResumeOptimizerAgent:
    """
    AI agent for optimizing resumes and
    coordinating ATS scoring.
    """

    def __init__(self):
        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_NAME,
            temperature=0.4,
            http_client=httpx.Client(trust_env=False)
        )

        self.ats_agent = AtsScoringAgent()

        self.prompt_template = PromptTemplate(
            input_variables=["resume", "job_description"],
            template="""You are an expert ATS resume optimizer.

**Candidate Resume:**
{resume}

**Job Description:**
{job_description}

**Task:** Optimize the resume to maximize ATS score by:
1. Highlighting skills matching the JD
2. Quantifying achievements (X% improvement, $Y saved, Z projects)
3. Using ATS-friendly keywords naturally
4. Formatting with clear sections and bullet points
5. Maintaining 100% truthful information

**Output Format:**

## PROFESSIONAL SUMMARY
[2-3 lines with key skills and achievements]

## CORE COMPETENCIES
• [Skill 1] • [Skill 2] • [Skill 3] • [Skill 4]

## PROFESSIONAL EXPERIENCE
**[Job Title]** | [Company] | [Dates]
• [Achievement with metrics]
• [Achievement with metrics]

## TECHNICAL SKILLS
[Programming Languages, Frameworks, Tools]

## EDUCATION
[Degree] | [Institution] | [Year]

## PROJECTS
**[Project Name]** | [Tech Stack]
• [Achievement with metrics]

Generate optimized resume:"""
        )

    def optimize(self, resume_text: str, job_description: str):
        """
        Optimize resume and calculate ATS score.
        """

        formatted_prompt = self.prompt_template.format(
            resume=resume_text,
            job_description=job_description
        )

        optimized_resume = self.llm.invoke(formatted_prompt).content

        ats_score = self.ats_agent.calculate(
            optimized_resume, job_description
        )

        return {
            "optimized_resume": optimized_resume,
            "ats_score": ats_score
        }
