#Write a function that calculates the average of a list of numbers.
list1 = [1,2,3,4]
def list_average(list2):
    sum_num = 0
    count = 0
    for i in list2:
        sum_num += i
        count += 1
    if count == 0:
        return 0
    return sum_num / count
print(list_average(list1))
