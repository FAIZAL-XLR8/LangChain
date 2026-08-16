from typing import TypedDict
#inheriting from class Typed Dict

class myClass(TypedDict):
    name : str
    age : int
myObj:myClass = {"name" : "Faizal", "age" : 10}
print(myObj)
