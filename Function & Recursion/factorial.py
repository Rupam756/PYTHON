# write a factorial function that takes a number as input and returns the factorial using recursion.

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
# Example usage:
n = int(input("Enter a number to calculate its factorial: "))
print(f"The factorial of {n} is : {factorial(n)}")