from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
chat_model = ChatGoogleGenerativeAI(model="gemini-3.6-flash")
result = chat_model.invoke("who was nushrat fateh ali khan")
print(result.content[0]["text"])