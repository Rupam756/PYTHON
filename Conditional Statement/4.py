#check the username contains less than 10 characters and contains less than 3 characters


username = input("Enter your username: ")
if len(username) < 10 and len(username) > 3:
    print("Username is valid.")
else:
    print("Username is invalid. It should be between 3 and 10 characters long.")

print(type(username))