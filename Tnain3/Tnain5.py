#You are given three lists, list1, list2, and list3. Your task is to implement a programm that takes these lists and prints the following:
list1 =(1,2,34,5,76)
list2 =(1,65,7,9,5,3)
list3 =(5,67,547,766,54 ,7)
s1,s2,s3 = set(list1) , set(list2) , set(list3)
#The set of elements that are common to all three lists.
print(s1& s2 &s3)
#The set of elements that are present in at least two of the three lists, but not in all three.
print( s2 & s3)
#The set of elements that are unique to each list (present in only one list).
print(f"set1 > {s1 - s2 - s3} set2 > {s2 - s3 -s1} set3 > {s3 - s2 -s1}")