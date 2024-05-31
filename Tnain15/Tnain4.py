#Write a function that takes two lists and returns a new list containing only the common elements. (without using set)
list_1 = [1,2,3,6,7,8]
list_2 = [4,5,6,7,8]
def new_list(list1 , list2):
    list3 = []
    for i in list1 :
        for j in list2:
            if i == j:
                list3.append(i)
    return list3
print(new_list(list_1,list_2))