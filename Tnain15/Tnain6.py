#Create a tuple of student names and their corresponding scores. Write a function to find the student with the highest score
students = ("jon", 4, "tom", 6, "bob", 8)
def student_with_highest_score(students):
    max_score = -1
    top_student = ""
    for i in range(1, len(students), 2):
        if students[i] > max_score:
            max_score = students[i]
            top_student = students[i - 1]
    return top_student, max_score
print(student_with_highest_score(students))
