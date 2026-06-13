#pass or fail
#assume that the total marks are 100 and passing marks is 40. Also, a student has to pass in all three subjects separately. So, if a student fails in any one of the subjects, then he/she will be considered as failed.

a = int(input("Enter your marks of Math: "))

b = int(input("Enter your marks of Science: "))
c = int(input("Enter your marks of English: "))

d = a+b+c

e = (d/100)*100

if(e >= 40 and a >= 33 and b >= 33 and c >= 33):
    print("Congratulations! You have passed the exam.")
else:    print("Sorry! You have failed the exam.")