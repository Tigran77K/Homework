#Write a Python program to find intersection of two given arrays using Lambda
list1 = [1, 2, 54, 43, 8, 9]
list2 = [1, 2, 534, 435, 8, 9]
res = list(filter(lambda x: x in list2, list1))
print(res)
