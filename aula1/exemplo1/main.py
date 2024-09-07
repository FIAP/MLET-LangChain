from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = OpenAI(api_key=api_key)

response = llm.invoke("Explique o conceito de aprendizado por reforço.")

print(response)
