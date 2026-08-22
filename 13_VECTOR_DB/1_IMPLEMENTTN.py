from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.schema import Document
from langchain_chroma import Chroma
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
loader = TextLoader('Death_Note.txt')
doc = loader.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)
list_ = splitter.split_documents(doc)
for i in range(len(list_)):
    list_[i].metadata["id"] = i
vector_store = Chroma(
    embedding_function=HuggingFaceEmbeddings(),
    persist_directory='chroma_db',
    collection_name='sample'
)
vector_store.add_documents(list_)
#print(vector_store.get(include=['embeddings', 'documents','metadatas']))
#print(vector_store.similarity_search(query='Who was Kira', k = 2))
print(vector_store.similarity_search_with_score(query='Who was Kira', k =2))