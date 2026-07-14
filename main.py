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


# Main function to start the application
def main():
    load_data()
    print("Student Management System Started!")
    print(f"{len(students)} student(s) loaded.")


if __name__ == "__main__":
    main()