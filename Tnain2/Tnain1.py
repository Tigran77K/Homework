#Arrange string characters such that lowercase letters should come first
word = "PyNaTive"
word_upper = ""
word_lower = ""
for check in word:
    if check.islower():
            word_lower += check
    if check.isupper():
            word_upper += check
print( word_lower + word_upper)
