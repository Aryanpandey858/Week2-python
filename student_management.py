"""Student Management System (Week 2 Mini Project).
Stores student data (roll number, name, marks) in a CSV file.
Features: add, delete, search, view all. Changes are saved permanently.
"""
import csv
import os

FILENAME = "students.csv"
FIELDS = ["roll_no", "name", "marks"]


def load_students():
    """Read all students from the CSV file into a list of dictionaries."""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_students(students):
    """Write the full list of students back to the CSV file."""
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)


def add_student():
    students = load_students()
    roll_no = input("Enter roll number: ").strip()
    if not roll_no:
        print("Roll number cannot be empty.")
        return
    if any(s["roll_no"] == roll_no for s in students):
        print("A student with this roll number already exists.")
        return

    name = input("Enter name: ").strip()
    try:
        marks = float(input("Enter marks (0-100): "))
    except ValueError:
        print("Marks must be a number.")
        return
    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    students.append({"roll_no": roll_no, "name": name, "marks": marks})
    save_students(students)
    print(f"Student '{name}' added and saved.")


def delete_student():
    students = load_students()
    roll_no = input("Enter roll number to delete: ").strip()
    remaining = [s for s in students if s["roll_no"] != roll_no]

    if len(remaining) == len(students):
        print("Student not found.")
        return
    save_students(remaining)
    print(f"Student with roll number {roll_no} deleted and saved.")


def search_student():
    students = load_students()
    keyword = input("Enter roll number or name to search: ").strip().lower()
    results = [
        s for s in students
        if keyword == s["roll_no"].lower() or keyword in s["name"].lower()
    ]

    if not results:
        print("No matching student found.")
        return
    print_table(results)


def view_students():
    students = load_students()
    if not students:
        print("No student records found.")
        return
    print_table(students)


def print_table(students):
    print(f"\n{'Roll No':<10}{'Name':<20}{'Marks':<10}")
    print("-" * 40)
    for s in students:
        print(f"{s['roll_no']:<10}{s['name']:<20}{s['marks']:<10}")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add student")
        print("2. Delete student")
        print("3. Search student")
        print("4. View all students")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            search_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()