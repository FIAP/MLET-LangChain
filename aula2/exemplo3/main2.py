from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    web_path = "https://en.wikipedia.org/wiki/Artificial_intelligence"     
)

docs = []
docs_lazy = loader.lazy_load()

for doc in docs_lazy:
    docs.append(doc)
print(docs[0].page_content[:100])
print(docs[0].metadata)


