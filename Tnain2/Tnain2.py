#Count all letters, digits, and special symbols from a given string
word = "P@#yn26at^&i5ve"
chars = 0
digits = 0
for Check in word:
    if Check.isupper() or Check.islower():
         chars += 1
    if Check.isdigit():
        digits += 1
print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbol = {len(word) - digits - chars}")
