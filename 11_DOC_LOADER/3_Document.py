from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
loader = DirectoryLoader(
    path='absolute_path',
    glob='*.pdf', #the directory contains what type of files,
    loader_cls=PyPDFLoader #"Go through all the .pdf files in this directory, and use PyPDFLoader to load each one."
)
document = loader.load() #this loads a list of documents with each page of each pdf as an document object   
print(document[0].meta_data)
print(document[0].page_content)
#disadvantage of this is like --> each pdf to load takes ~5 mins
#greater the number of pdfs greater is the amt to load fully -->use lazy loading