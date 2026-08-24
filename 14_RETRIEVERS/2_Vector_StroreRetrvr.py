from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_classic.schema import Document
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter
from langchain_classic.document_loaders import PyPDFLoader
loader = PyPDFLoader('Death_Note _pdf.pdf')
docs = loader.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap=20
)
embedding_model = HuggingFaceEmbeddings()
docs_list = splitter.split_documents(docs) #this is the list of docs after spillting

#below is the inmemory Chroma Db
vector_store = Chroma.from_documents( #.from_docs se it can make embeddings and store directly
documents=docs_list,
embedding=embedding_model,
collection_name='my_collection'
)
#below code makes this vector store a retriver
retriever = vector_store.as_retriever(search_kwargs = {"k" : 2})
query = 'Who was Kira'
results = retriever.invoke(query)
for i, item in enumerate(results):
    print (i, item.page_content)