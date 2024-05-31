# Write a function that removes an element at a specified index from a list. Handle the
# IndexError by raising a custom exception if the index is out of range
numbers = [1,2,332,4,5434,654,743]
def remove_index(list1,index):
    num = []
    if index >= len(list1):
        raise IndexError(f"{index} - this index does not exist")
    for i in list1:
        if i != list1[index]:
            num.append(i)
    return num
print(remove_index(numbers,6))