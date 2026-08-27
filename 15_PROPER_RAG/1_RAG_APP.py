#the pipeline woill be in such a way that we know retirever is a runnable 
# and we will mke a chain where we will feed ques and docs both to LLM using parallelRunnable then connect in series with a swquential Runnable to get the answer
from langchain_classic.document_loaders import PyPDFLoader
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace,HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_classic.schema.runnable import RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_classic.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv() 
loader = PyPDFLoader('Death_Note _pdf.pdf')
document = loader.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=30
)
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    provider="featherless-ai",
)
chat_model = ChatHuggingFace(llm=llm)
doc_list = splitter.split_documents(documents=document)
embeddings=  HuggingFaceEmbeddings()
vector_store = Chroma.from_documents( #.from_docs se it can make embeddings and store directly
documents=doc_list,
embedding=embeddings,
collection_name='my_collection1'
)
retriever = vector_store.as_retriever(search_type='similarity',search_kwargs={'k':3})
user_query = input('input ur querey uh wizard')
def my_func(query):
    docs = retriever.invoke(query)
    return "\n\n".join(item.page_content for item in docs)
parser = StrOutputParser()
prompt = PromptTemplate(
    template='You are a helpful assistant.Answer the following user query {query} using the following context {context}',
    input_variables=['query','context']
)
chain1 = RunnableParallel(
    {
        'query' : RunnablePassthrough(),
        'context' : RunnableLambda(my_func) 
    }
)
chain2 = prompt | chat_model | parser
chain = chain1 | chain2

result = chain.invoke('who was Kira')
print(result)