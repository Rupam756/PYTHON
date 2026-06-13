# take input from user keys and values and create a dictionary

friends = {}
for i in range(4):
    name = input("Enter the name of your friend : ")
    language = input("Enter the language your friend speaks : ")
    friends[name] = language

print(friends)
print(type(friends))

print(friends["Sabuj"])# find keys in dictionary