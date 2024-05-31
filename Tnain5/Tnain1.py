#Write a Python program that prompts the user to enter a positive integer and then prints all the numbers from 1 to that number using a while loop.
num = int(input())
numbers = []
stop = 0
while stop < num:
    stop += 1
    numbers.append(stop)
print(numbers)