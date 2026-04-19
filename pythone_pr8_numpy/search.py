import numpy as np
import create_array as cr

def search():
    print("\nChoose an option:")
    print("1. Search a value")
    print("2. Sort the array")
    print("3. Filter value") 

    choice = int(input("Enter your choice: "))

    
    arr = cr.create_array1()

    if arr is None:
        print("Error in array creation!")
        return

    print("\nOriginal Array:\n", arr)

    match choice:

        
        case 1:
            val = int(input("Enter value to search: "))

            result = np.where(arr == val)

            if len(result[0]) == 0:
                print("Value not found!")
            else:
                print("Value found at index:", result)

        
        case 2:
            if arr.ndim == 1:
                sorted_arr = np.sort(arr)
            else:
                sorted_arr = np.sort(arr, axis=1)  # row-wise

            print("\nSorted Array:\n", sorted_arr)
            print("(Sorting applied row-wise.)")

        
        case 3:
            print("\n1. Greater than")
            print("2. Less than")
            print("3. Equal to")

            opt = int(input("Enter condition: "))
            val = int(input("Enter value: "))

            if opt == 1:
                result = arr[arr > val]
            elif opt == 2:
                result = arr[arr < val]
            elif opt == 3:
                result = arr[arr == val]
            else:
                print("Invalid choice!")
                return

            print("Filtered Values:", result)

        case _:
            print("Invalid choice!")



search()

        