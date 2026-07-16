import sqlite3

from app.database import get_connection
from app.models import StudentCreate


# Function to create a new student in the database
def create_student(student: StudentCreate):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO students (name, age, major)
        VALUES (?, ?, ?)
        """,
        (
            student.name,
            student.age,
            student.major
        )
    )

    connection.commit()

    connection.close()


# Function to retrieve all students from the database
def get_all_students():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM students"
    )

    students = cursor.fetchall()

    connection.close()

    return students


# Function to retrieve a student by ID from the database
def get_student_by_id(student_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT * FROM students
        WHERE id = ?
        """,
        (student_id,)
    )

    student = cursor.fetchone()

    connection.close()

    return student


# Function to delete a student by ID from the database
def update_student(student_id, student: StudentCreate):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE students
        SET name=?, age=?, major=?
        WHERE id=?
        """,
        (
            student.name,
            student.age,
            student.major,
            student_id
        )
    )

    connection.commit()

    connection.close()


# Function to delete a student by ID from the database
def delete_student(student_id):

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM students
        WHERE id=?
        """,
        (student_id,)
    )

    connection.commit()

    connection.close()