print("Welcome to the Pattern Generator and Number Analyer!") 

print("Select an option:")
print("1. Generater a Pattern")
print("2. Analyze a Range of Numbers")
print("3. Exit")

a = int(input("Enter your choice: ")) 

match a:
    case 1:
        b = int(input("Enter the number of rows for pattern: "))
        for i in range(1,b+1):
            k = "*"*i 
            print(k)
    case 2:
        start = int(input("Enter the start of range: "))
        end = int(input("Enter the end of range: "))
        k = 0
        for j in range(start,end+1):
            if j % 2 == 0:
                print("Number" + str(j) +"is Even")
            else:
                print("Number" + str(j) + " is Odd")

            k = k + j 
        print("Sum of all Number from " + str(start) + " to " + str(end) + "is :" + str(k))
    case 3:
        print("Exiting the program. Goodbye!")
    case _:
        print("Invalid")