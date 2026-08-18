from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_classic.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
from dotenv import load_dotenv
load_dotenv()
#to create a parallel chain we use parallel runnables 
from langchain_core.runnables import RunnableBranch,RunnableLambda
llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)

chat_model1 = ChatHuggingFace(llm=llm1)

string_parser = StrOutputParser()
class Feedback(BaseModel):
    sentiment: Literal['positive', 'negative'] = Field(description="Write the sentiment in positive or negative")
parser = PydanticOutputParser(pydantic_object=Feedback)
prompt = PromptTemplate(
    template="Write down the sentiment of the feedback{feedback}\n {format_instruction}",
    input_variables=['feedback'],
    partial_variables={"format_instruction" : parser.get_format_instructions()}
)
specifier_chain = prompt | chat_model1 | parser
#the above chain will decide the output in form of json-->sentiment : 'positive' / 'negative'
result = specifier_chain.invoke({"feedback" : "This is a ugly smartphone"})
#print(result)
prompt2 = PromptTemplate(
    template="Write an appropriate response to the feedback{feedback}",
    input_variables=['feedback']
)
prompt3=PromptTemplate(
    template='Write an appropriate response to the feedback{feedback}\n',
    input_variables=['feedback']
)
"""now the if/elseif/elseif/default branches are made by RUnnableBranch --> take tuple of tuples--> 2d tuple
branch_chain = RunnableBranch(
    (condition,chain),
    (condtion,chain),
    default chain

)
"""
#conceptually we wanna make feedback --> sentiment:posiitve will be input to branch chain
branch_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive', prompt2 | chat_model1 | string_parser),
    (lambda x : x.sentiment == 'negative', prompt3 | chat_model1 | string_parser),
    RunnableLambda(lambda x : "couldnt convert")
)
final_chain = specifier_chain | branch_chain
result = final_chain.invoke({"feedback" : "This is a terrible smartphone"})
print(result)