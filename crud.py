from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

class Student(BaseModel):
    id:int
    name:str
    course:str

student_db=[]

@app.get("/student")
def student():
    student=student_db
    return student

@app.post("/student")
def student_create(student:Student):
    student_db.append(student)
    return student

@app.get("/student/{id}")
def student_retrieve(id:int):
    for student in student_db:
        if student.id==id:
            return student
    else:
        raise HTTPException(status_code=404, detail="student not found")

@app.put("/student/{id}", response_model=Student)
def student_update(student:Student, id:int):
    for student in student_db:
        if student.id==id:
            return student
    else:
        raise HTTPException(status_code=404, detail="student not found with that id")

@app.delete("/student/{id}")
def student_delete(id:int):
    for student in student_db:
        if student.id==id:
            student_db.remove(student)
            return { "message":"success" }
    else:
        raise HTTPException(status_code=404, detail="student not found")