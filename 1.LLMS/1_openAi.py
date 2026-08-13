from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv() #this helps to load all the env variables

#this is the old llm model not the curr
#chat model thing
llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke("send any ques to the model from here")
print(result)