#Write a Python function to calculate count of each letter in string
def count_letters(string):
    letters_count = {}
    for letter in string:
        if letter.isupper() or letter.islower():
            letter = letter.lower()
        if letter in letters_count:
            letters_count[letter] += 1
        else:
            letters_count[letter] = 1
    return letters_count
print(count_letters("fsdfdfdgdg"))