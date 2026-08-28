from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()
from langchain_classic.tools import tool
llm = HuggingFaceEndpoint(repo_id='deepseek-ai/DeepSeek-V4-Pro', task='text-generation')
chat_model = ChatHuggingFace(llm = llm)

#main imports
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import tool
import requests
search_tool = DuckDuckGoSearchRun()
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic import hub
prompt = hub.pull(
    'hwchase17/react',
    dangerously_pull_public_prompt=True
)  #pulls std react agent prompt
@tool
def fetchWeather(ip : str) -> str :
    url = (f"")
    response = requests.get(url)
    res = response.json()
    return res
#this is agent creation -->agents creates commands for executor to ewxecute
agent = create_react_agent(
    llm=llm,
    tools=[search_tool, fetchWeather],
    prompt=prompt
)
#this is wrapper agentexecutor this will execute commands instructed by agent
agent_exec =AgentExecutor(
    agent=agent,
    tools=[search_tool, fetchWeather],
    verbose=True
) 
res = agent_exec.invoke(
    {"input" : "Whos was Kira in Death Note"}
)
print(res)