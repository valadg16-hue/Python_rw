import random
def ranDom():
    print("\n1. Random Data Generation")
    print("2. Generate Random List")
    print("3. Create Random Password")
    print("4. Generate Random OTP")
    print("5. Back to main menu")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("Random number:", random.randint(1, 100))
        case 2:
            n = int(input("How many numbers? "))
            start = int(input("Start of range: "))
            end = int(input("End of range: "))
            numbers = [random.randint(start, end) for _ in range(n)]
            print("\n Random List:", numbers)

        case 3:
            import string

            length = int(input("Enter password lenght: "))
            chars = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(chars) for _ in range(length))

            print("Random Password:", password)
        case 4:
            print("Your OTP :", random.randint(100000, 1000000))
        case 5:
            import project7_main as md
            md.main()

ranDom()