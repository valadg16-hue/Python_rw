students = []

while True:
    print("\nWelcome to Student Data Organize")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grade = input("Enter grade: ")
        student_id = int(input("Enter student ID: "))
        dob = input("Enter DOB (YYYY-MM-DD): ")

        subjects_input = input("Enter subjects (comma separated): ")
        subjects = set(s.strip() for s in subjects_input.split(","))

        id_dob = (student_id, dob)

        student = {
            "id_dob": id_dob,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        students.append(student)
        print("Student added successfully!")
        

    elif choice == "2":
        if len(students) == 0:
            print("No students found.")
        else:
            print("\nAll Students")
            for s in students:
                print("ID:", s["id_dob"][0],
                      "| Name:", s["name"],
                      "| Age:", s["age"],
                      "| Grade:", s["grade"],
                      "| Subjects:", ", ".join(s["subjects"]))
                

    elif choice == "3":
        sid = int(input("Enter student ID to update: "))
        found = False

        for s in students:
            if s["id_dob"][0] == sid:
                found = True
                s["age"] = int(input("Enter new age: "))

                subjects_input = input("Enter new subjects: ")
                s["subjects"] = set(x.strip() for x in subjects_input.split(","))

                print("Student updated successfully!")

        if not found:
            print("Student not found!")

    elif choice == "4":
        sid = int(input("Enter student ID to delete: "))
        found = False

        for i in range(len(students)):
            if students[i]["id_dob"][0] == sid:
                del students[i]   
                print("Student deleted successfully!")
                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == "5":
        all_subjects = set()

        for s in students:
            all_subjects.update(s["subjects"])

        if len(all_subjects) > 0:
            print("Subjects Offered:", ", ".join(all_subjects))
        else:
            print("No subjects found.")

    elif choice == "6":
        print("Thank you for using the program!")
        break

    else:
        print("Invalid choice!")