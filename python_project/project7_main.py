def main():
    print("===================================")
    print("Welcome to Multi-Utility Toolkit")
    print("===================================")


    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Indetifier (UUID)")
    print("5. File Operation (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")
    print("====================================")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            import DateOp as dt
            dt.dateTime()
        case 2:
            import mathasSolv as ms 
            ms.maths_Sl() 
        case 3:
            import randomData as rdt
            rdt.ranDom()
        case 4:
            import uuid
            print(uuid.uuid4()) 

        case 5:
            import sys
            import os
            sys.path.append(os.path.dirname(os.path.abspath(__file__)))
            import PR6_file as p6
            p6.main_file()
        case 6:
            
            print("\n===== Explore Module Attributes =====")
            print("Which module do you want to explore?")
            print("1. DateOp")
            print("2. mathasSolv")
            print("3. randomData")
            print("4. uuid (built-in)")
            print("5. math (built-in)")
            print("6. os (built-in)")
            print("=====================================")
    
            mod_choice = int(input("Enter your choice: "))
    
            match mod_choice:
                case 1:
                    import DateOp as dt
                    print("\nAttributes of DateOp module:")
                    print(dir(dt))
                case 2:
                    import mathasSolv as ms
                    print("\nAttributes of mathasSolv module:")
                    print(dir(ms))
                case 3:
                    import randomData as rdt
                    print("\nAttributes of randomData module:")
                    print(dir(rdt))
                case 4:
                    import uuid
                    print("\nAttributes of uuid module:")
                    print(dir(uuid))
                case 5:
                    import math
                    print("\nAttributes of math module:")
                    print(dir(math))
                case 6:
                    import os
                    print("\nAttributes of os module:")
                    print(dir(os))
                case _:
                    print("Invalid choice!")
        case 7:
            exit()



main()