from pydantic import BaseModel
#basemodel is a class which we have to inherit
class myClass(BaseModel):
    name:str
    age : int = 10 #sets the default value
my_dict = {"name" : "akhi"}
myObj = myClass(**my_dict) 
#myClass(name = "Faizal") same as above
print(myObj)
