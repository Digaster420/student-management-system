# Student Management System
# Author: Swapnil
# Description: Add students, view list, calculate average marks.

students = {}

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter student marks (0-100): "))
    students[name] = marks
    print(f"{name} added successfully!\n")


def view_students():
    if not students:
        print("No students yet.\n")
        return
    print("Student List:")
    for name, marks in students.items():
        print(f"{name}: {marks}")
    print()


def calculate_average():
    if not students:
        print("No students to calculate average.\n")
        return
    avg = sum(students.values()) / len(students)
    print(f"Class average: {avg:.2f}\n")

while True:
    print("1. Add Student")
    print("2. View Students")
    print("3. Calculate Class Average")
    print("4. Exit")
    choice = input("Choose an option: ")
    
    
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.\n")