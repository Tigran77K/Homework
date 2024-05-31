# Create a hierarchy of classes representing different types of bank accounts. Start
# with a base class called BankAccount. Then, create two subclasses,
# SavingsAccount and CheckingAccount. Each subclass should inherit from the BankAccount class
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number  = account_number
        self.balance = balance
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
    def get_balance(self):
        if self.balance < 0:
            raise ValueError(f"Balance is negative: {self.balance}")
        return f"Account number - {self.account_number}, Balance - {int(self.balance)}"
class SavingsAccount(BankAccount):
    def __init__(self,account_number , balance ,interest_rate=0):
        super().__init__(account_number , balance)
        self.interest_rate = interest_rate
    def deposit(self,deposit):
        if deposit < 0 or  self.interest_rate > 100:
            raise ValueError("you entered an incorrect number")
        self.balance += deposit
        self.balance += deposit * self.interest_rate / 100
class CheckingAccount(BankAccount):
    def __init__(self , account_number , balance ,overdraft_fee=5):
        super().__init__(account_number,balance)
        self.overdraft_fee = overdraft_fee
    def withdraw(self, withdraw):
        if withdraw > self.balance or withdraw < 0 or self.overdraft_fee > 100:
            raise ValueError("you entered an incorrect number")
        self.balance -= withdraw + withdraw * self.overdraft_fee / 100
        return withdraw
account_1 = SavingsAccount(1324 , 1000 , 2)
account_1.deposit(100)
print(account_1.get_balance())