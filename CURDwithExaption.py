students = []

while True:
    print("\nStudent Management System")
    print("1. Add Student Create :")
    print("2. Show Students Read :")
    print("3. Update Student :")
    print("4. Delete Student :")
    print("5. Exit :")

    try:
        choice = int(input("Enter your choice: "))

        # CREATE
        if choice == 1:
            name = input("Enter student name: ")
            students.append(name)
            print("Student added successfully")

        # READ
        elif choice == 2:
            if len(students) == 0:
                print("No students found")
            else:
                print("Student List:")
                for i, student in enumerate(students):
                    print(i, student)

        # UPDATE
        elif choice == 3:
            index = int(input("Enter index to update: "))
            new_name = input("Enter new name: ")
            students[index] = new_name
            print("Student updated successfully")

        # DELETE
        elif choice == 4:
            index = int(input("Enter index to delete: "))
            students.pop(index)
            print("Student deleted successfully")

        # EXIT
        elif choice == 5:
            print("Program closed")
            break

        else:
            print("Invalid choice")


    #EXCEPTION HEDLING
    except ValueError:
        print("Please enter a valid number")

    except IndexError:
        print("Invalid index Student not found")

    except Exception as e:
        print("Something went wrong:", e)