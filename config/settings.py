"""Configuration with validation."""
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """App configuration for AI Job Assistant (Groq)."""

    # API Key for Groq
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

    # Model name (Grok / GPT-OSS-120B)
    MODEL_NAME = "openai/gpt-oss-120b"

    # Generation settings
    MAX_FILE_SIZE_MB = 10
    TEMPERATURE = 0.4
    MAX_OUTPUT_TOKENS = 3000

    @classmethod
    def validate(cls):
        """Validate configuration."""
        if not cls.GROQ_API_KEY:
            raise ValueError("❌ GROQ_API_KEY not found. Add it to .env file.")
        return True


settings = Settings()