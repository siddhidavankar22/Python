from datetime import datetime


class Account:
    # Class variable for annual interest rate
    annualInterestRate = 0.045  # default to 4.5%

    def __init__(self, id=0, balance=0.0):
        self.__id = id
        self.__balance = balance
        self.__dateCreated = datetime.now()

    # Accessor methods
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def get_annual_interest_rate(self):
        return Account.annualInterestRate

    def set_annual_interest_rate(self, rate):
        Account.annualInterestRate = rate

    def get_date_created(self):
        return self.__dateCreated

    # Method to get monthly interest rate
    def get_monthly_interest_rate(self):
        return Account.annualInterestRate / 12

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    # Deposit method
    def deposit(self, amount):
        self.__balance += amount
# Test Program


def main():
    # Create an Account object with ID  and balance
    account = Account(int(input("enter account number ")),
                      int(input("enter balance ")))

    # Withdraw
    account.withdraw(int(input("enter withdraw amount ")))

    # Deposit
    account.deposit(int(input("enter deposit amount ")))

    # Print the account details
    print(f"Account ID: {account.get_id()}")
    print(f"Balance: ${account.get_balance():.2f}")
    print(
        f"Monthly Interest: ${account.get_monthly_interest_rate() * account.get_balance():.2f}")
    print(f"Date Created: {account.get_date_created()}")


if __name__ == "__main__":
    main()
