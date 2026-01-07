"""Cover letter generation agent."""
import httpx
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from config.settings import settings

class CoverLetterAgent:
    """AI agent for cover letter generation."""
    
    def __init__(self):
        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_NAME,
            temperature=0.4,
            http_client=httpx.Client(trust_env=False)
        )
        
        self.prompt_template = PromptTemplate(
            input_variables=["resume", "job_description", "company", "role"],
            template="""Write a professional cover letter (300-400 words).

**Resume:** {resume}

**Job Description:** {job_description}

**Company:** {company}
**Role:** {role}

**Structure:**
1. Opening: Express genuine interest in role and company
2. Body: Connect top 3 skills to JD requirements with specific achievements
3. Closing: Strong call-to-action for interview

**Tone:** Professional, confident, enthusiastic

Generate the cover letter:"""
        )
    
    def generate(self, resume_text: str, job_description: str, company: str, role: str):
        """Generate tailored cover letter."""
        
        prompt = f"""Write a professional cover letter (300-400 words).

**Resume:** {resume_text}

**Job Description:** {job_description}

**Company:** {company}
**Role:** {role}

**Structure:**
1. Opening: Express genuine interest in role and company
2. Body: Connect top 3 skills to JD requirements with specific achievements
3. Closing: Strong call-to-action for interview

**Tone:** Professional, confident, enthusiastic

Generate the cover letter:"""
        
        formatted_prompt = self.prompt_template.format(
            resume=resume_text,
            job_description=job_description,
            company=company,
            role=role
        )
        result = self.llm.invoke(formatted_prompt).content
        return result
