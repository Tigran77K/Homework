#Given a string, create a dictionary where keys are characters, and values are their ASCII values.
word = "hello"
dict1 = {i : ord(i) for i in  word}
print(dict1)
