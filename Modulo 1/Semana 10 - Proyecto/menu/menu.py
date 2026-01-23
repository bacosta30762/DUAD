import actions.students as st
import actions.notes as nt

def show_menu():
    print("\n Student management system")
    print("Select operation:")
    print("1. Add Student")
    print("2. Students list")
    print("3. Top 3 average notes")
    print("4. Average note of all students")
    print("5. Export CSV")
    print("6. Import CSV")
    print("0. Exit")


def menu(students):
    while True:
        show_menu()

        choice = input("Enter choice (0/1/2/3/4/5/6): ")

        if choice == '0':
            print("Exiting program...")
            break

        if choice not in ['1', '2', '3', '4', '5', '6']:
            print("Invalid option. Try again.")
            continue

        if choice == '1':
            while True:
                student = st.create_student()
                students.append(student)  
                create_student = input("Add more students? (y or n): ")

                if create_student == 'n':
                    print("Showing menu...")
                    break

                if choice not in ['n']:
                    print("Adding another student.")
                    continue

        if choice == '2':
            st.show_all_students(students)

        if choice == '3':
            nt.top3_average_students(students)

        if choice == '4':
            nt.average_grades_students(students)



