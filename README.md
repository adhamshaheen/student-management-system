# Student Management System API

A RESTful Student Management System built using **FastAPI** and **SQLite**.

This project is an upgrade of the previous Python console-based Student Management System. 
The application was refactored into a backend web service with API endpoints, database integration, and data validation.

---

## Features

The API supports the following operations:

- Add a new student
- Retrieve all students
- Retrieve a specific student by ID
- Update student information
- Delete a student
- Store data permanently using SQLite database
- Validate incoming requests using Pydantic models

---

## Technologies Used

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn

---

## Project Structure

```
Student_Management_System/
│
├── app/
│   │
│   ├── main.py          # FastAPI application and API routes
│   ├── database.py      # SQLite database connection and initialization
│   ├── models.py        # Pydantic data models
│   └── crud.py          # Database CRUD operations
│
├── students.db          # SQLite database
├── requirements.txt     # Project dependencies
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/adhamshaheen/student-management-system.git
```

### 2. Navigate to the project directory

```bash
cd Student_Management_System
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

Windows:

```bash
.\.venv\Scripts\Activate
```

---

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the FastAPI server using:

```bash
uvicorn app.main:app --reload
```

The API will run at:

```
http://127.0.0.1:8000
```

---

## API Documentation

FastAPI automatically provides interactive documentation.

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/students` | Add a new student |
| GET | `/students` | Retrieve all students |
| GET | `/students/{id}` | Retrieve a student by ID |
| PUT | `/students/{id}` | Update student information |
| DELETE | `/students/{id}` | Delete a student |

---

## Example Request

### Add Student

POST:

```
/students
```

Request body:

```json
{
    "name": "Ahmed",
    "age": 20,
    "major": "Computer Science"
}
```

Response:

```json
{
    "id": 1,
    "name": "Ahmed",
    "age": 20,
    "major": "Computer Science"
}
```

---

## Database

The application uses SQLite.

The database file:

```
students.db
```

is created automatically when the application starts.

The students table contains:

| Column | Type |
|---|---|
| id | INTEGER PRIMARY KEY |
| name | TEXT |
| age | INTEGER |
| major | TEXT |

---

## Validation

The API validates incoming data using Pydantic.

Examples:

- Student age must be a positive number.
- Required fields cannot be empty.
- Data must follow the defined schema.

---

## Author

Adham Shaheen

Senior Computer Engineering Student at the German University in Cairo (GUC)