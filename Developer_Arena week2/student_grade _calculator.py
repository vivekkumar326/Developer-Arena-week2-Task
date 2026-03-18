# ==========================================
#  Student Grade Calculator
# ==========================================

def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print(" Invalid input! Marks must be between 0 and 100.")
        except ValueError:
            print(" Please enter a valid number!")


def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! "
    elif marks >= 80:
        return "B", "Very Good! Keep it up! "
    elif marks >= 70:
        return "C", "Good job! You can do even better! "
    elif marks >= 60:
        return "D", "Keep trying! Practice more! "
    else:
        return "F", "Don't give up! Work harder next time! "


def main():
    print(" Welcome to Student Grade Calculator\n")

    name = input("Enter student name: ").upper()
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n RESULT FOR", name + ":")
    print("Marks:", marks, "/100")
    print("Grade:", grade)
    print("Message:", message)


# Run the program
if __name__ == "__main__":
    main()