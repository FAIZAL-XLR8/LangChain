from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import  PromptTemplate
from langchain_classic.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
chat_model = ChatHuggingFace(llm = llm)
class Person(BaseModel):
    name:str = Field(description="name of the person")
    age : int = Field(gt=18, description="Age of the person")
    city:str = Field("city of the person")

#mention the name of class within the pydantic_object
parser = PydanticOutputParser(pydantic_object=Person)

prompt1 = PromptTemplate(
    template= "Create a fictional person with the place of {place}\n {format_instruction}",
    input_variables=['place'],
    partial_variables={"format_instruction" : parser.get_format_instructions()}

)

chain = prompt1 | chat_model | parser
response = chain.invoke({"place" : "America"})
print(prompt1)
print(response)