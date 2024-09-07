from langchain_community.llms import Ollama

llm = Ollama(model="llama3.1")

response = llm.invoke("Explique o conceito de aprendizado por reforço.")

print(response)
