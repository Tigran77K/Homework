#Write a function that checks if a sentence is a pangram
def palindrom_checker(palindrom):
    palindroms = ""
    for i in palindrom:
        palindroms = i + palindroms
        if palindrom == palindroms:
            return True
    return False
print(palindrom_checker("anna"))