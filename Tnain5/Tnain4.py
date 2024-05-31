# Write a Python program that generates a random number between 1 and 100 and asks
# the user to guess the number. The program should give hints whether the guessed
# number is too high or too low until the correct number is guessed.
import random
random_number = random.randint(1, 100)
print("enter number 0 - 100")
stop = False
while stop == False:
    num = int(input())
    if num == random_number:
        print(f"win random number <{num}>")
        stop = True
    if num > 100:
        print("enter number less 100")
    if num < random_number and num != random_number and num <= 100:
        print(f"more > {num} )")
        continue
    if num > random_number and num != random_number and num <= 100:
        print(f"less < {num} )")
        continue
