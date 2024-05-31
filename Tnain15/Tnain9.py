#Write a function that finds the key with the maximum value in a dictionary.
scores = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 88}
def find_max_value_key(dictionary):
    value = 0
    key = ""
    for k, v in dictionary.items():
        if v > value:
            value = v
            key = k
    return key
print(find_max_value_key(scores))
