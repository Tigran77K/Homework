# Given two dictionaries, merge them into a new dictionary, excluding any keys that start with an underscore
dict1 = {"_1" :1 , "2" : 2 , "_3" :3 , "4" : 4}
dict2 = {k : v  for k,v in dict1.items() if k[0] != "_"}
print(dict2)