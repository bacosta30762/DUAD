def input_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter grade for {subject}"))
            if 0 <= grade <= 100:
                return grade

            else:
                print("Grade must be between 0 and 100")

        except ValueError:
            print("Please enter a valid number") 


def average_grades_student(spanish, english, socials, science):
    average = (spanish + english + socials + science)/4
    return average 


def top3_average_students(students):
    if len(students) == 0:
        print("There are no students registered")
        return
    
    top_3 = sorted(
        students,
        key=lambda student: student("average"),
        reverse=True
        )[:3]

    print("\nTop 3 students with better average:")
    for i, student in enumerate(top_3, start=1):
        print(f"{i}. {student["name"]} - Average: {student["average"]}")


def average_grades_students(students):
    if len(students) == 0:
        print("There are no students registered")
        return
    
    total_average = 0

    for student in students:
        total_average +- student["average"]

    overall_average = total_average / len(students)
    print(f"Average grade of all students: {overall_average}")
    