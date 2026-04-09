import math

def maths_Sl():
    print("\n1. Calculate Factorial")
    print("2. Solve Compound Interest ")
    print("3. Area of Geometric shapes")
    print("4. Back to Main Menu")
    
    

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            num = int(input("Enter a number: "))

            if num < 0:
                print("Factorial does not exist for negative numbers.")
            else:
                factorial = math.factorial(num)
                print(f"Factorial of {num} is {factorial}")
        case 2:
            
            P = float(input("Enter principal amount (P): "))
            r = float(input("Enter annual interest rate (r%) : "))
            n = float(input("Enter number of years (n): "))


            A = P * math.pow((1 + r/100), n)
            CI = A - P  

            print("Compound Interest:", CI)
            print("Total Amount:", A)
        case 3:
            print("\n1. Square")
            print("2. Rectangle")
            print("3. Triangle")
            print("4. Circle")

            choice = int(input("Enter your choice: "))

            match choice:

                case 1:
                    side = float(input("Enter side: "))
                    area = side * side
                    print("Area of Square:", area)

                case 2:
                    length = float(input("Enter length: "))
                    width = float(input("Enter width: "))
                    area = length * width
                    print("Area of Rectangle:", area)

                case 3:
                    base = float(input("Enter base: "))
                    height = float(input("Enter height: "))
                    area = 0.5 * base * height
                    print("Area of Triangle:", area)

                case 4:
                    r = float(input("Enter radius: "))
                    area = math.pi * r * r
                    print("Area of Circle:", area)

                case _:
                    print("Invalid choice!")
        case 4:
                import project7_main as md
                md.main()
        

maths_Sl()