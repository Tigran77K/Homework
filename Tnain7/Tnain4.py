#Write a function that finds the index of a given element in a list. If the element is not present, return -1
list1 = [3,2,3,4,5,1]
def index_list(num , list2):
    count = 0 # -1
    for i in list2:
        count += 1
        if num == i:
            return f"index > {count} num > {num}"
    return -1
print(index_list(1,list1))