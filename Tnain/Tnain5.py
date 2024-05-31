num = int(input())
last_digit = num % 10
middle_digit = (num // 10) % 10
first_digit = num // 100
if first_digit <= middle_digit <= last_digit or first_digit >= middle_digit >= last_digit:
    print("Sorted")
else:
    print("Unsorted")
