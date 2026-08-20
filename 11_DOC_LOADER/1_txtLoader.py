from langchain_community.document_loaders import TextLoader

loader = TextLoader("Death_Note.txt", encoding='utf-8') #TextLoader(file_path, encoding = utf-8)
documents = loader.load() #this is loaded as a list of document objects and each object has page_content, metadata 

print(documents[0].metadata)
print(documents[0].page_content)