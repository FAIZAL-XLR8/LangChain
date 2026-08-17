from pydantic import BaseModel,EmailStr,Field #field hlps to give constraints, emailstr for email validations
from typing import Optional
#basemodel is a class which we have to inherit

class myClass(BaseModel):
    name:str
    age : int = 10 #sets the default value
    courses : Optional[int] = None
    email: EmailStr
    cgpa:float = Field(gt=0,lt=10,default=2,description='A cgpa value representing students aggregate scores')
my_dict = {"name" : "akhi", "courses" : 10, "email":"anvc@gmail.com"}
myObj = myClass(**my_dict) 
#myClass(name = "Faizal") same as above
obj_dict= dict(myObj)
pydantic_json_ = myObj.model_dump_json()
print(pydantic_json_)
print(obj_dict['age'])
print(myObj.age)
print(myObj)
