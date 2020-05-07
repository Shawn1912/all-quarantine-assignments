import time

class BankAccount:
    def __init__(self):
        self.acc = 0
    def deposit(self, amount):
        self.acc += amount
    def withdraw(self, amount):
        self.acc -= amount
    def balanceCheck(self):
        print("Balance : ", self.acc)

acc = BankAccount()
while True:
    print("\n***WELCOME TO TRANSACTIONS DAILY***\n")
    print("1. Withdrawal")
    print("2. Deposit")
    print("3. Check balance")
    print("4. Exit")

    choice = int(input("\nEnter your choice : "))

    if choice == 1:
        amount = int(input("\nEnter amount to be withdrawn : "))
        acc.withdraw(amount)
        print("Withdrawing...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("Please collect your money Rs {}".format(amount))
        acc.balanceCheck()

    elif choice == 2:
        amount = int(input("\nEnter amount to be deposited : "))
        acc.deposit(amount)
        print("Depositing...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("Rs {} deposited successfully.".format(amount))
        acc.balanceCheck()

    elif choice == 3:
        print("\nChecking balance...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        acc.balanceCheck()

    elif choice == 4:
        time.sleep(1.5)
        print("\n\n***THANKYOU FOR USING OUR APP!***")
        time.sleep(1)
        break

    time.sleep(1)
