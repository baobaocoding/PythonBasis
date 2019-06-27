def getGradeAndGPA(score):
    """ Get grade and GPA from score value """
    if score >= 85:
        grade = "A"
        gpa = 4.0
    elif score >= 73:
        grade = "B"
        gpa = 3.0
    else:
        grade = "C"
        gpa = 2.0

    return grade, gpa


score = float(input("Please input your score:"))
grade, gpa = getGradeAndGPA(score)
print("Your grade is:", grade, "and your GPA is:", gpa)
