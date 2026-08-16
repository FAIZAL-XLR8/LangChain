from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
load_dotenv()
llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation")
chat_model = ChatHuggingFace(llm=llm)
#we define a class of typedDict for the specific kind of strcture o/p we need
from typing import TypedDict
#this is the schema
class structure_format(TypedDict):
    summary:str
    sentiment:str
#we defined it
structured_model = chat_model.with_structured_output(structure_format)
response = structured_model.invoke(""" The hardware is great but the software feels bloated.there are too many pre-installed apps that I cant remove.Also the UI looks outdated compared to other brands   """)
print(response)
print(response['summary'])
print(response['sentiment'])