import os
import json
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def carregar_documentos(caminho_arquivo):
    loader = PyPDFLoader(caminho_arquivo)
    return loader.load_and_split()

def limpar_e_extrair_informacoes(documentos):
    informacoes_extraidas = []
    for doc in documentos:
        linhas = doc.page_content.strip().split("\n")
        informacoes = {linha.split(":")[0].strip().replace(" ", "-"): linha.split(":")[1].strip() 
                       for linha in linhas if ":" in linha}
        informacoes_extraidas.append(informacoes)
    return informacoes_extraidas

def criar_chain_sequencial():
    prompt_template_analise = PromptTemplate(
        input_variables=["input"],
        template="Avalie o currículo fornecido e forneça uma análise resumida: {input}"
    )
    
    llm_analise_curriculo = Ollama(
        model="llama3.1", num_gpu=0, callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
    )
    
    prompt_template_rh = PromptTemplate(
        input_variables=["input"],
        template="""
        De acordo com a análise do currículo fornecido:
        {input}
        O candidato tem perfil tecnico para uma vaga de tech lead?.
        """
    )
    
    llm_analise_rh = ChatOpenAI(model='gpt-4-turbo', api_key=os.getenv("OPENAI_API_KEY"))
    
    return prompt_template_analise | llm_analise_curriculo | prompt_template_rh | llm_analise_rh

def main(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"O arquivo {caminho_arquivo} não foi encontrado.")
    
    documentos = carregar_documentos(caminho_arquivo)
    informacoes_extraidas = limpar_e_extrair_informacoes(documentos)
    informacoes_json = json.dumps(informacoes_extraidas, indent=4, ensure_ascii=False)

    chain_sequencial = criar_chain_sequencial()
    
    resultado_final = chain_sequencial.invoke({"input": informacoes_json})
    
    # Imprimir apenas a resposta formatada da análise
    print("Resposta da análise:\n")
    print(resultado_final.content)

# Executar a função principal
if __name__ == "__main__":
    caminho_arquivo = "profile.pdf"
    main(caminho_arquivo)