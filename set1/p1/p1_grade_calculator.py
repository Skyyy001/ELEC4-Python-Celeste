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


# Test the computing functions.
if __name__ == "__main__":
    sample_grades = [90, 85, 88, 92, 95]

    print("Student: Antonio Caracas Celeste")
    print("Average:", calculate_average(sample_grades))
    print("Highest:", get_highest_grade(sample_grades))
    print("Lowest:", get_lowest_grade(sample_grades))
    print("Status:", determine_status(sample_grades))