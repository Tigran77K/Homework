#Write a function that calculates the sum of squares of numbers from 1 to n
def sum_squares(num):
    result = 0
    for i in range(1, num + 1):
        result += i * i
    return  result
print(sum_squares(5))