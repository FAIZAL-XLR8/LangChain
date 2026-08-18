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
    template="What is the meaning of {topic}\n{format_instruction}"
    input_variables=['topic'],
    partial_variables={'format_instruction' : parser.get_format_}
)