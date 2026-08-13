from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("AI_API_KEY")
AI_MODEL_NAME = os.getenv("AI_MODEL_NAME")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def get_model(model_name: str = None):
    if model_name is None:
        model = ChatOpenAI(
            model=f"{AI_MODEL_NAME}",
            api_key=f"{API_KEY}",
            base_url="https://ai.ltp-contest.com/v1",
            timeout=300,
            max_retries=3
        )
    elif model_name == "OpenAI":
        model = ChatOpenAI(model="gpt-4o-mini")

    return model

