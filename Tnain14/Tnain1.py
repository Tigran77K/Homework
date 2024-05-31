# Create a class called BankAccount to represent a basic bank account. The class should
# have the following attributes
class BankAccount:
    def __init__(self, owner, balance):
        if not isinstance(balance, int) or balance < 0:
            raise ValueError("Initial balance must be a non-negative integer.")
        self.owner = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Balance must be a non-negative integer.")
        self.__balance = value

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Deposit amount must be a positive integer.")
        self.__balance += amount

    def withdraw(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive integer.")
        if amount > self.__balance:
            raise ValueError("Withdrawal amount exceeds the current balance.")
        self.__balance -= amount

account1 = BankAccount("John", 100)
account1.deposit(100)
account1.withdraw(100)
print(account1.get_balance())



