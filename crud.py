from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class Student(BaseModel):
    name:str
    course:str

student_db=[]

@app.get("/student")
def student(student:Student):
    for student in student_db:
        return student

@app.post("/student")
def student_create(student:Student):
    student_db.append(student)
    return student

@app.get("/student/{id}")
def student_retrieve(student:Student, id:int):
    student=student_db[id]
    return student

@app.post("/student/{id}", response_model=Student)
def student_update(student:Student, id:int):
    student=student_db[id]
    return student

@app.delete("/student/{id}")
def student_delete(id:int):
    student_db.remove(id)
    return { 'delete':'student data deleted' }