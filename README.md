**Name:** Asti Sojitra  
**Assignment:** Practical Assignment



# Student Management System

A simple **Student Management System** developed using **Python**.
This project is a menu-driven console application that allows users to add, display, search, update, and delete student records.

## Features

The Student Management System provides the following options:

1. **Add Student** – Add a new student with ID, name, age, grade, date of birth, and subjects.
2. **Display All Students** – Display all stored student records.
3. **Search Student** – Search for a student using their student ID.
4. **Update Student** – Update a student's name, age, and grade using their student ID.
5. **Delete Student** – Delete a student record using their student ID.
6. **Display Subjects Offered** – Display the available subjects.
7. **Exit** – Exit the Student Management System.

## Student Information

When adding a student, the following information is entered:

* Student ID
* Student Name
* Student Age
* Student Grade
* Date of Birth
* Subjects

The subjects are entered as comma-separated values.

## Technologies Used

* **Python**
* Python Lists
* Python Dictionaries
* `input()` and `print()`
* Conditional statements
* `for` loops
* `while` loop

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

You can check the Python version using:

```bash
python --version
```

### 2. Run the Program

Open a terminal in the project folder and run:

```bash
python StudentManagement.py
```

## Main Menu

When the program starts, the following menu is displayed:

```text
-----------------student management system-------------------
Select an option:
1.Add student:
2.Display all student:
3.Search student
4.Update student
5.Delete student
6.Display subject offered
7.Exit:
Enter your choice (1-7):
```

## Sample Output

### 1. Add Student

```text
-----------------student management system-------------------
Select an option:
1.Add student:
2.Display all student:
3.Search student
4.Update student
5.Delete student
6.Display subject offered
7.Exit:
Enter your choice (1-7): 1

Enter student id:101
Enter student name:Rahul
Enter student age:20
Enter student grade:A
Enter student date of birth(yyyy-mm-dd):2006-05-15
Enter student subjects(comma-separated):Python,C++

Student added successfully!!!
```

The program stores the student information in the following format:

```text
{
    'id': 101,
    'name': 'Rahul',
    'age': 20,
    'Grade': 'A',
    'DOB': '2006-05-15',
    'Subject': 'Python,C++'
}
```

### 2. Display All Students

```text
Enter your choice (1-7): 2

-----------------Display Student List-------------------

{'id': 101, 'name': 'Rahul', 'age': 20, 'Grade': 'A',
'DOB': '2006-05-15', 'Subject': 'Python,C++'}
```

### 3. Search Student

```text
Enter your choice (1-7): 3

Enter student id:101

{'id': 101, 'name': 'Rahul', 'age': 20, 'Grade': 'A',
'DOB': '2006-05-15', 'Subject': 'Python,C++'}
```

If the student ID does not exist:

```text
Enter student id:999

student not found??
```

### 4. Update Student

```text
Enter your choice (1-7): 4

---------------Update student-------------------

Enter student id:101
Enter new name:Ravi
Enter new age:21
Enter new grade:A+

Student updated successfully!!!
```

### 5. Delete Student

```text
Enter your choice (1-7): 5

---------------Delete student-------------------

Enter student id:101

Student deleted successfully!!!
```

If the student ID does not exist:

```text
Enter student id:999

student not found??
```

### 6. Display Subjects

```text
Enter your choice (1-7): 6

--------Subject Name--------
Python
C++
PHP
```

### 7. Exit

```text
Enter your choice (1-7): 7

Thank you for using the student management system!
```

## Project Structure

```text
StudentManagement/
│
├── StudentManagement.py
└── README.md
```

## Data Storage

Student records are stored in a Python list:

```python
students = []
```

Each student is stored as a dictionary containing:

```python
{
    "id": id,
    "name": name,
    "age": age,
    "Grade": Grade,
    "DOB": DOB,
    "Subject": Subject
}
```

## Available Subjects

The program currently displays these subjects:

* Python
* C++
* PHP

## Notes

* Student ID is used to search, update, and delete student records.
* Age and Student ID are entered as integers.
* Date of birth should be entered in `yyyy-mm-dd` format.
* Subjects should be entered using commas to separate multiple subjects.
* The program runs continuously until the user selects **7. Exit**.
