import openai
from src.config import API_KEY, BASE_URL

class OpenAIClient:
    """
    Singleton class for OpenAI client.
    """
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = openai.Client(
                api_key=API_KEY,
                base_url=BASE_URL,
            )
        return cls._instance
