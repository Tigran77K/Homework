# Write a Python program that asks the user to enter a password. Keep asking for the
#password until the correct password "secret" is entered. Provide appropriate feedback to the user.
pasword = input()
stop = 0
pasword_on = "secret"
while stop < 2:
    stop+=1
    if pasword == pasword_on:
        print(f" the password is correct < {pasword} >")
        break
    if pasword != pasword_on:
        print("enter your password again")
        pasword = input()
        continue