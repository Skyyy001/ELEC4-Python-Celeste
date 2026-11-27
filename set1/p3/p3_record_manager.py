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

# Remove a student from the list and set.
def remove_student(students, student_names, name):
    normalized_name = name.strip().casefold()

    for student in students:
        if student.casefold() == normalized_name:
            students.remove(student)
            student_names.remove(normalized_name)
            print(f"{student} removed successfully.")
            return

    print("Student not found.")

# Search students using a partial name.
def search_student(students, keyword):
    keyword = keyword.strip().casefold()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    matches = []

    for student in students:
        if keyword in student.casefold():
            matches.append(student)

    print("\n===== SEARCH RESULTS =====")
    print("Student: Antonio Caracas Celeste")

    if matches:
        for number, name in enumerate(
            sorted(matches, key=str.casefold), start=1
        ):
            print(f"{number}. {name}")

        print(f"Total matches: {len(matches)}")
    else:
        print("No matching students found.")

# Main menu of the student record manager.
def main():
    students = []
    student_names = set()

    print("==============================")
    print("    STUDENT RECORD MANAGER")
    print("==============================")
    print("Student: Antonio Caracas Celeste")
    print("Section: IV-BSIT-A")

    while True:
        print("\n===== MAIN MENU =====")
        print("Student: Antonio Caracas Celeste")
        print("[1] Add Student")
        print("[2] Remove Student")
        print("[3] Search Student")
        print("[4] Display All Students")
        print("[5] Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            add_student(students, student_names, name)

        elif choice == "2":
            name = input("Enter name to remove: ")
            remove_student(students, student_names, name)

        elif choice == "3":
            keyword = input("Enter name to search: ")
            search_student(students, keyword)

        elif choice == "4":
            display_students(students)

        elif choice == "5":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
