import numpy as np
import create_array as cr

def mathematical_op():

    print("\nChoose a mathematical operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input!")
        return

    print("\nEnter First Array:")
    arr = cr.create_array1()

    print("\nEnter Second Array:")
    arr1 = cr.create_array1()

    
    if arr is None or arr1 is None:
        print("Error in array creation!")
        return

    print("First Array:\n", arr)
    print("Second Array:\n", arr1)

    
    if arr.shape != arr1.shape:
        print("Error: Arrays must be of same size!")
        return

    match choice:
        case 1:
            print("Addition:\n", arr + arr1)

        case 2:
            print("Subtraction:\n", arr - arr1)

        case 3:
            print("Multiplication:\n", arr * arr1)

        case 4:
            try:
                print("Division:\n", arr / arr1)
            except:
                print("Error: Division by zero!")

        case _:
            print("Invalid choice")



while True:
    mathematical_op()

    again = input("\nDo you want to continue? (y/n): ")
    if again.lower() != 'y':
        print("Program Ended.")
        break