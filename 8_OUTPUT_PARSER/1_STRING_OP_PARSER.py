from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
chat_model = ChatHuggingFace(llm = llm)
prompt1 = PromptTemplate(
    template="Write a detailed summary about {topic}",
    input_variables=['text']
)
prompt2 = PromptTemplate(
    template='Give me a 5 line summary of the text /n {text}',
    input_variables=['text']
)
str_parser = StrOutputParser()
chain = prompt1 | chat_model | str_parser | prompt2 | chat_model | str_parser
result = chain.invoke({"topic" : "Blackhole"})
print(result)