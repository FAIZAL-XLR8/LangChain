from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_classic.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation"
)
model = ChatHuggingFace(llm = llm)
parser= StrOutputParser()
prompt1 = PromptTemplate(
    template='Name a joke related to {anime} Anime',
    input_variables=['anime']
)
prompt2 = PromptTemplate(
    template='Explain the joke {joke}\n',
    input_variables=['joke']
)
chain1 = RunnableSequence(prompt1, model, parser)
chain2 = RunnableParallel(
    {   
        'explaination' : RunnableSequence(prompt2, model, parser),
        'joke' : RunnablePassthrough()
    })
chain = RunnableSequence(chain1, chain2)
result = chain.invoke({'anime' : 'Death Note'})
print(result)
print (result['explaination'])
print(result['joke']) 

