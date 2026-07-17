class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited ₹", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn ₹", amount)
        else:
            print("Insufficient Balance")

    def display(self):
        print("\n----- Account Details -----")
        print("Account Holder :", self.name)
        print("Current Balance: ₹", self.balance)


account = BankAccount("Tanaya", 10000)

account.display()
account.deposit(5000)
account.withdraw(500)
account.display()

#output
#----- Account Details -----
#Account Holder : Tanaya
#Current Balance: ₹ 10000
#Deposited ₹ 5000
#Withdrawn ₹ 500
#----- Account Details -----
#Account Holder : Tanaya
#Current Balance: ₹ 14500
