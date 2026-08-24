import wikipedia
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.retrievers import WikipediaRetriever

wikipedia.set_user_agent("MyLangChainApp/1.0 (contact@example.com)")

api_wrapper = WikipediaAPIWrapper(top_k_results=3, doc_content_chars_max=4000)
retriever = WikipediaRetriever(api_wrapper=api_wrapper)

docs = retriever.invoke('Who is Kanye West')