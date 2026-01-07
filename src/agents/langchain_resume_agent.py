"""LangChain-powered Resume Optimizer."""
import httpx
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config.settings import settings

class LangChainResumeAgent:
    """Resume optimizer using LangChain."""
    
    def __init__(self):
        """Initialize LangChain components."""
        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_NAME,
            temperature=settings.TEMPERATURE,
            http_client=httpx.Client(trust_env=False)
        )
        
        self.prompt = PromptTemplate(
            input_variables=["resume", "jd"],
            template="""You are an expert ATS resume optimizer.

Resume:
{resume}

Job Description:
{jd}

Optimize the resume for ATS compatibility. Include clear sections, quantified achievements, and keywords from the job description.

Generate optimized resume:"""
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)
    
    def optimize(self, resume_text: str, job_description: str):
        """Optimize resume."""
        result = self.chain.run(resume=resume_text, jd=job_description)
        
        ats_score = self._calculate_ats_score(result, job_description)
        
        return {
            'optimized_resume': result,
            'ats_score': ats_score,
            'used_rag': True
        }
    
    def _calculate_ats_score(self, resume: str, jd: str) -> float:
        """Calculate ATS score."""
        resume_words = set(resume.lower().split())
        jd_words = set(jd.lower().split())
        
        if len(jd_words) == 0:
            return 0
        
        match = len(resume_words.intersection(jd_words))
        score = min((match / len(jd_words)) * 100, 95)
        return round(score, 1)
