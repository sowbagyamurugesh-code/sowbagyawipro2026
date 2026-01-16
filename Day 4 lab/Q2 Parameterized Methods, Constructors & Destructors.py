class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
        print(f"Account {self.account_number} created with balance ₹{self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
        else:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Current Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance. Withdrawal failed.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Remaining Balance: ₹{self.balance}")

    def __del__(self):
        print(f"Account {self.account_number} is being closed. Final Balance: ₹{self.balance}")



acc1 = BankAccount("SB1001", 5000)

acc1.deposit(2000)
acc1.withdraw(3000)
acc1.withdraw(6000)

del acc1