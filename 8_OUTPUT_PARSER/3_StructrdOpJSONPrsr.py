from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate
from langchain_classic.output_parsers import StructuredOutputParser,ResponseSchema
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
chat_model = ChatHuggingFace(llm = llm)
schema = [
    ResponseSchema(name='Fact1', description='First fact about the topic'),
    ResponseSchema(name='Fact2', description='Second fact about the topic'),
    ResponseSchema(name = 'Fact3', description='Third fact about the topic')
]
parser = StructuredOutputParser.from_response_schemas(schema)
prompt1 = PromptTemplate(
    template= "Write exactly three facts about {topic}. \n {format_instruction}",
    input_variables=['topic'],
    partial_variables={"format_instruction" : parser.get_format_instructions()}

)

chain = prompt1 | chat_model | parser
response = chain.invoke({"topic" : "black hole"})
print(response)