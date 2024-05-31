# Write a function that checks the length of a string provided by the user. Handle the
# TypeError by raising a custom exception if the input is not a string.
def check_len(word):
        if not isinstance(word, str):
            raise TypeError(f"{word} - is not a string")
        else:
                return len(word)
print(check_len("р"))