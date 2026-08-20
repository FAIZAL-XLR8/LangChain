from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_classic.schema.runnable import RunnableParallel,RunnableSequence,RunnablePassthrough,RunnableLambda,RunnableBranch
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
    template='Summarise this joke \n{joke}',
    input_variables=['joke']
)
chain1 = RunnableSequence(prompt1, model, parser)
chain2 = RunnableBranch(
    #syntax : (condition, Runnable)
    #(condtion2, Runnable2)
    #default Runnable at last : RunnableXYZ()
    (lambda x : len(x.split()) > 10, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)
chain = RunnableSequence(chain1, chain2)
result = chain.invoke({'anime':'Rent a Girlfriend'})
print(result)
