# Full Name: Antonio Caracas Celeste
# Section: IV-BSIT-A
# Activity: P2 - Custom Module
# Date: November 27, 2026

import student_utils
from student_utils import determine_status
from datetime import datetime


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


# Generate the student grade report.
def main():
    print("==============================")
    print("     STUDENT GRADE REPORT")
    print("==============================")
    print("Student: Antonio Caracas Celeste")
    print("Section: IV-BSIT-A")

    grades = enter_grades()

    print("\n===== GRADE RESULTS =====")
    print("Student: Antonio Caracas Celeste")
    print(f"Average: {student_utils.calculate_average(grades):.2f}")
    print(f"Highest: {student_utils.get_highest_grade(grades):.2f}")
    print(f"Lowest: {student_utils.get_lowest_grade(grades):.2f}")
    print(f"Status: {determine_status(grades)}")

    # Display the date and time of the report.
    report_date = datetime.now()
    print("Report generated:", report_date.strftime("%B %d, %Y - %I:%M %p"))


if __name__ == "__main__":
    main()
