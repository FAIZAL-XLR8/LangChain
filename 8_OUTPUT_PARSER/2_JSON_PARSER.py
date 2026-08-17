from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
chat_model = ChatHuggingFace(llm = llm)
parser = JsonOutputParser()
prompt1 = PromptTemplate(
    template="Write a detailed summary about {topic}\n {format_instruction}",
    input_variables=['topic'],
    partial_variables={"format_instruction" : parser.get_format_instructions()}

)
chain = prompt1 | chat_model
result = chain.invoke({"topic":"Blach_hole"})
#
print(parser.parse(result.content))


