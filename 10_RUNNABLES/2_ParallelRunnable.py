from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_classic.schema.runnable import RunnableParallel,RunnableSequence
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
chat_model = ChatHuggingFace(llm=llm)
parser = StrOutputParser()
prompt = PromptTemplate(
    template="Make a twitter post about topic {topic}",
    input_variables=['topic'],
   
)
prompt2 = PromptTemplate(
    template='Make a LinkedIN post about  this topic--> {topic}',
    input_variables=['topic']
)
prompt3 = PromptTemplate (
  template='Analyse the twitter post {twitter} and the LinkedIn post {post} and summarise the two into 5 lines',
  input_variables=['twitter', 'post']
 )
chain1 = RunnableParallel(
    {
        'twitter' : RunnableSequence(prompt, chat_model, parser),
        'post' : RunnableSequence(prompt2, chat_model, parser)
    }
)
result2 = chain1.invoke({'topic' : "AI/LLMS in era of tommorow"})
print(result2['twitter'])
print(result2['post'])
chain2 = RunnableSequence(chain1, prompt3, chat_model, parser)
result = chain2.invoke({'topic' : "Data Structures and algorithm"})
print(result)


