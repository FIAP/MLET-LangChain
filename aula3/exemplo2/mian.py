from langchain_community.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(api_key=api_key)

prompt = """
Você é um consultor financeiro com foco em investimentos de longo prazo.
Seu cliente é um homem de 39 anos, com baixa tolerância ao risco, que pode investir 10.000 reais por mês 
e já possui 130 mil reais em ações de renda fixa.

Desenvolva um plano de investimento detalhado para este cliente, recomendando tipos de ativos, 
proporções de alocação e estratégias de diversificação. 
O plano deve priorizar a preservação do capital e garantir um crescimento moderado ao longo do tempo.
"""

response = llm.invoke(prompt)

print("Plano de Investimento Gerado:\n")
print(response)
