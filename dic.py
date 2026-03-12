#Noraml DICTIONARY
di = {
    "Name" : "Divyarajsinh",
    "Age" : 22,
    "Subject" : ["Hindi","English","Gujarati"],
    "Education" : "BE"
}

for key,value in di.items():
    print(f"{key} : {value}")

#CURD USING LIST,TUPLE,SET,DICTIONARY

# LIST → store student names
students = []

# TUPLE → fixed subjects
subjects = ("Math", "Science", "English")

# SET → unique student IDs
student_ids = set()

# DICTIONARY → student details
student_data = {}

# number of students
n = int(input("Enter number of students: "))

for i in range(n):
    
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    city = input("Enter student city: ")
    sid = int(input("Enter student ID: "))
    
    # LIST
    students.append(name)
    
    # SET
    student_ids.add(sid)
    
    # DICTIONARY
    student_data[name] = {
        "age": age,
        "city": city
    }

print("\nSubjects (Tuple):", subjects)

print("\nStudent List:", students)

print("\nStudent IDs (Set):", student_ids)

print("\nStudent Details (Dictionary):")
for key, value in student_data.items():
    print(key, ":", value)