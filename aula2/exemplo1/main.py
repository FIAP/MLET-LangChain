from langchain.document_loaders import PyPDFLoader

caminho_pdf = "guia-pratico-de-typescript-melhore-suas-aplicacoes-javascript.pdf"

loader = PyPDFLoader(caminho_pdf)

documentos = loader.load()

#print(f"Número de documentos carregados: {len(documentos)}")

for i, documento in enumerate(documentos):
    print(f"\nConteúdo da página {i + 1}:")
    print(documento.page_content)  