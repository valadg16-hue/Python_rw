import numpy as np
import create_array as cr

def combineAndSplit():

    print("\nCombine or Split Arrays:")
    print("1. Combine Arrays")
    print("2. Split Array")

    choice = int(input("Enter your choice: "))

    match choice:

        
        case 1:
            print("\nEnter First Array:")
            arr1 = cr.create_array1()

            print("\nEnter Second Array:")
            arr2 = cr.create_array1()

            if arr1 is None or arr2 is None:
                print("Error in array creation!")
                return

            print("\nOriginal Array:\n", arr1)
            print("\nSecond Array:\n", arr2)

            
            if arr1.ndim == 1:
                result = np.concatenate((arr1, arr2))
                print("\nCombined Array:\n", result)

            
            else:
                print("\n1. Vertical Stack")
                print("2. Horizontal Stack")

                opt = int(input("Enter your choice: "))

                if opt == 1:
                    result = np.vstack((arr1, arr2))
                    print("\nCombined Array (Vertical Stack):\n", result)

                elif opt == 2:
                    result = np.hstack((arr1, arr2))
                    print("\nCombined Array (Horizontal Stack):\n", result)

                else:
                    print("Invalid choice!")

        
        case 2:
            print("\nEnter Array:")
            arr = cr.create_array1()

            if arr is None:
                print("Error in array creation!")
                return

            print("\nOriginal Array:\n", arr)

            parts = int(input("\nEnter number of parts: "))

            
            if arr.ndim == 1:
                result = np.array_split(arr, parts)
                print("\nSplit Arrays:")
                for i in result:
                    print(i)

            
            else:
                print("\n1. Row-wise Split")
                print("2. Column-wise Split")

                opt = int(input("Enter your choice: "))

                if opt == 1:
                    result = np.array_split(arr, parts, axis=0)
                    print("\nRow-wise Split:")
                elif opt == 2:
                    result = np.array_split(arr, parts, axis=1)
                    print("\nColumn-wise Split:")
                else:
                    print("Invalid choice!")
                    return

                for i in result:
                    print(i)

        case _:
            print("Invalid choice!")



combineAndSplit()

        