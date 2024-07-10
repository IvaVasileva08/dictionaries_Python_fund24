n = int(input())

student_grades = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in student_grades:
        student_grades[name] = []

    student_grades[name].append(grade)

filtered_students = {}
for name, grades in student_grades.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        filtered_students[name] = average_grade

for name, average_grade in filtered_students.items():
    print(f"{name} -> {average_grade:.2f}")