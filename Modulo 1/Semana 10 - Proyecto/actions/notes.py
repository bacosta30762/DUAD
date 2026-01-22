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