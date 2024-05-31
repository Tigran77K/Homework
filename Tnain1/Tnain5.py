numbers = [1, 2, 3, 4, 1]
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
numbers = unique_numbers
print(numbers)
