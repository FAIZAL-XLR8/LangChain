from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
model_obj = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=20)
embed_vector = model_obj.embed_query("what is the local word of Pig")
res = str(embed_vector)
print(res)
#this prints the result
