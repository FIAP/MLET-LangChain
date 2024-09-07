from langchain.document_loaders import CSVLoader

caminho_csv = "exemplo.csv"

loader = CSVLoader(caminho_csv)

documentos = loader.load()

print(f"Número de documentos carregados: {len(documentos)}")

for i, documento in enumerate(documentos):
    print(f"\nConteúdo da linha {i + 1}:")
    print(documento.page_content)
