from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
document = ["alpha is the new beta",
"beta is the new alpha"]
model_obj = OpenAIEmbeddings(model='')
vector_embedding = model_obj.embed_documents(document)
print(str(vector_embedding))
