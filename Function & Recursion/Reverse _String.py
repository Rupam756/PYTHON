def reverse_string(name):
    if name == "":
        return ""
    return reverse_string(name[1:]) + name[0]

name = str(input("Enter the text : "))
print(f"Reverse of {name} is {reverse_string(name)}")

