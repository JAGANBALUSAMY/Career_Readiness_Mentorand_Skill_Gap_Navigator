"""Email Follow-up Generator Agent."""
import httpx
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from config.settings import settings

class EmailAgent:
    """AI agent for email generation."""
    
    def __init__(self):
        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_NAME,
            temperature=0.4,
            http_client=httpx.Client(trust_env=False)
        )
        
        self.followup_prompt = PromptTemplate(
            input_variables=["company", "role", "days_since"],
            template="""Write a professional follow-up email.

**Company:** {company}
**Role:** {role}
**Days Since Application:** {days_since}

**Requirements:**
- Professional but warm tone
- 100-150 words
- Reiterate interest
- Add value (mention recent company news if generic)
- Clear call-to-action
- Subject line included

Generate follow-up email:"""
        )
        
        self.thank_you_prompt = PromptTemplate(
            input_variables=["company", "role", "interviewer_name"],
            template="""Write a thank you email after interview.

**Company:** {company}
**Role:** {role}
**Interviewer:** {interviewer_name}

**Requirements:**
- Send within 24 hours
- 150-200 words
- Thank them for time
- Reference specific conversation point
- Reiterate fit for role
- Express enthusiasm

Generate thank you email:"""
        )
    
    def generate_followup(self, company: str, role: str, days_since: int = 7):
        """Generate follow-up email."""
        
        formatted_prompt = self.followup_prompt.format(
            company=company,
            role=role,
            days_since=days_since
        )
        result = self.llm.invoke(formatted_prompt).content
        return result
    
    def generate_thank_you(self, company: str, role: str, interviewer_name: str):
        """Generate thank you email after interview."""
        
        prompt = f"""Write a thank you email after interview.

**Company:** {company}
**Role:** {role}
**Interviewer:** {interviewer_name}

**Requirements:**
- Send within 24 hours
- 150-200 words
- Thank them for time
- Reference specific conversation point
- Reiterate fit for role
- Express enthusiasm

Generate thank you email:"""
        
        formatted_prompt = self.thank_you_prompt.format(
            company=company,
            role=role,
            interviewer_name=interviewer_name
        )
        result = self.llm.invoke(formatted_prompt).content
        return result
