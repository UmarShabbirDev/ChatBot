from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


students = {
    1:{
        "name": "umar",
        "age": 24,
        "year": 2
    }
}
class Student(BaseModel):
    name: str
    age: int
    year: int

class Update_Student(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[int] = None

@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    return students[student_id]

@app.get("/get-student-by-name")
def get_student_by_name(name: str):
    for student in students:
        if students[student]["name"] == name:
            return students[student]
    return {"message": "Student not found"}


@app.post("/add-student/{student_id}")
def add_student(student_id: int, student: Student):
    if student_id in students:
        return {"message": "Student already exist"}
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: Update_Student):
    if student_id not in students:
        return {"message": "Student not found"}
    if student.name != None:
        students[student_id]["name"] = student.name
    if student.age != None:
        students[student_id]["age"] = student.age
    if student.year != None:
        students[student_id]["year"] = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"message": "Student not found"}
    del students[student_id]
    return {"message": "Student deleted"}



