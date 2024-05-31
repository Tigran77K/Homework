# Write a simple login system where the user enters a username and password. Handle
# the KeyError by raising a custom exception if the username is not found in the users
# database(dictionary).
name = input("Enter username: ")
password = input("Enter password: ")
def login_system(name, password):
    login_name = {"Jony": 1234, "Tom": 12543, "Mike": 53423}
    for k, v in login_name.items():
        if k == name and v == int(password):
            return "Login True"
    raise KeyError("Invalid username or password")
try:
    print(login_system(name, password))
except KeyError as e:
    print(e)
