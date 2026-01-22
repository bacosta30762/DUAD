from notes import input_grade

def create_student():
    name = input("Enter full name: ")
    section = input("Enter section (example 7A): ")

    grades = {
        "spanish": input_grade("Spanish"),
        "english": input_grade("English"),
        "socials": input_grade("Socials"),
        "science": input_grade("Science")
    }

    student = {
        "name": name,
        "section": section,
        "grades": grades
    }

    return student