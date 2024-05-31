#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
def factorial(num):
    fac = 1
    while num > 0:
        fac *= num
        num -= 1
    return fac
print(factorial(5))
