from langchain_openai import chat_models
from dotenv import load_dotenv
load_dotenv()
chatmodel = ChatOpenAi(model ='gpt-4', temperature=0.5, max_completion_tokens = 10) #can add high temp for creative ans
result = model.invoke("whta is the model name "
                      )
print(result.content) #this prints the content
