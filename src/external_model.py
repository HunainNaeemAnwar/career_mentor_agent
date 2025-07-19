import os
from pathlib import Path
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BASE_URL = os.getenv("BASE_URL")

if not GEMINI_API_KEY or not BASE_URL:
    raise ValueError("GEMINI_API_KEY and BASE_URL must be set in the .env file.")

# Set up OpenAI SDK compatible client
client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url=BASE_URL,
)

# Initialize the OpenAIChatCompletionsModel with the client
MODEL = OpenAIChatCompletionsModel(openai_client=client, model="gemini-2.0-flash")
