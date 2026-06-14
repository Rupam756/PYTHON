# find the sum of first n natural numbers

num = int(input("Enter a number: "))

sum = 0
for i in range(1, num+1):

    print(i)
    sum += i
print(f"The sum of first {num} natural numbers is: {sum}")