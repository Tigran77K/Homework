#Develop a simple dice rolling simulator. Generate random numbers between 1 and 6 to
#simulate the roll of a six-sided die using the random module.
import random
dice = [1, 2, 3, 4, 5, 6]
print("         /_/- ")
print(f"dice >   | {random.choice(dice)} |")
print("         |_|_")
