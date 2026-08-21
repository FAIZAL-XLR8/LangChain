from langchain_community.document_loaders import TextLoader
from langchain_classic.text_splitter import RecursiveCharacterTextSplitter,Language
PYTHON_CODE = """
def hello_world():
    print("Hello, World!")

# Call the function
hello_world()
"""
splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=50,chunk_overlap=0
)
python_docs = splitter.split_text(PYTHON_CODE)
print(python_docs[0])