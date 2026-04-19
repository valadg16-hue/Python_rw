import numpy as np
def main():
    print("Welcome to the NumPy Analyzer!")
    print("==============================")

    print("\nChoose an option:")
    print("1. Creat a Numpy Array")
    print("2. Perform Mathematical Operation")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Agregates and Statistics")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            import create_array as cr 
            cr.create_array()
        case 2:
            import mathematical_op as mop
            mop.mathematical_op()
        case 3:
            import combineandsplit as cbs 
            cbs.combineAndSplit()
        case 4:
            import search as se
            se.search()
        case 5:
            import agregates as ag
            ag.aggregate()
        case 6:
            exit()
        case _:
            print("Invalid choice!")




main()