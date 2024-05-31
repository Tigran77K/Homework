#Write a function that generates a random password for the user. Allow the user to
#specify the length and complexity of the password (include letters, numbers, and symbols)
import random
import string
def random_password(lens):
    check = ""
    password = ""
    isdigit = False
    islower = False
    isupper = False
    issimvol = False
    check += string.ascii_letters + string.digits + string.punctuation
    password = random.choices(check, k=lens)
    for i in password:
        if i.isdigit():
            isdigit = True
        elif i.islower():
            islower = True
        elif i.isupper():
            isupper =True
        elif i in string.punctuation:
            issimvol = True
    while isupper == False or islower == False or isdigit == False or issimvol == False or not password[0].isalpha():
        isdigit = False
        islower = False
        isupper = False
        issimvol = False
        password = random.choices(check, k=lens)
        for i in password:
            if i.isdigit():
                isdigit = True
            elif  i.islower():
                islower = True
            elif i.isupper():
                isupper = True
            elif i in string.punctuation:
                issimvol = True
    return "".join(password)
def password_check(password):
    digit = 0
    alpha = 0
    for i in password:
        if i.isdigit():
            digit += 1
        if i.isalpha():
            alpha += 1
    if digit < 2 or alpha < len(password) - len(password) / 2 or len(password) - alpha - digit < 2:
            return f"the password is not strong <  {password}"
    return f"password is strong >  {password}"
print(password_check(random_password(10)))