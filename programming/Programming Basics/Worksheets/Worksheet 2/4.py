exam = int(input("What was your score (1-100): "))
attendance = int(input("What is your attendance score (1-100): "))
if attendance > 90: 
    if exam > 90:
        grade = "A"
    elif exam > 80:
        grade = "B"
    elif exam > 70:
        grade = "C"
    else: 
        grade = "D"
else: 
    grade = "Fail"

print(grade)


