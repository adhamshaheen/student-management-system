from fastapi import FastAPI, HTTPException, status

from app.database import initialize_database
from app.models import StudentCreate, StudentResponse
from app import crud

# Create a FastAPI instance
app = FastAPI()

# Initialize the database and create the students table
initialize_database()


#====================================== API Endpoints ====================================== 

# Route 1: Endpoint to add a new student
# POST http://localhost:8000/students
@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def add_student(student: StudentCreate):

    # Call the create_student function from the crud module to add the student to the database
    new_student = crud.create_student(student)

    return new_student


# Route 2: Endpoint to retrieve all students
# GET http://localhost:8000/students
@app.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_students():

    # Call the get_all_students function from the crud module to retrieve all students from the database
    students = crud.get_all_students()

    return students


# Route 3: Endpoint to retrieve a student by ID
# GET http://localhost:8000/students/{student_id}
@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(student_id: int):

    # Call the get_student_by_id function from the crud module to retrieve the student from the database
    student = crud.get_student_by_id(student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# Route 4: Endpoint to update a student by ID
# PUT http://localhost:8000/students/{student_id}
@app.put(
    "/students/{student_id}",
    response_model=StudentResponse
)
def update_student(
    student_id: int,
    student: StudentCreate
):

    existing_student = crud.get_student_by_id(student_id)

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    updated_student = crud.update_student(
        student_id,
        student
    )

    return updated_student


# Route 5: Endpoint to delete a student by ID
# DELETE http://localhost:8000/students/{student_id}
@app.delete(
    "/students/{student_id}"
)
def delete_student(student_id: int):

    existing_student = crud.get_student_by_id(student_id)

    if existing_student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    crud.delete_student(student_id)

    return {
        "message": "Student deleted successfully"
    }


#====================================== Home Endpoint ======================================
@app.get("/")
def home():
    return {
        "message": "Welcome to the Student Management API!"
    }