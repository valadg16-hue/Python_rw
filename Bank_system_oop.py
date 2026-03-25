class BanckAccount:
    def __init__ (self,name,acc_no,balance=0):
        self.name = name
        self.acc_no = acc_no 
        self.balance = balance 
        self.transection = [] 

    def deposit(self,amount):
        if amount <= 0:
            print("Invalid deposit amount")
            return 
        
        self.balance += amount 
        self.transection.append(f"Deposite: + {amount}")
        print(f"{amount} credited successfully")

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid widhrawal amount!")
            return 
        
        elif amount> self.balance:
            print("Insufficient Balance! ")
        
        else:
            self.balance -= amount 
            self.transection.append(f"Withdraw:-{amount}")
            print(f"{amount} debited sucessfully")
    def check_balance(self):
        print(f"Account Holder:{self.name}")
        print(f"Account Number:{self.acc_no}")
        print(f"Current Balance:{self.balance}")

    def show_transaction(self):
        print("Transaction History:")
        if not self.transection:
            print("No transaction yet")
        else:
            for t in self.transection:
                print(t)

name = input("Enter your name: ")
acc_no = input("Enter account number: ")
account = BanckAccount(name,acc_no,0)

if len(name) != 0 and len(acc_no)!=0 :
    print("Acount details get!")

while True:
    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Transaction History")
    print("5.Exit")

    choice = int(input("Enter amount to choice: "))

    if choice == 1:
        amt = float(input("Enter amount to deposit: "))
        account.deposit(amt)

    elif choice == 2:
        amt = float(input("Enter amount to withdraw: "))
        account.withdraw(amt)

    elif choice == 3:
        account.check_balance()
    
    elif choice == 4:
        account.show_transaction()
    
    elif choice == 5:
        print("Thank you for bancking!")
        break 
    
    else:
        print("Invalid choice!")
    