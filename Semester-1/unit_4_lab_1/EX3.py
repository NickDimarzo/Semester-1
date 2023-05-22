# A Bank Account
# Author: Dawson Gall

# Class & Definition
class BankAccount:
    def __init__(self, account_number, name):
        self.account_number = account_number
        self.name = name
        self.account_balance = 10000

    def deposit(self, total):
        self.account_balance += total

    def withdraw(self, total):
        self.account_balance -= total

    def funds(self):
        print(
            f' Hello {self.name}, Your account balance is {self.account_balance} for the account {self.account_number}')


# Customer Info
customer = BankAccount(706, "Dawson")
customer.deposit(200)
customer.withdraw(1000)
customer.funds()
