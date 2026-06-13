# calculate the grade of a student based on their marks

marks = float(input("Enter the student's marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: Excellent")
elif marks >= 80 and marks < 89:
    print("Grade: Very Good")
elif marks >= 70 and marks < 79:
    print("Grade: Good")
elif marks >= 60 and marks < 69:
    print("Grade: Average") 
elif marks >= 50 and marks < 59:
    print("Grade: Pass")
elif marks >= 0 and marks < 49:
    print("Grade: Fail")