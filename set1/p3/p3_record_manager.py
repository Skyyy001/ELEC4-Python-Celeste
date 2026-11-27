# Full Name: Antonio Caracas Celeste
# Section: IV-BSIT-A
# Activity: P3 - Student Record Manager
# Date: November 27, 2026


# Add a student and prevent duplicate names.
def add_student(students, student_names, name):
    name = name.strip()

    if not name:
        print("Student name cannot be empty.")
        return

    normalized_name = name.casefold()

    if normalized_name in student_names:
        print("Student already exists.")
    else:
        students.append(name)
        student_names.add(normalized_name)
        print(f"{name} added successfully.")


# Display students in alphabetical order.
def display_students(students):
    print("\n===== STUDENT RECORDS =====")
    print("Student: Antonio Caracas Celeste")

    if not students:
        print("No student records available.")
    else:
        sorted_students = sorted(students, key=str.casefold)

        for number, name in enumerate(sorted_students, start=1):
            print(f"{number}. {name}")

    print(f"Total students: {len(students)}")


# Temporary test for adding and displaying students.
if __name__ == "__main__":
    students = []
    student_names = set()

    add_student(students, student_names, "Anna Dimagiba")
    add_student(students, student_names, "Rosa Bella")
    add_student(students, student_names, "Peter Pan")
    add_student(students, student_names, "John Paul")

    display_students(students)