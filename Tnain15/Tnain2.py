#Create a Python class representing a basic calculator with methods for addition, subtraction, multiplication, and division.
class Calculator:
    def __init__(self, num1 , num2):
        self.num_1 = num1
        self.num_2 = num2
    def addition(self):
        return self.num_1 + self.num_2
    def  subtraction(self):
        return self.num_1 - self.num_2
    def multiplication(self):
        return self.num_1 * self.num_2
    def division(self):
        if self.num_2 != 0:
            return self.num_1 / self.num_2
        else:
            raise ZeroDivisionError("Division by zero is not allowed")
calc1 = Calculator(20 , 20)
print(calc1.subtraction())