from langchain_community.document_loaders import PyPDFLoader
from langchain_classic.text_splitter import CharacterTextSplitter
loader = PyPDFLoader('Death_Note _pdf.pdf')
documents = loader.load()
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator=''
)
result = splitter.split_documents(documents)#this carries alist of document objects
print(result[0]) #this in itself is a document object
print(result[0].page_content)