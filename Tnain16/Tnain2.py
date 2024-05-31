#Given a string, create a dictionary where keys are characters and values are their frequencies in the string
word= "Hello"
dict1 = {char: len([c for c in word if c == char]) for char in set(word)}
print(dict1)
