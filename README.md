# ELEC 4 - Python Programming

**Student:** Antonio Caracas Celeste  
**Section:** IV-BSIT-A  
**Course:** ELEC 4 - Python Programming

## Set 1 Activities

| Activity | Description | Folder |
| --- | --- | --- |
| P1 | Student Grade Calculator | [View Activity](set1/p1/) |
| P2 | Custom Module: student_utils | [View Activity](set1/p2/) |
| P3 | Student Record Manager | [View Activity](set1/p3/) |
| P4 | Safe Menu Program | [View Activity](set1/p4/) |

### P1 - Student Grade Calculator

A menu-driven Python program that accepts and validates
student grades, calculates the average, identifies the
highest and lowest grades, and determines the pass or
fail status.

**How to run:**

python set1/p1/p1_grade_calculator.py

**Program Output:**

![P1 Program Output](set1/p1/screenshots/P1_02_Passed_Results.png)


### P2 - Custom Module: student_utils

A modular Python program that uses reusable functions
to calculate the average, highest and lowest grades,
and determine the pass or fail status. It demonstrates
two import styles and uses the datetime module to
display the report generation date and time.

**Source Files:**

- student_utils.py - Contains reusable grade calculation functions.
- p2_main.py - Handles user input and displays the grade report.

**How to run:**

python set1/p2/p2_main.py

**Program Output:**

![P2 Program Output](set1/p2/screenshots/P2_01_Program_Output.png)

**Input Validation and Failed Results:**

![P2 Validation](set1/p2/screenshots/P2_02_Validation_and_Failed.png)

### P3 - Student Record Manager

A menu-driven Python program that manages student
names using lists and sets. It allows users to add,
remove, search, and display student records while
preventing duplicate entries.

**Features:**

- Add and remove student records.
- Case-insensitive duplicate prevention.
- Partial-name searching.
- Alphabetical display with numbering and total count.

***How to run:**

python set1/p3/p3_record_manager.py

**Adding Students:**

![Add Students](set1/p3/screenshots/P3_01_Add_Students.png)

**Duplicate Prevention:**

![Duplicate Prevention](set1/p3/screenshots/P3_02_Duplicate_Prevention.png)

**Display All Students:**

![Display Students](set1/p3/screenshots/P3_03_Display_Students.png)

**Search Student:**

![Search Student](set1/p3/screenshots/P3_04_Search_Student.png)

**Remove Student:**

![Remove Student](set1/p3/screenshots/P3_05_Remove_Student.png)

### P4 - Safe Menu Program

A menu-driven Python program that demonstrates
exception handling through division and file reading
operations. It handles invalid inputs and common
errors without interrupting the program.

**Features:**

- Division of two user-entered numbers.
- Invalid numeric input handling (ValueError).
- Division by zero handling (ZeroDivisionError).
- File reading and missing file handling (FileNotFoundError).
- Invalid menu selection handling.
- Demonstrates try, except, else, and finally.

**How to run:**

python set1/p4/p4_exceptions.py

For successful file reading, select option 2 and enter
set1/p4/sample.txt when running from the repository root.

**Invalid Numeric Input:**

![Invalid Number](set1/p4/screenshots/P4_01_Invalid_Number.png)

***Division by Zero:**

![Division by Zero](set1/p4/screenshots/P4_02_Division_By_Zero.png)

**File Not Found:**

![File Not Found](set1/p4/screenshots/P4_03_File_Not_Found.png)

***Invalid Menu Selection:**

![Invalid Menu](set1/p4/screenshots/P4_04_Invalid_Menu.png)

**Successful File Reading:**

![File Reading](set1/p4/screenshots/P4_05_Successful_File_Reading.png)

**Successful Division:**

![Successful Division](set1/p4/screenshots/P4_06_Successful_Division.png)