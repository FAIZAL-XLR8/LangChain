from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader,TextLoader
loader = PyPDFLoader('Death_Note _pdf.pdf')
document = loader.lazy_load() #this is of type generator and generates one doc object at a time 
print(type(document))
splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=20,
    
)   
loader2 = TextLoader('Death_Note.txt')
document2 = loader.load()
#result = splitter.split_documents(document)
result2 = splitter.split_text(document2[0].page_content)

print(result2)
#print(result[0].page_content)