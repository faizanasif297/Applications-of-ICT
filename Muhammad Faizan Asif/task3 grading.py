marks = int (input("Enter your marks:"))
grade = "Invalid"
if marks>=90 and marks<=100:
    grade = "A"
elif marks>=75 and marks <90:
    grade = "B"
elif marks>=60:
    grade = "C"
elif marks>50 and marks<60:
    grade = ""
elif marks<50:
    grade = "F"
else:
    print ("invalid") 

print("Grade:", grade)