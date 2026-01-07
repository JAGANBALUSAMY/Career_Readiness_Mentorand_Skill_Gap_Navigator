"""Resume optimization agent."""
import httpx
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from config.settings import settings

class ResumeOptimizerAgent:
    """AI agent for resume optimization."""
    
    def __init__(self):
        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_NAME,
            temperature=0.4,
            http_client=httpx.Client(trust_env=False)
        )
        
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
        """Optimize resume for ATS."""
        
        prompt = f"""You are an expert ATS resume optimizer.

**Candidate Resume:**
{resume_text}

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
        
        formatted_prompt = self.prompt_template.format(
            resume=resume_text,
            job_description=job_description
        )
        result = self.llm.invoke(formatted_prompt).content
        
        ats_score = self._calculate_ats_score(result, job_description)
        
        return {
            'optimized_resume': result,
            'ats_score': ats_score
        }
    
    def _calculate_ats_score(self, resume: str, jd: str):
        """Calculate ATS match score."""
        resume_words = set(resume.lower().split())
        jd_words = set(jd.lower().split())
        
        if len(jd_words) == 0:
            return 0
        
        match = len(resume_words.intersection(jd_words))
        score = min((match / len(jd_words)) * 100, 95)
        return round(score, 1)
