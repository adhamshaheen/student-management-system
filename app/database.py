import sqlite3

# Define the database name
DATABASE_NAME = "students.db"


# Function to get a connection to the SQLite database
def get_connection():
    """Create and return a connection to the SQLite database."""

    connection = sqlite3.connect(DATABASE_NAME)

    return connection

# Function to initialize the database and create the students table
def initialize_database():
    """Create the students table if it does not already exist."""

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            major TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()