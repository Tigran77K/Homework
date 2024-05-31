#Write a Python program to get the smallest number from a list.

numbers = [48, 20,10, 56]
min_number = min(numbers)

for num in numbers:
    if num <= min_number:
        min_number = num
        print(num)