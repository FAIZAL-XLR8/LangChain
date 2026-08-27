from langchain_community.tools import DuckDuckGoSearchRun
#create an object of search run
search_obj = DuckDuckGoSearchRun() #this is also a runnable

result = search_obj.invoke('who was light yagami')
print(result)