import os
from google import genai

def get_client():
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise EnvironmentError(
            "Please set your GEMINI_API_KEY environment variable.\n"
            "Get an API key from: https://aistudio.google.com/app/apikey\n"
            "Then run: export GEMINI_API_KEY='your-api-key-here'"
        )
    return genai.Client(api_key=api_key)
