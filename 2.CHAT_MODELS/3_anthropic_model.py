from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()
chatmodel = ChatAnthropic(model = 'claude-4.5....')
result = chatmodel.invoke("write ur ques here my man!")
print(result.content)