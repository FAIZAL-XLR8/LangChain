from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
loader = DirectoryLoader(
    path='absolute_path',
    glob='*.pdf', #the directory contains what type of files,
    loader_cls=PyPDFLoader #"Go through all the .pdf files in this directory, and use PyPDFLoader to load each one."
)
document = loader.lazy_load() #this is an iterator/generator not a list of docs which loads doxs one by one in loop
for d in document : 
    print(d.metadata)
    print (d.page_content)