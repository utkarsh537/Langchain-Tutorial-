from pydantic import BaseModel
class Student(BaseModel):
    name: str

new_student = {"name": "utkarsh"}
Student = Student(**new_student)
print(Student)