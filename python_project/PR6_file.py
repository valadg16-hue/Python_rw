def createFile(name):
    try:
        with open(name,"x") as file:
            print("\nFile created sucessfully ! \n")
    except FileExistsError:
        print("\n File already there ! \n")
    
    main_file()

def readFile(name):
    try :
        with open(name,"r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("\n File is not found ! \n")
    
    main_file()


def appendFile(name,data):
    try:
        with open(name,"a") as file:
            file.write("\n ----------------- \n")
            file.write(data) 
            file.write("\n ------------------\n")
    except FileNotFoundError:
        print("\nFile Not Found !")
    
    main_file()

def searchEnter(name,keyword):
    try:
        with open(name,"r") as file:
            li = file.readlines()
            for index, line in enumerate(li):
                if keyword in line:
                    print(index)
                    print(line)
    except FileNotFoundError:
        print("\n File not found ! \n")
    
    main_file()

def clearFile(name):
    try:
        with open(name,"w") as file:
            pass 
    except FileNotFoundError:
        print("\n File not found ! \n")
    
    

            


def main_file():
    print("\nWelcom to personal Journal Manager!")
    print("Please Select an option :")

    print("\n1. Creat new file ")
    print("2. Add new Entriy ")
    print("3. View All Entris")
    print("4. Seacher All Entri")
    print("5. Delete All Entris")
    print("6. Back to main menu")
    print("7. Exit")

    value = int(input("User Input : "))

    match value:
        case 1:
            name = input("Enter File name :")
            createFile(name)
        case 2:
            name = input("Enter File name :")
            data = input("Enter your journal entry: ")
            print("Enter add successfully!")
            appendFile(name,data)
            
        case 3:
            name = input("Enter File name :")
            readFile(name)
        case 4:
            name = input("Enter File name :")
            keyword = input("Enter keyword or data to search: ")
            searchEnter(name,keyword)
        case 5:
            name = input("Enter File name:")
            clearFile(name)
            main_file()
        case 6:
            import project7_main as md
            md.main()
        case 7:
            exit()
        case _:
            print("Enter Valid number")
    



main_file()