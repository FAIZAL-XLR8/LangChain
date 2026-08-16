from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
#messgae placeholder is for fetching data from db and placing it as context btn system instruvction and user query
load_dotenv()
llm = HuggingFaceEndpoint(repo_id='meta-llama/Llama-3.1-8B-Instruct', temperature=0.2)
chat_model = ChatHuggingFace(llm = llm)
user_prompt = ChatPromptTemplate([
    ('system', 'You are a {expert} expert. Recommend something like this {movie}'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('user', '{query}')
])
chat_history = []
with open('4.PROMPTS/history.txt') as f:
    chat_history.append(f.readlines())
    
prompt = user_prompt.invoke({'expert' : 'movie', 'movie' : 'Gone-Girl', 'query' : 'what is the summary of the movie', 'chat_history' :chat_history})
response = chat_model.invoke(prompt)
print(response.content)