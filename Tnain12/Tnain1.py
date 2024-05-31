# Define a class named BankAccount with an __init__ method that initializes two
# instance variables: account_holder and balance
# The class has methods like deposit and withdraw, each of which takes an amount as
# an argument and updates the account balance accordingly. These methods also
# include checks for valid input and available funds.
# The get_balance method allows you to retrieve the account balance.
# We create an Object of the BankAccount class called account1 with an initial balanceof $1000.
# We deposit $500 and withdraw $200 from the account and print the accountinformation.
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        print(f"name - {account_holder}")
    def deposit(self,deposit):
        if deposit < 0:
            raise ValueError("you entered an incorrect number")
        self.balance += deposit
        print(f"deposit - {deposit}")
        return f"deposit - {deposit}"
    def withdraw(self,withdraw):
        if withdraw > self.balance or withdraw < 0:
            raise ValueError("you entered an incorrect number")
        print(f"withdraw - {withdraw}")
        self.balance -= withdraw
        return withdraw
account_1= BankAccount("Jony",1000)
account_1.deposit(500)
account_1.withdraw(200)
print(f"balance - {account_1.balance}")