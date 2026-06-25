# write a program using function to find the gratest of three numbers
a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

def number(a,b,c):
    if(a == b == c ):
        print(f"{a},{b},{c} are equal")
    elif(a>b and a>c and a>0):
        print(f"{a} is the greatest number")
    elif(b>a and b>c and b>0 ):
        print(f"{c} is the gratest number")
    elif(c > 0):
        print(f"{c} is the greatest number ")
    else:
        print("You have entered a nagetive number !!")
    
number(a,b,c)  

number(a,b,c) 
'''
number(a,b,c) 
number(a,b,c) 
number(a,b,c)
'''
