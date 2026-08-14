from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-2b-it",
    task="text-generation",
    provider="featherless-ai",
)
chatmodel = ChatHuggingFace(llm=llm)
result = chatmodel.invoke("Who is Naruto Uzumaki?")
print(result.content)
