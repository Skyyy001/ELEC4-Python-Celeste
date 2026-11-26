# Full Name: Antonio Caracas Celeste
# Section: IV-BSIT-A
# Activity: P1 - Student Grade Calculator
# Date: November 26, 2026

PASSING_GRADE = 75


# Calculate the average grade.
def calculate_average(grades):
    return sum(grades) / len(grades)


# Find the highest grade.
def get_highest_grade(grades):
    return max(grades)


# Find the lowest grade.
def get_lowest_grade(grades):
    return min(grades)


# Determine the pass or fail status.
def determine_status(grades):
    average = calculate_average(grades)

    if average >= PASSING_GRADE:
        return "PASSED"
    else:
        return "FAILED"

# Accept and validate student grades.
def enter_grades():
    grades = []

    while True:
        try:
            count = int(input("Enter number of grades: "))

            if count > 0:
                break

            print("Enter at least one grade.")

        except ValueError:
            print("Please enter a whole number.")

    for i in range(count):
        while True:
            try:
                grade = float(input(f"Enter grade {i + 1}: "))

                if 0 <= grade <= 100:
                    grades.append(grade)
                    break

                print("Grade must be from 0 to 100.")

            except ValueError:
                print("Please enter a valid number.")

    return grades

   # Display the computed grade results.
def display_results(grades):
    if not grades:
        print("No grades entered yet.")
        return

    print("\n===== GRADE RESULTS =====")
    print(f"Average: {calculate_average(grades):.2f}")
    print(f"Highest: {get_highest_grade(grades):.2f}")
    print(f"Lowest: {get_lowest_grade(grades):.2f}")
    print(f"Status: {determine_status(grades)}")

# Main menu of the program.
def main():
    grades = []

    print("==============================")
    print("   STUDENT GRADE CALCULATOR")
    print("==============================")
    print("Student: Antonio Caracas Celeste")
    print("Section: IV-BSIT-A")

    while True:
        print("\n===== MAIN MENU =====")
        print("[1] Enter Grades")
        print("[2] View Results")
        print("[3] Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            grades = enter_grades()
            print("Grades saved successfully!")

        elif choice == "2":
            display_results(grades)

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()