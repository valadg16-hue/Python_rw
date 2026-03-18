students = []

def add():
    """Add student data"""
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    grade = input("Enter grade: ")
    sid = int(input("Enter student ID: "))
    dob = input("Enter DOB: ")

    subject = set(input("Enter subject (comma):").split(","))

    student = {
        "id_dob" : (sid,dob), #tuple 
        "name" : name,
        "age" : age,
        "grade" : grade,
        "subject" : subject  #set
    }
    students.append(student)
    print("Student Data added!")

def show():
    if students == []:
        print("Data not found")
    else:
        for s in students:
            print("\n ID :", s["id_dob"][0])
            print("Name :", s["name"])
            print("Age :",s["age"])
            print("Grade :", s["grade"])
            print("Subject :",", ".join(s["subject"]))
def update():
    """Upadet student dstails"""
    sid = int(input("Enter Student id number :"))
    found = False 
    for s in students:
        if s["id_dob"][0] == sid :
            s["age"] = int(input("new age: "))
            s["subjects"] = set(input("New subjects: ").split(","))
            found = True 
            break 
    if not found:
        print("Student not found")

def delete():
    """Delete student"""
    sid = int(input("Enter ID: "))
    found = False 

    for s in students:
        if s["id_dob"][0] == sid:
            students.remove(s)
            print("Deleted!")
            found = True 
            break
    if not found:
        print("Student data not found")

def subjects():
    """Show all subjects"""
    all_sub = set()

    for s in subjects:
        all_sub = all_sub.union(s["subjects"])

    print("Subjects:",", ".join(all_sub) if all_sub else "No subjects")


def docs():
    """Show function docs"""
    print(add.__doc__)
    print(show.__doc__)
    print(update.__doc__)
    print(delete.__doc__)
    print(subjects.__doc__)
    



#main
while True:
    print("\n1 Add")
    print("2 Show")
    print("3 Update")
    print("4 Delete")
    print("5 Subjects")
    print("6 Docs")
    print("7 Exit")

    ch = int(input("Enter choice :"))

    if ch == 1:
        add()
    elif ch == 2:
        show()
    elif ch == 3:
        update()
    elif ch == 4:
        delete()
    elif ch == 5:
        subjects()
    elif ch == 6:
        docs()
    elif ch ==7:
        print("Exit")
        break
    else:
        print("Invalid choice")

