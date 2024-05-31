#Write a Python program to get the largest number from a list.

numbers = [5, 7, 11, 9,0]
max_number = max(numbers)

for num in numbers:
    if num >= max_number:
        max_number = num
        print(num)