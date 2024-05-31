#Write a function that checks if two sets are disjoint (have no common elements)
sets1 = {2,3,4,5}
sets2 = {6,9,7,5}
def check_set(set1 , set2):
    check = False
    for i in set1:
        for j in set2:
            if i == j :
                check = True
    if check:
        return "YES"
    else:
        return "No"
print(check_set(sets1,sets2))

