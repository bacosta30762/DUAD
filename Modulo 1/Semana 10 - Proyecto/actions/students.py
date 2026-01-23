from actions.notes import input_grade
from actions.notes import average_grades_student

def create_student():
    name = input("Enter full name: ")
    section = input("Enter section (example 7A): ")

    grades = {
        "spanish": input_grade("Spanish"),
        "english": input_grade("English"),
        "socials": input_grade("Socials"),
        "science": input_grade("Science")
    }

    average = average_grades_student(
        grades["spanish"],
        grades["english"],
        grades["socials"],
        grades["science"])

    student = {
        "name": name,
        "section": section,
        "grades": grades,
        "average": average
    }

    return student

def show_student(student):
    print("\nStudent Information")
    print("-------------------")
    print(f"Name: {student['name']}")
    print(f"Section: {student['section']}")

    print("Grades:")
    for subject, grade in student["grades"].items():
        print(f"  {subject.capitalize()}: {grade}")

def show_all_students(students):
    if not students:
        print("No students registered")
        return
    
    for i, student in enumerate(students, start=1):
        print(f"\nStudent #{i}")
        show_student(student)