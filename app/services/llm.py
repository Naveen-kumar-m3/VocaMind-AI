import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

class LLMService:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def generate_response(self, user_text: str) -> str:
        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a calm, empathetic assistant."},
                {"role": "user", "content": user_text}
            ]
        )
        return response.choices[0].message.content.strip()
