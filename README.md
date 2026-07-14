# 🎓 Student Management System

A simple command-line Student Management System built with Python as part of the **Innovera AI Internship - Task #04**.

This project demonstrates the fundamentals of Python programming by implementing a complete CRUD (Create, Read, Update, Delete) application with persistent data storage using a JSON file.

---

## 📌 Features

The application allows users to:

- ➕ Add a new student
- 📋 View all students
- 🔍 Search for a student by ID
- ✏️ Update student information
- 🗑️ Delete a student
- 💾 Save student data to a JSON file
- 📂 Automatically load saved data when the program starts

---

## 🛠️ Technologies Used

- Python 3
- JSON (for data storage)

No external libraries are required.

---

## 📁 Project Structure

```
Student_Management_System/
│
├── main.py          # Main application
├── students.json    # Stores student data
└── README.md        # Project documentation
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/adhamshaheen/student-management-system.git
```

### 2. Navigate to the project directory

```bash
cd student-management-system
```

### 3. Run the application

```bash
python main.py
```

---

## 📖 How to Use

After running the program, a menu similar to the following will appear:

```
===== Student Management System =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Save Data
7. Exit
```

Choose the desired option by entering its corresponding number.

---

## 💾 Data Storage

Student information is stored in the `students.json` file.

Each student is represented as a JSON object:

```json
{
    "id": "101",
    "name": "Ahmed",
    "age": 20,
    "major": "Computer Science"
}
```

The application automatically:

- Loads data when it starts.
- Saves data when the user exits.
- Allows manual saving through the menu.

---

## 🧠 Python Concepts Demonstrated

This project practices the following Python fundamentals:

- Variables and Data Types
- Conditional Statements
- Loops
- Functions
- Lists
- Dictionaries
- File Handling
- JSON Serialization
- Basic Error Handling
- Modular Programming

---

## 📸 Sample Output

```
===== Student Management System =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Save Data
7. Exit

Enter your choice (1-7): 1

Enter Student ID: 101
Enter Student Name: Ahmed
Enter Student Age: 20
Enter Student Major: Computer Science

Student added successfully!
```

---

## 🎯 Learning Outcomes

Through this project, I learned how to:

- Build a complete CRUD application using Python.
- Organize code into reusable functions.
- Store and retrieve data using JSON files.
- Validate user input and handle common errors.
- Work with lists and dictionaries effectively.
- Structure a Python program for better readability and maintainability.

---

## 👨‍💻 Author

**Adham Shaheen**

Computer Science Student at the German University in Cairo (GUC)

GitHub: https://github.com/adhamshaheen

---

## 📜 License

This project was created for educational purposes as part of the **Innovera AI Internship**.