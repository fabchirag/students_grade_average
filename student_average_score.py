number_of_students = int(input())
student_details = {}

for i in range(number_of_students):
    student_name = input("Enter student name: ")
    grades = []
    for j in range(3):
        grade = int(input("Enter your grades: "))
        grades.append(grade)
    student_details[student_name] = grades

print(number_of_students)
for key, value in student_details.items():
    print(key, *value, sep=" ")

for key, value in student_details.items():
    query = input("Enter the student name: ")
    print(query)
    if query in student_details.keys():
        average = sum(value) / (len(value))
        print("{:.2f}".format(average))
        break