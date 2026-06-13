# take 8 numnber as input from user and display all the unique numbers ijn set

s = set()

for i in range(8):
    n = int(input("Enter the number : "))
    s.add(n)
print(s)
print(f"Unique numbers are : {s}")
