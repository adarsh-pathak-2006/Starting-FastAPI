from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

# class Student(BaseModel):
#     name:str
#     age:int
#     course:str

# @app.post("/student")
# def student(student:Student):
#     return {"Student name":student.name, "Student age":student.age, "Student course":student.course}

class Registration(BaseModel):
    username:str
    name:str
    password:str
    rep_password:str


class RegistrationResponse(BaseModel):
    username:str
    name:str

@app.post('/register', response_model=RegistrationResponse)
def registration(register:Registration):
    if register.password==register.rep_password:
        return register
    else:
        return { 'failed':'enter the same password in both fields' }

    