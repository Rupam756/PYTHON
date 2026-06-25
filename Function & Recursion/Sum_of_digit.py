def sum_of_digits(n):

    if n == 0:
        return 0
    
    last_digits = n % 10

    remaining_num = n//10

    return last_digits + sum_of_digits(remaining_num)


n = int(input("Enter the number : "))

print(f"The sum of {n} is : {sum_of_digits(n)}")