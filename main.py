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
    for student in students:
        if student["id"] == student_id:
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


# Main function to start the application
def main():
    # Load existing student data
    load_data()
    print("Student Management System Started!")
    print(f"{len(students)} student(s) loaded.")

    # Add a new student
    add_student()
    print(students)

    # Save the updated student data
    save_data()




if __name__ == "__main__":
    main()