numbers = [1, 2, 3,4 ]
min_numbers = min(numbers)
max_numbers = max(numbers)


for num in numbers:
    if num > min_numbers and num < max_numbers - num:
        print(num)
