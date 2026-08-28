from langchain_community.tools import tool
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
@tool
def add (a:int, b:int) -> int :
    """Add two numbers"""
    return a + b
llm = HuggingFaceEndpoint(repo_id='deepseek-ai/DeepSeek-V4-Pro', task='text-generation')
chat_model = ChatHuggingFace(llm=llm)
tooled_chat = chat_model.bind_tools([add])
res = tooled_chat.invoke('add 4 with 4')
print(res)
