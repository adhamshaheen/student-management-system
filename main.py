import json

students = []


# Function to load student data from a JSON file
def load_data():
    """Load students from the JSON file."""
    global students

    try:
        with open("students.json", "r") as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    except json.JSONDecodeError:
        students = []


# Function to save student data to a JSON file
def save_data():
    """Save students to the JSON file."""
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


# Function to add a new student
def add_student():
    """Add a new student to the system."""

    student_id = input("Enter Student ID: ")

    # Check if the ID already exists
    if find_student_by_id(student_id):
        print("A student with this ID already exists.")
        return

    name = input("Enter Student Name: ")

    # Validate age
    while True:
        try:
            age = int(input("Enter Student Age: "))
            break
        except ValueError:
            print("Please enter a valid number for age.")

    major = input("Enter Student Major: ")

    new_student = {
        "id": student_id,
        "name": name,
        "age": age,
        "major": major
    }

    students.append(new_student)

    print("Student added successfully!")


# Function to view all students
def view_students():
    """Display all students."""

    if len(students) == 0:
        print("\nNo students found.")
        return

    print("\n===== Student List =====")

    for student in students:
        print(f"ID    : {student['id']}")
        print(f"Name  : {student['name']}")
        print(f"Age   : {student['age']}")
        print(f"Major : {student['major']}")
        print("-" * 30)


# Helper function to find a student by ID (helps with searching, updating and deleting students)
def find_student_by_id(student_id):
    """Find a student by ID and return the student dictionary."""

    for student in students:
        if student["id"] == student_id:
            return student

    return None


# Function to search for a student by ID
def search_student():
    """Search for a student using their ID."""

    student_id = input("Enter Student ID: ")

    student = find_student_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nStudent Found")
    print(f"ID    : {student['id']}")
    print(f"Name  : {student['name']}")
    print(f"Age   : {student['age']}")
    print(f"Major : {student['major']}")


# Function to update an existing student's information
def update_student():
    """Update an existing student's information."""

    student_id = input("Enter Student ID to update: ")

    student = find_student_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    print("\nEnter the new student information.")

    student["name"] = input("New Name: ")

    while True:
        try:
            student["age"] = int(input("New Age: "))
            break
        except ValueError:
            print("Please enter a valid number for age.")

    student["major"] = input("New Major: ")

    print("Student updated successfully!")


# Function to delete a student from the system
def delete_student():
    """Delete a student from the system."""

    student_id = input("Enter Student ID to delete: ")

    student = find_student_by_id(student_id)

    if student is None:
        print("Student not found.")
        return

    students.remove(student)

    print("Student deleted successfully!")


# Main function to start the application
def main():
    # Load existing student data
    load_data()
    print("Student Management System Started!")
    print(f"{len(students)} student(s) loaded.")

    # Add a new student
    # add_student()
    # print(students)

    # view_students()
    # Save the updated student data
    # save_data()

    # Search for a student by ID
    # search_student()

    # Update a student's information
    # update_student()

    # Delete a student from the system
    delete_student()
    
    save_data()



if __name__ == "__main__":
    main()