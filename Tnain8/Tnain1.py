#Write a Python program to square and cube every number in a given list of integers using Lambda.
list1 = [1,2,3,4,5]
square = list(map(lambda x: x ** 2 ,list1))
cube = list(map(lambda x: x ** 3 ,list1))
print(square , cube)
