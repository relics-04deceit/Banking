# bank_manager.py
from account import Account
from customer import Customer

class BankManager:
    def __init__(self):
        self.accounts = []

    def create_account(self, customer, initial_balance):
        account_number = len(self.accounts) + 1
        account = Account(account_number, initial_balance, customer)
        self.accounts.append(account)
        print(f"Account created successfully! Account Number: {account_number}")

    def display_accounts(self):
        print("Bank Accounts:")
        for account in self.accounts:
            print(f"Account Number: {account.account_number}, Customer: {account.customer.name}, Balance: ${account.balance}")

if __name__ == "__main__":
    bank_manager = BankManager()

    customer1 = Customer(1, "John Doe", "john@example.com")
    customer2 = Customer(2, "Jane Smith", "jane@example.com")

    bank_manager.create_account(customer1, 1000.0)
    bank_manager.create_account(customer2, 500.0)

    bank_manager.display_accounts()

    # Perform transactions
    account1 = bank_manager.accounts[0]
    account1.deposit(500.0)
    account1.withdraw(200.0)

    account2 = bank_manager.accounts[1]
    account2.withdraw(100.0)

    bank_manager.display_accounts()
