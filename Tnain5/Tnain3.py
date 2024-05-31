#Write a Python program that calculates the sum of all even numbers between 1 and 100 using a while loop.
num = 100
stop = 2
sum_even = 0
while stop <= num:
    sum_even += stop
    stop += 2
print(f"sum even 0 - {num} = {sum_even}")
