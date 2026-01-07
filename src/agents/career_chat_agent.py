"""AI Career Chat Assistant with conversation memory (Groq)."""

import os
import httpx
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from config.settings import settings

load_dotenv()


class CareerChatAgent:
    """AI-powered career advisor chatbot using Groq."""

    def __init__(self):
        # Create Groq LLM client
        self.llm = ChatGroq(
            api_key=settings.GROQ_API_KEY,
            model_name=settings.MODEL_NAME,     # e.g., gpt-oss-120b
            temperature=settings.TEMPERATURE,
            http_client=httpx.Client(trust_env=False),
        )

        # Simple in-memory conversation history
        self.conversation_history = []

    def chat(self, user_message: str, resume_context: str = None) -> str:
        """Chat with the career advisor."""

        # Build system prompt
        system_prompt = """
You are an expert career advisor helping students and job seekers.
Be practical, encouraging, structured, and realistic.
Give examples and steps the user can follow.
Keep responses under 200 words.
Use bullet points when useful.
"""

        # Build conversation content
        conversation = system_prompt

        if resume_context:
            conversation += f"\nUser Background:\n{resume_context}\n"

        if self.conversation_history:
            conversation += "\nConversation History:\n"
            conversation += "\n".join(self.conversation_history[-6:])

        conversation += f"\nUser Question: {user_message}\n"

        # Call Groq LLM
        response = self.llm.invoke(conversation)

        answer = response.content

        # Store conversation memory
        self.conversation_history.append(f"User: {user_message}")
        self.conversation_history.append(f"Assistant: {answer}")

        return answer

    def reset_conversation(self):
        """Clear conversation history."""
        self.conversation_history = []