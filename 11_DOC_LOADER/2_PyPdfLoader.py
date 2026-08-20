from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('Death_Note_pdf.pdf') #created a loader object
list_docs = loader.load()
print(list_docs)