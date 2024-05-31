# Write a Python program that calculates the Fibonacci sequence up to a given number n
# using a while loop. The Fibonacci sequence is a series of numbers where each number
# is the sum of the two preceding ones.
num = int(input("Enter a number to calculate Fibonacci"))
fib1 = 1
fib2 = 0
stop = 0
while stop < num:
    fib1, fib2 = fib2, fib1 + fib2
    stop +=1
print(f"Fibonacci > {num} = {fib2} ")