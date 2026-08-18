from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import JsonOutputToolsParser
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
chat_model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()
prompt = PromptTemplate(
    template="What is the meaning of {topic} in 2 lines\n",
    input_variables=['topic'],
   
)
chain = prompt | chat_model| parser
#for sequential chains --> use prompt1 | chat_model | parser | prompt2 | chat_model | parser 
result = chain.invoke({"topic" : "anime"})
print(result)
#chains visualed by below statement
chain.get_graph().print_ascii()