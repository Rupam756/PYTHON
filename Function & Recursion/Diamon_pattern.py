def diamond(n):
    for i in range(1, n+1):
        print(" " * (n-i),end="")

        print("*" * (2 * i -1))
    for i in range(n-1 , 0,-1):
        print(" " * (n-i),end="")

        print("*" * (2 * i -1))


n = int(input("Enter the row : "))
diamond(n)