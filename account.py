# account.py
class Account:
    def __init__(self, account_number, balance, customer):
        self.account_number = account_number
        self.balance = balance
        self.customer = customer

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"Account {self.account_number} Balance: ${self.balance}")
