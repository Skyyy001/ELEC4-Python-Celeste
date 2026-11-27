# Full Name: Antonio Caracas Celeste
# Section: IV-BSIT-A
# Activity: P4 - Safe Menu Program
# Date: November 27, 2026


# Perform division and handle possible errors.
def divide_numbers():
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))

        result = first_number / second_number

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print(f"Result: {result:.2f}")

    finally:
        print("Division operation finished.")

# Open a text file and handle possible errors.
def open_file():
    filename = input("Enter file name: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            contents = file.read()

    except FileNotFoundError:
        print("Error: File not found.")

    except PermissionError:
        print("Error: Permission denied.")

    except UnicodeError:
        print("Error: Unable to read the text file.")

    except (OSError, ValueError):
        print("Error: Unable to open the file.")

    else:
        print("\n===== FILE CONTENTS =====")
        print(contents)

    finally:
        print("File operation finished.")

# Main menu of the program.
def main():
    while True:
        print("\n===== SAFE MENU PROGRAM =====")
        print("Student: Antonio Caracas Celeste")
        print("Section: IV-BSIT-A")
        print("[1] Divide Numbers")
        print("[2] Open File")
        print("[3] Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    