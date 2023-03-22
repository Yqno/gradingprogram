student_scores = {
"Yuno": 81,
"Asta": 78,
"Goku": 99,
"Beerus": 74,
"Guts": 62,
}

# Create a empty dictionary called student_grates
student_grades = {}

# Write your code below to add the grades to student_grades
for student in student_scores:
    score = student_scores[student] 
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
            student_grades[student] = "Exceeds Expectations"
    elif score > 70:
            student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"                


print(student_grades)        
