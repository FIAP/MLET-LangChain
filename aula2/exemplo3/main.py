from langchain.document_loaders import WebBaseLoader

url = "https://en.wikipedia.org/wiki/Artificial_intelligence" 

loader = WebBaseLoader(url)

documentos = loader.load()

# print(f"Número de seções carregadas: {len(documentos)}")

for i, documento in enumerate(documentos):
    print(f"\nConteúdo da seção {i + 1}:")
    print(documento.page_content)
