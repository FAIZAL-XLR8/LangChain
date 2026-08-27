from langchain_core.tools import tool
@tool
def multiply(a:int, b : int) -> int:
    """Multiply two numbers a and b"""
    return a * b
@tool
def add(a:int, b : int) -> int :
    """Add two numbers a and b"""
    return a + b
#this is a runnable also
print(add.invoke({'a' : 2, 'b' : 12}))
class MathToolKit :
    def get_tools(self):
        return[add, multiply]
toolkit = MathToolKit()
tools = toolkit.get_tools()
for t in tools :
    print (t.description)