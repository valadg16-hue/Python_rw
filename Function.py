def filttering_data(threshold_value, data_set):
    filtered_data = [x for x in data_set if x > threshold_value]
    new_set_filtter = ", ".join(str(i) for i in filtered_data)
    return new_set_filtter


def factorial(fact_num):
    if fact_num == 1:
        return 1
    else:
        return fact_num * factorial(fact_num - 1)


def data_summary(enter):
    len_vl = len(enter)
    min_v =  min(enter)
    max_vl = max(enter)
    sum_vl = sum(enter)
    avg_vl = sum_vl/len_vl
    print("- Total element: ",len_vl)
    print("- Minimum value: ",min_v)
    print("- Maximum value: ",max_vl)
    print("- Sum of all values: ",sum_vl)
    print("- Avrage value: ",avg_vl)

def input_data():
    global data_set 
    data_set = list(map(int, input().split(" ")))
    return data_set



def main():
    print("\n1. Input Data")
    print("2.Display Data Summary (Built-in Function) ")
    print("3.Calculate Factorial (Recursion)")
    print("4.Filter Data by Threshold (Lambda Function Values)")
    print("5.sort Data")
    print("6.Exit Program")

    a = int(input("\nPlease enter your choice: "))

    if a == 1:
        print("\nEnter data for a 1D array (separated by spaces):")
        global enter 
        enter = input_data()
        print("\nData has been stored successfully!")
        main()

    elif a == 2:
        print("\nData Summary:")
        data_summary(enter)
        main()

    elif a == 3:
        fact_num = int(input("Enter a number to calculate its factorial: " ))
        final_fact=factorial(fact_num)
        print(f"Factorial of {fact_num} is : {final_fact}")
        main()

    elif a == 4: 
        print("Enter a threshold value to filter out  data above this value:")
        threshold_value = int(input())
        filter_values  = filttering_data(threshold_value,data_set)
        print(filter_values)
        main()
    elif a == 5:
        print("\nChoose sorting option:")
        print("1. Ascending")
        print("2. Descending")

        value = int(input("\nEnter your choice: "))

        if value == 1:
            sort_data = sorted(data_set)
            new_data_ac = ", ".join(str(i) for i in sort_data)
            print(new_data_ac)
            main()
        elif value == 2:
            des = sorted(data_set,reverse=True)
            ew_data_dc = ", ".join(str(i) for i in des)
            print(ew_data_dc)
            main()
        
        main()

    elif a == 6:
        print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
        exit()







    
print("\nWelcome to the Data Analyzer and Transformer Program")
main()