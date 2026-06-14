'''Write a python program of this pattern
   *
  ***
 *****  
  ***
   *
'''
num = int(input("Enter a number: "))

for i in range(num):
    for j in range(num-1-i):
        print(" ", end="")
    for k in range (2*i+1):
        print("*", end="")
    print()
for i in range(num-2, -1, -1):
    for j in range(num-1-i):
        print(" ", end="")
    for k in range (2*i+1):
        print("*", end="")
    print()