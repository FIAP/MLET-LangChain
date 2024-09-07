from langchain_community.document_loaders import WikipediaLoader

docs = WikipediaLoader(query="Cavaleiros do Zodiaco", load_max_docs=2).load()
len(docs)

#print(docs[0].metadata)

print(docs[0].page_content[:400])