def classify_grade(percentage: int):
    if percentage >= 90:
        Grade = "A"
    elif percentage >= 80:
        Grade = "B"
    elif percentage >= 70:
        Grade = "C"
    elif percentage >= 60:
        Grade = "D"
    else:
        Grade = "Fail"
    return Grade

# Test the function
print(classify_grade(85))
