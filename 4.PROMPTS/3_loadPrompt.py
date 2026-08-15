from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(repo_id = 'meta-llama/Llama-3.1-8B-Instruct', task = 'text-generation')
chat_model = ChatHuggingFace(llm = llm) 
loaded_prompt = load_prompt('template.json')
final_prompt = loaded_prompt.invoke({'name':'Sasuke Uchiha'})
result = chat_model.invoke(final_prompt)
print(result.content)
