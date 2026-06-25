def fibonacci_recursive(n):
    
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

n = int(input("Enter the number: "))
print(f"Fibonacci of {n}th number is {fibonacci_recursive(n)}")