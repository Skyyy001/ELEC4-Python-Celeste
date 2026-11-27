# Full Name: Antonio Caracas Celeste
# Section: IV-BSIT-A
# Activity: P2 - Custom Module
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
