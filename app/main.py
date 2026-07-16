from fastapi import FastAPI
from app.database import initialize_database

# Create a FastAPI instance
app = FastAPI()

# Initialize the database when the application starts
initialize_database()


@app.get("/")
def home():
    return {"message": "Welcome to the Student Management API!"}