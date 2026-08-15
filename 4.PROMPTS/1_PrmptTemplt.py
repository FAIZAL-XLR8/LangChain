from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-3.1-8B-Instruct", task="text-generation")
chat_model = ChatHuggingFace(llm=llm)
#create the template for dynamic prompt
query_template = PromptTemplate(
    template = 'Tell me about this anime character : {name}',
    input_variables=['name'],
    validate_template=True
)    
#now we have to fill the values of the placeholder and we do by another template.invoke 
#function
final_prompt = query_template.invoke({'name' : "Naruto"}) #as a form of dic give all the values of the i/p variables
res = chat_model.invoke(final_prompt)
print(res.content)
