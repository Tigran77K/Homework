# Given a list of words, create a dictionary where keys are words, and values are
# their lengths, but only for words with lengths greater than 3
list1 = ["hello", "world", "python", "Hi" ,  "great"]
dict1= {i : len(i) for i in list1  if len(i) > 3}
print(dict1)