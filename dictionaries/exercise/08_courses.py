def main():
    courses = {}

    while True:
        input_line = input()
        if input_line.lower() == "end":
            break

        course_name, student_name = input_line.split(" : ")

        if course_name not in courses:
            courses[course_name] = []
        courses[course_name].append(student_name)

    for course, students in courses.items():
        print(f"{course}: {len(students)}")
        for student in students:
            print(f"-- {student}")


if __name__ == "__main__":
    main()
