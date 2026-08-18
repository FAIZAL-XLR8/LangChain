from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
#to create a parallel chain we use parallel runnables 
from langchain_core.runnables import RunnableParallel
llm1 = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation"
)
llm2 = HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-V4-Pro",
    task="text-generation"

)
chat_model1 = ChatHuggingFace(llm=llm1)
chat_model2 = ChatHuggingFace(llm = llm2)

parser = StrOutputParser()
prompt1 = PromptTemplate(
    template="What is the summary of {topic} in 10 lines\n",
    input_variables=['topic'],
   
)
prompt2 = PromptTemplate(
    template="generate 5 question and answers according to  the summarised topic {topic}",
    input_variables=['topic']
)
prompt3 = PromptTemplate(
    template="Here is the summarised topic{topic} and few questions{questions}, merge the two with sumamarised topic and questions must also be present in the final text",
    input_variables=['topic', 'questions']
)
#create a parallel chain 
parallel_chain = RunnableParallel({
    'topic': prompt1| chat_model1 | parser,
    'questions': prompt2 | chat_model2 | parser
})
#what happens after parallel chain is controlled by merge chain
merge_chain = prompt3| chat_model1 |parser
#chain is resultant chain parallel + merge
chain = parallel_chain | merge_chain
text = """
One of the most powerful LLM-based applications are sophisticated question-answering (Q&A) chatbots which augment LLMs by providing it with inference-time access to a set of data. This might be private data, recent data, or data that is not part of the training data the LLM is trained on. These applications use a technique known as Retrieval Augmented Generation, or RAG.
Deep Agents gives you primitives for RAG: custom retrieval tools, a filesystem backend, subagents, skills, and grading rubrics. You can combine them in different ways depending on your corpus size, latency requirements, and how strictly answers must be grounded in source data.
This guide introduces several RAG patterns and walks through one end-to-end example: a documentation Q&A agent that indexes a subset of docs.langchain.com, retrieves relevant chunks at query time, offloads them to the filesystem, and delegates analysis to subagents so the orchestrator context stays clean.
​
RAG patterns
Deep Agents allows you to orchestrate retrieval, analysis, and synthesis in several ways:
Skills-guided retrieval: The user asks a question. The agent loads a relevant skill that describes how to search your corpus (which index to use, query formulation, citation format). The agent calls your retrieval tool following that guidance, then synthesizes an answer.
Rubric-checked grounding: The user asks a question. The agent retrieves evidence and drafts an answer. A grader sub-agent, configured with RubricMiddleware, evaluates whether the response is grounded in the retrieved source material. The agent revises until the rubric passes or an iteration cap is reached.
Todo-driven investigation: The user asks a question. If you opt into task planning, the agent uses the planning tool to create a todo list of documentation pages or search queries to investigate. It retrieves results for each item, then synthesizes a response from the collected evidence.
Retrieve, offload, and delegate: The user asks a question. The agent retrieves matching chunks and writes them to the filesystem backend rather than keeping full text in the orchestrator context. Subagents read, search, and summarize individual files in parallel. For large documents, the agent can paginate through files with built-in search tools or run a code interpreter to produce tables, timelines, or visuals from source data.
Grading rubrics require deepagents>=0.6.5 and are currently in beta.
This tutorial implements the retrieve, offload, and delegate pattern. The same primitives appear in the other patterns: skills often wrap retrieval workflows, rubrics can grade any of these flows, and opt-in todo planning helps break complex questions into focused searches.
​
Why retrieval matters
A language model on its own does not have access to your documentation. Ask it about a specific API that changed recently, and it answers from training data: often plausible, sometimes wrong, and never grounded in your source of truth.
Even when documentation is available, you generally cannot just fit it all into the context window. You therefore must select only the passages relevant to a given question, which in itself is a non-trivial task.
This tutorial uses one question throughout:
How do I stream intermediate tool results from a subagent?
Pass that question to a Deep Agent with no custom tools and no access to the documentation corpus, to see what the model comes up with:

Google

OpenAI

Anthropic

OpenRouter

Fireworks

Baseten

Ollama
from deepagents import create_deep_agent
from langchain.messages import HumanMessage

EXAMPLE_QUERY = "How do I stream intermediate tool results from a subagent?"

baseline_agent = create_deep_agent(
    model="google_genai:gemini-3.6-flash",
    tools=[],
    system_prompt=(
        "You are a helpful LangChain documentation assistant. "
        "Answer questions about LangChain APIs and patterns."
    ),
)

result = baseline_agent.invoke(
    {"messages": [HumanMessage(content=EXAMPLE_QUERY)]}
)

print(result["messages"][-1].text)
Without retrieval, the agent cannot look up current LangChain documentation. Responses tend to be generic, may omit guidance such as subagent streaming, or include outdated information.
The example in this tutorial indexes LangChain documentation, retrieves evidence with a vector search tool, analyzes each chunk in parallel subagents, and answers a question with citations to the docs.
​
What you will build
Index: Load the LangChain documentation into a vector store.
Search: Build a custom tool that runs vector similarity search and writes each retrieved chunk to the agent filesystem.
Analyze: Delegate file analysis to a subagent that reads the file and returns a focused summary.
Synthesize: Use the main agent to get the final answer from subagent reports.
"""
result = chain.invoke({"topic" : text})
print(result)