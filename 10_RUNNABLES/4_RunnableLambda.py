from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_classic.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda
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
def myFunc(text):
    return len(text.split())
chain1 = RunnableSequence(prompt1, model, parser)
# chain2 = RunnableParallel(
#     {   
#         'word_count' : RunnableLambda(myFunc),
#         'joke' : RunnablePassthrough()
#     })
chain2 = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'word_count' : RunnableLambda(lambda x:len(x.split()))
})
chain = RunnableSequence(chain1, chain2)
result = chain.invoke({'anime' : 'Attack On Titans'})
print (result)
