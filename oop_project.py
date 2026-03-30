class Employee:
    def __init__(self, name, age, employee_id, salary):
        self.name = name
        self.age = age
        self.__employee_id = employee_id 
        self.__salary = salary            

    
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary

    
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, emp_id):
        self.__employee_id = emp_id

    def display(self):
        print("Employee Details:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Employee ID: {self.__employee_id}")
        print(f"Salary: ${self.__salary}")

    


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}")

    


class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print(f"Programming Language: {self.programming_language}")

    


def main():
    print("--- Python OOP Project: Employee Management System ---")

    objects = []

    while True:
        print("\nChoose an operation:")
        print("1. Create an Employee")
        print("2. Create a Manager")
        print("3. Create a Developer")
        print("4. Show Details")
        print("5. Exit")

        choice = int(input("\nEnter your choice: "))

        match choice:
            case 1:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                e = Employee(name, age, emp_id, salary)
                objects.append(e)
                print(f"Employee created with name: {name}, age: {age}, ID: {emp_id}, and salary: ${salary}.")

            case 2:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                dept = input("Enter Department: ")
                m = Manager(name, age, emp_id, salary, dept)
                objects.append(m)
                print(f"Manager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and department: {dept}.")

            case 3:
                name = input("Enter Name: ")
                age = int(input("Enter Age: "))
                emp_id = input("Enter Employee ID: ")
                salary = float(input("Enter Salary: "))
                lang = input("Enter Programming Language: ")
                d = Developer(name, age, emp_id, salary, lang)
                objects.append(d)
                print(f"Developer created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, and language: {lang}.")

            case 4:
                if not objects:
                    print("No records found.")
                else:
                    for i, obj in enumerate(objects):
                        print(f"\n--- Record {i + 1} ---")
                        obj.display()

                        # issubclass() check
                        if isinstance(obj, Employee):
                            print(f"Is Manager a subclass of Employee? {issubclass(Manager, Employee)}")

            case 5:
                print("\nExiting the system. All resources have been freed.")
                print("Goodbye!")
                break

            case _:
                print("Invalid choice. Please try again.")

        print("\n--- Choose another operation ---")


main()