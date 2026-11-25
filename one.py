import json
import os

FILE_NAME = "attendance.txt"


def load_data():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_data(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    roll = input("Enter roll number: ").strip()

    if roll in students:
        print("Student already exists.")
        return

    name = input("Enter student name: ").strip()

    if not roll or not name:
        print("Roll number and name cannot be empty.")
        return

    students[roll] = {"name": name, "attendance": []}
    save_data(students)
    print("Student added successfully.")


def mark_attendance(students):
    roll = input("Enter roll number: ").strip()

    if roll not in students:
        print("Student not found.")
        return

    status = input("Enter P for Present or A for Absent: ").strip().upper()

    if status not in ("P", "A"):
        print("Invalid attendance status.")
        return

    students[roll]["attendance"].append(status)
    save_data(students)
    print("Attendance marked successfully.")


def calculate_percentage(records):
    if not records:
        return 0
    present = records.count("P")
    return (present / len(records)) * 100


def view_attendance(students):
    if not students:
        print("No students found.")
        return

    print("\n--- Attendance Report ---")
    for roll, details in students.items():
        records = details["attendance"]
        percentage = calculate_percentage(records)
        print(
            f"Roll: {roll} | Name: {details['name']} | "
            f"Attendance: {percentage:.2f}% "
            f"({records.count('P')}/{len(records)})"
        )


def shortage_list(students):
    print("\n--- Students Below 75% ---")
    found = False

    for roll, details in students.items():
        percentage = calculate_percentage(details["attendance"])

        if percentage < 75:
            print(f"{roll} - {details['name']} ({percentage:.2f}%)")
            found = True

    if not found:
        print("No students below 75%.")


def main():
    students = load_data()

    while True:
        print("\n===== STUDENT ATTENDANCE MANAGER =====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. Show Shortage List")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            mark_attendance(students)
        elif choice == "3":
            view_attendance(students)
        elif choice == "4":
            shortage_list(students)
        elif choice == "5":
            print("Thank you for using Student Attendance Manager!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()