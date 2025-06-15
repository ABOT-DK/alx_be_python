student_name = input("Enter your name:")
marks_scored = float(input("Enter your marks to determine your grade:"))

if marks_scored >= 70:
    grade ='A'
    print("You have grade is:",grade)
    print("Excellent performance!")
elif marks_scored >= 60 and marks_scored < 70:
    grade = 'B'
    print("You have grade is:",grade)
    print("Very good performance!")
elif marks_scored >=50 and marks_scored < 60:
    grade = 'C'
    print("You have grade is:",grade)
    print("Good performance!")
elif marks_scored >= 40 and marks_scored < 50:
    grade = 'D'
    print("You have grade is:",grade)
    print("Average performance!")
else:
    grade = 'E'
    print("You have grade is:",grade)
    print("Poor performance!")