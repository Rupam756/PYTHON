'''write a python program to show "S" pattern of * using for loop '''

num = int(input("Enter a number: "))

for i in range(num):
    for j in range(num):
        if(i==0 or i==num-1 or i==num//2 or j==0 and i>num//2 or j==num-1 and i<num//2):
            print("*", end="")
        else:
            print(" ", end="")
    print()