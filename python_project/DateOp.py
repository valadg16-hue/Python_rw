import datetime
import time

def dateTime():
    print("\n1. Display current date and time")
    print("2. Calculate different between two dates/times")
    print("3. Format date into custom format")
    print("4. Countdown timer")
    print("5. Back to main menu")
   
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            now = datetime.datetime.now()
            print("\nCurrent Date & Time:", now)

        case 2:
            date1 = input("Enter first date (YYYY-MM-DD): ")
            date2 = input("Enter second date (YYYY-MM-DD): ")

            d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

            diff = abs((d2 - d1).days)
            print("Difference:", diff, "days")

        case 3:
            date_input = input("Enter date (YYYY-MM-DD): ")
            d = datetime.datetime.strptime(date_input, "%Y-%m-%d")

            print("1. DD-MM-YYYY")
            print("2. Month DD, YYYY")
            print("3. DD Month YYYY")

            fmt = int(input("Choose format: "))

            match fmt:
                case 1:
                    print(d.strftime("%d-%m-%Y"))
                case 2:
                    print(d.strftime("%B %d, %Y"))
                case 3:
                    print(d.strftime("%d %B %Y"))
                case _:
                    print("Invalid format choice")

        case 4:
            seconds = int(input("Enter countdown time in seconds: "))
            while seconds > 0:
                print("Time left:", seconds, "seconds")
                time.sleep(1)
                seconds -= 1
            print("Time's up!")  # moved outside loop

        case 5:
            import project7_main as md
            md.main()

dateTime()