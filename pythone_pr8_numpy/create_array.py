import numpy as np


def create_array():

    while True:
        print("\nSelect the types of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except:
            print("Invalid input!")
            continue

        match choice:

            
            case 1:
                try:
                    arr = np.array(list(map(int, input("Enter numbers: ").split())))
                except:
                    print("Invalid input!")
                    continue

                print(arr)

                while True:
                    print("\nChoose an operation:")
                    print("1. Indexing")
                    print("2. Slicing")
                    print("3. Go Back")

                    operation = int(input("Enter your choice: "))

                    if operation == 1:
                        try:
                            i = int(input("Enter index: "))
                            print("Element:", arr[i])
                        except:
                            print("Invalid index!")

                    elif operation == 2:
                        try:
                            start = int(input("Start: "))
                            end = int(input("End: "))
                            step = int(input("Step: "))
                            print("Sliced Array:", arr[start:end:step])
                        except:
                            print("Invalid slicing!")

                    elif operation == 3:
                        break

                    else:
                        print("Invalid choice!")

            
            case 2:
                try:
                    rows = int(input("Rows: "))
                    cols = int(input("Cols: "))
                    data = list(map(int, input("Enter all elements: ").split()))
                except:
                    print("Invalid input!")
                    continue

                if len(data) != rows * cols:
                    print("Error: Elements must be =", rows * cols)
                    continue

                arr_2d = np.array(data).reshape(rows, cols)
                print(arr_2d)

                while True:
                    print("\nChoose an operation:")
                    print("1. Indexing")
                    print("2. Slicing")
                    print("3. Go Back")

                    operation = int(input("Enter your choice: "))

                    if operation == 1:
                        try:
                            r = int(input("Row index: "))
                            c = int(input("Column index: "))
                            print("Element:", arr_2d[r, c])
                        except:
                            print("Invalid index!")

                    elif operation == 2:
                        try:
                            r1 = int(input("Row start: "))
                            r2 = int(input("Row end: "))
                            c1 = int(input("Col start: "))
                            c2 = int(input("Col end: "))
                            print("Sliced 2D Array:\n", arr_2d[r1:r2, c1:c2])
                        except:
                            print("Invalid slicing!")

                    elif operation == 3:
                        break

                    else:
                        print("Invalid choice!")

            case 3:
                print("Exiting...")
                break

            case _:
                print("Invalid choice!")



def create_array1():

    print("\nSelect the types of array to create:")
    print("1. 1D Array")
    print("2. 2D Array")

    try:
        choice = int(input("Enter your choice: "))
    except:
        print("Invalid input!")
        return None

    match choice:

        case 1:
            try:
                return np.array(list(map(int, input("Enter numbers: ").split())))
            except:
                print("Invalid input!")
                return None

        case 2:
            try:
                rows = int(input("Rows: "))
                cols = int(input("Cols: "))
                data = list(map(int, input("Enter all elements: ").split()))
            except:
                print("Invalid input!")
                return None

            if len(data) != rows * cols:
                print("Error: Invalid size")
                return None

            return np.array(data).reshape(rows, cols)

        case _:
            print("Invalid choice!")
            return None