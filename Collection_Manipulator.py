students = []

while True:

    print("-----------------student management system-------------------")
    print("Select an option:")
    print("1. Add student")
    print("2. Display all student")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Display subject offered")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":

        id = int(input("Enter student id: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        Grade = input("Enter student grade: ")
        DOB = input("Enter student date of birth (yyyy-mm-dd): ")
        Subject = input("Enter student subjects (comma-separated): ")

        # ID and DOB stored as tuple
        id_dob = (id, DOB)

        # Subjects stored as set
        subjects = set(Subject.split(","))

        # Student information stored in dictionary
        student = {
            "id_dob": id_dob,
            "name": name,
            "age": age,
            "Grade": Grade,
            "subjects": subjects
        }

        # Dictionary added to list
        students.append(student)

        print("Student added successfully!!!")


    elif choice == "2":
        
        print("\n--- Display All Students ---")

        for student in students:
            print(
            "Student ID:", student["id_dob"][0],
            "| Name:", student["name"],
            "| Age:", student["age"],
            "| Grade:", student["Grade"],
            "| Date of Birth:", student["id_dob"][1],
            "| Subjects:", ", ".join(student["subjects"])
           )

    elif choice == "3":

        id = int(input("Enter student id: "))

        for student in students:

            if student["id_dob"][0] == id:
                print(student)
                break

        else:
            print("Student not found??")


    elif choice == "4":

        print("---------------Update student-------------------")

        id = int(input("Enter student id: "))

        for student in students:

            if student["id_dob"][0] == id:

                student["name"] = input("Enter new name: ")
                student["age"] = int(input("Enter new age: "))
                student["Grade"] = input("Enter new grade: ")

                print("Student updated successfully!!!")
                break

        else:
            print("Student not found??")


    elif choice == "5":

        print("---------------Delete student-------------------")

        id = int(input("Enter student id: "))

        for student in students:

            if student["id_dob"][0] == id:

                del students[students.index(student)]
                print("Student deleted successfully!!!")
                break

        else:
            print("Student not found??")


    elif choice == "6":

        for subject in set().union(*(student["subjects"] for student in students)):
            print(subject)


    elif choice == "7":

        print("Thank you for using the student management system!")
        break


    else:
        print("Invalid choice....")