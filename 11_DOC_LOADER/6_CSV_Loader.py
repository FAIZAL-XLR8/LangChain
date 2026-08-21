from langchain_community.document_loaders import CSVLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct",
                          task='text-generation')
model = ChatHuggingFace(llm = llm)

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

loader = CSVLoader('path')

docs = loader.load() #returns a list of doc object where each doc obj represnts one row of the whole csv like harr row ek doc object hai
#docs = loader.lazy_load() this too shall work


chain = prompt | model | parser

print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))