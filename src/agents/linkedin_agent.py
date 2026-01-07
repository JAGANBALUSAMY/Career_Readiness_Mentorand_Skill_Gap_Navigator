"""LinkedIn Profile Optimization Agent."""
import httpx
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from config.settings import settings

class LinkedInAgent:
    """AI agent for LinkedIn profile optimization."""
    
    def __init__(self):
        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_NAME,
            temperature=0.4,
            http_client=httpx.Client(trust_env=False)
        )
        
        self.about_prompt = PromptTemplate(
            input_variables=["resume", "target_role"],
            template="""Write a compelling LinkedIn "About" section.

**Resume:** {resume}

**Target Role:** {target_role}

**Requirements:**
- 150-200 words
- First-person narrative
- Hook in first line
- Highlight unique value proposition
- Include 3-4 key achievements with metrics
- End with call-to-action
- SEO-optimized with industry keywords

Generate LinkedIn About section:"""
        )
        
        self.headline_prompt = PromptTemplate(
            input_variables=["resume", "target_role"],
            template="""Create a powerful LinkedIn headline (max 220 characters).

**Resume:** {resume}
**Target Role:** {target_role}

Format: [Current Role] | [Key Skill 1] | [Key Skill 2] | [Unique Value]

Generate 3 headline options:"""
        )
    
    def generate_about_section(self, resume_text: str, target_role: str):
        """Generate LinkedIn About section."""
        
        formatted_prompt = self.about_prompt.format(
            resume=resume_text,
            target_role=target_role
        )
        result = self.llm.invoke(formatted_prompt).content
        return result
    
    def generate_headline(self, resume_text: str, target_role: str):
        """Generate LinkedIn headline."""
        
        prompt = f"""Create a powerful LinkedIn headline (max 220 characters).

**Resume:** {resume_text}
**Target Role:** {target_role}

Format: [Current Role] | [Key Skill 1] | [Key Skill 2] | [Unique Value]

Generate 3 headline options:"""
        
        formatted_prompt = self.headline_prompt.format(
            resume=resume_text,
            target_role=target_role
        )
        result = self.llm.invoke(formatted_prompt).content
        return result
