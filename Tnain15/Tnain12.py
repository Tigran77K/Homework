#Write a function that returns the nth largest element from a list
def find_max(list1):
    max_element = list1[0]
    for i in list1:
        if i > max_element:
            max_element = i
    return max_element

def nth_largest_element(list1, n):
    max_element = 0
    if n <= 0 or n > len(list1):
        raise ValueError("Invalid value of n")
    for i in range(n):
        max_element = find_max(list1)
        list1.remove(max_element)
    return max_element

list_1 = [1, 2, 34, 43, 653, 3]
print(nth_largest_element(list_1,2))
