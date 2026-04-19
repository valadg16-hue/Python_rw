import numpy as np
import create_array as cr

def aggregate():
    print("\nChoose an aggregate/statistical operation:")
    print("1. Sum")
    print("2. Mean")
    print("3. Median")
    print("4. Standard Deviation")
    print("5. Variance")

    choice = int(input("Enter your choice: "))

    # take array input
    arr = cr.create_array1()

    if arr is None:
        print("Error in array creation!")
        return

    print("\nOriginal Array:\n", arr)

    match choice:

        
        case 1:
            print("Sum:", np.sum(arr))

        
        case 2:
            print("Mean:", np.mean(arr))

        
        case 3:
            print("Median:", np.median(arr))

        
        case 4:
            print("Standard Deviation:", np.std(arr))

        
        case 5:
            print("Variance:", np.var(arr))

        case _:
            print("Invalid choice!")


aggregate()
