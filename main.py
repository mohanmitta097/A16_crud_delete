from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI(title="Student CRUD - Complete")
students = []
next_id = 1

class Student(BaseModel):
    name: str
    age: int
    course: str

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def page():
    return FileResponse("static/index.html")

@app.get("/students")
def list_students():
    return students

@app.post("/students")
def add_student(student: Student):
    global next_id
    record = {"id": next_id, **student.model_dump()}
    students.append(record)
    next_id += 1
    return record

@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    for index, current in enumerate(students):
        if current["id"] == student_id:
            students[index] = {"id": student_id, **student.model_dump()}
            return students[index]
    raise HTTPException(status_code=404, detail="Student not found")

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, current in enumerate(students):
        if current["id"] == student_id:
            deleted = students.pop(index)
            return {"message": "Student deleted", "student": deleted}
    raise HTTPException(status_code=404, detail="Student not found")
