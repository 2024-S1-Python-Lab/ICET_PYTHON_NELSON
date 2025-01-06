
class Bank:
    def __init__(self, accNo,name, acctype,balance=0):
        self.acc = accNo
        self.na = name
        self.acctype = acctype
        self.bal = balance
    def deposit(self, amount):
        if amount > 0:
            self.bal +=amount
            print (f"Deposit succesfull! New balance: {self.bal}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")
    def withdraw(self,amount):
        if amount >0:
            if amount <= self.bal:
                self.bal -=amount
                print(f"Withdrawal succesfull! New balance: {self.bal}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")
    def display(self):
        print(f"\n Account Number: {self.acc} \n Account Holder Nmae: {self.na}")
        print(f" Account Type: {self.acctype} \n Balance: {self.bal}")
        print("\n*** Menu***")
        print(" 1. Deposit \n 2. Withdraw \n 3. Display \n 4. Exit ")
b1 = Bank(1002, "Nidhi" , "Savings", 0)
b1.display()
while True:
    #b1.display()
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        d = int(input("Enter amount to be deposited: "))
        b1.deposit(d)
    elif choice == 2:
        w =int(input("Enter amount to withdraw: "))
        b1.withdraw(w)
    elif choie == 3:
        b1.display()
    elif choice == 4:
        print("Exiting....Thank you! ")
        break
    else:
        print("Enter a valid choce.")
