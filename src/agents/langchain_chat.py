"""LangChain Chat Agent."""
import httpx
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from config.settings import settings

class LangChainChatAgent:
    """Career advisor with memory."""
    
    def __init__(self):
        """Initialize chat agent."""
        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_NAME,
            temperature=0.7,
            http_client=httpx.Client(trust_env=False)
        )
        
        self.memory = ConversationBufferMemory()
        
        self.chain = ConversationChain(
            llm=self.llm,
            memory=self.memory,
            verbose=False
        )
    
    def chat(self, user_message: str, resume_context: str = None) -> str:
        """Chat with memory."""
        response = self.chain.predict(input=user_message)
        return response
    
    def reset_conversation(self):
        """Clear memory."""
        self.memory.clear()
