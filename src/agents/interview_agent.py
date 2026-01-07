"""Interview preparation agent."""
import httpx
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from config.settings import settings

class InterviewAgent:
    """AI agent for interview preparation."""
    
    def __init__(self):
        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_NAME,
            temperature=0.4,
            http_client=httpx.Client(trust_env=False)
        )
        
        self.prompt_template = PromptTemplate(
            input_variables=["resume", "job_description", "role"],
            template="""Generate 10 interview questions with STAR-format answers.

**Resume:** {resume}

**Job Description:** {job_description}

**Role:** {role}

**Categories:**
- 4 Technical questions
- 4 Behavioral questions
- 2 Situational questions

**Format for each:**

### Question X: [Category]
**Q:** [Question]

**Answer (STAR):**
- **Situation:** [Context]
- **Task:** [Challenge]
- **Action:** [Steps taken]
- **Result:** [Outcome with metrics]

Generate all 10 questions:"""
        )
    
    def generate(self, resume_text: str, job_description: str, role: str):
        """Generate interview questions and answers."""
        
        prompt = f"""Generate 10 interview questions with STAR-format answers.

**Resume:** {resume_text}

**Job Description:** {job_description}

**Role:** {role}

**Categories:**
- 4 Technical questions
- 4 Behavioral questions
- 2 Situational questions

**Format for each:**

### Question X: [Category]
**Q:** [Question]

**Answer (STAR):**
- **Situation:** [Context]
- **Task:** [Challenge]
- **Action:** [Steps taken]
- **Result:** [Outcome with metrics]

Generate all 10 questions:"""
        
        formatted_prompt = self.prompt_template.format(
            resume=resume_text,
            job_description=job_description,
            role=role
        )
        result = self.llm.invoke(formatted_prompt).content
        return result
