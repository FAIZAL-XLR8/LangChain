from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(repo_id='meta-llama/Llama-3.1-8B-Instruct', task='text-generation', max_new_tokens=100, temperature=1.0)
chat_model = ChatHuggingFace(llm = llm)
while True:
    user_input = input("You: ")
    if user_input == 'exit' :
        break
    response = chat_model.invoke(user_input)
    print(response.content)
else:
    print("Loop over!")
