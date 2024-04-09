from pydantic import BaseModel

# class Todo(BaseModel):
#     name: str
#     description: str
#     complete: bool
#     # date: str



# Define Pydantic models for data validation

class Address(BaseModel):
    city: str
    country: str

class Student(BaseModel):
    name: str
    age: int
    address: Address