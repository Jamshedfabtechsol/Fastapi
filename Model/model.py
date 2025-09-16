# model.py

from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Model:

    def model(self, prompt, query):

        response = client.responses.create(
        model="gpt-4o-mini",
        input=[
        {"role": "system", "content": prompt},
        {"role": "user", "content": query}
        ]
        )
        
        return response.output_text

