#Write a function that checks if a given string is a valid email address.
def check_email(email):
    if email[-10:] == "@gmail.com" or email[-8:] == "@mail.ru":
        return "Valid email address"
    return "Invalid email address"

print(check_email("example@gmail.com"))

