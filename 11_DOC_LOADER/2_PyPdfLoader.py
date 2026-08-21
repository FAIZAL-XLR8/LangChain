from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_community.document_loaders import PyPDFLoader
loader = PyPDFLoader('Death_Note_pdf.pdf') #created a loader object
list_docs = loader.load() #each page of the pdf is an document object
#so a list of document objects and total number of objects = page_number
print(list_docs)