from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
from  sklearn.metrics.pairwise import cosine_similarity
import numpy as np
document = [ "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."]
query = "who is virat kohli"
model_obj = OpenAIEmbeddings(model='')

doc_embedding = model_obj.embed_documents(document)
query_embedding = model_obj.embed_query(query)
list_of_similarity = cosine_similarity([query_embedding], doc_embedding)[0] 
idx, score = list(enumerate(list_of_similarity), key = lambda x : (-x[1]))
print(score, document[idx])
"""
rom langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)

scores = cosine_similarity([query_embedding], doc_embeddings)[0] #scores returns a 2d vector
#cosine_simialrity needs a 2d query vector and a 2d document stored vectors

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
#Enumerate  takes an iterable and returns pairs of (index, value), optionally starting the index count from a custom number:

print(query)
print(documents[index])
print("similarity score is:", score)
"""


