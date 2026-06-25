# Write a recursive function to calculate sum of first n number

def sum(n):
    if(n == 1):
        return 1
    return sum(n-1) + n

n = int(input("Enter the nth number : "))

print(f"Sum of {n}th number is ",sum(n))