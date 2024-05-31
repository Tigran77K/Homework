#Given a list of numbers, write a function to find the sum of all numbers in the list that can be divided by 7
list_1 = [7, 2, 6, 14]
def list_sum(lst):
    total_sum = 0
    for i in lst:
        if i % 7 == 0:
            total_sum += i
    return total_sum
print(list_sum(list_1))
