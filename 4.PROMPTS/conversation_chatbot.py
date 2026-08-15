from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
llm = HuggingFaceEndpoint(repo_id='meta-llama/Llama-3.1-8B-Instruct', temperature=1.0, max_new_tokens=100)
load_dotenv()
chat_history =[
    SystemMessage(content='You are an hardcor   e anime  watcher who knows every anime in history')
]
chat_model = ChatHuggingFace(llm=llm)
while True:
    user_input = input('')
    chat_history.append(HumanMessage(content=user_input))
    if user_input =='exit' :
         break
    response = chat_model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print(response.content)

print(chat_history)