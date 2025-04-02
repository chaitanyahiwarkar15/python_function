# function to find percentage and grade 

def percentage_and_grade(marks):
    total_marks = sum(marks)
    percentage = total_marks/len(marks)
    if percentage > 90:
        grade = 'A+'
    elif percentage >= 60:
        grade = 'A'
    elif percentage >= 50:
        grade = 'B' 
    elif percentage >= 35:
        grade = 'C'

    else:
        grade =  'Fail'

    return percentage, grade

marks = [90,75,68,78,48,30,28,91,88,65]
percentage , grade = percentage_and_grade(marks)                 

print("Kitne percentage mile ", percentage )
print ("konsa grade mila ", grade )