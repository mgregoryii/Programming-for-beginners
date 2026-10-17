# =============================================================================
# Student Record Management System
# Programming Fundamentals with Python - Week 8 Refactoring Exercise
#
# This program reads student data from a CSV file and provides a menu-driven
# interface to list all students and search for a student by ID.
#
# NOTE TO STUDENTS: This program works correctly but is written in a "top-down"
# style with no functions and uses global variables. Your task is to refactor
# this program to make it more readable and maintainable by organizing the code
# into well-named functions and eliminating the use of global variables.
# =============================================================================



import csv


# Parent class representing a student
class Student:
    def __init__(self, student_id, student_name, major, gpa, total_credits):
        self.student_id = student_id.strip()
        self.student_name = student_name.strip()
        self.major = major.strip()
        self.gpa = gpa.strip()
        self.total_credits = total_credits.strip()

    def __str__(self):
        return (
            f"Student ID: {self.student_id}, "
            f"Name: {self.student_name}, "
            f"Major: {self.major}, "
            f"GPA: {self.gpa}, "
            f"Credits: {self.total_credits}"
        )


# Subclass representing a graduate student
class GraduateStudent(Student):
    def __init__(
        self, student_id, student_name, major, gpa,
        total_credits, thesis_topic
    ):
        # Initialize inherited attributes
        super().__init__(
            student_id, student_name, major, gpa, total_credits
        )

        # Add the graduate student's thesis topic
        self.thesis_topic = thesis_topic.strip()

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"Thesis Topic: {self.thesis_topic}"
        )


# Class that manages the student roster
class StudentRoster:
    REQUIRED_COLUMNS = [
        "StudentID", "StudentName", "Major", "GPA", "TotalCredits"
    ]

    def __init__(self):
        self.students = []
        self.csv_filename = ""
        self.csv_loaded = False

    def read_csv(self):
        self.csv_filename = input(
            "Enter the CSV filename (e.g., students.csv): "
        ).strip()

        new_students = []
        seen_ids = set()
        duplicate_count = 0
        skipped_count = 0

        try:
            with open(
                self.csv_filename,
                newline="",
                encoding="utf-8-sig"
            ) as csv_file:
                csv_reader = csv.DictReader(csv_file)

                if not csv_reader.fieldnames or not all(
                    column in csv_reader.fieldnames
                    for column in self.REQUIRED_COLUMNS
                ):
                    print("Error: CSV file has missing or incorrect headers.")
                    return

                for row in csv_reader:
                    # Check required fields
                    if not all(
                        str(row.get(column) or "").strip()
                        for column in self.REQUIRED_COLUMNS
                    ):
                        print("Warning: Skipping a row with missing data.")
                        skipped_count += 1
                        continue

                    # Create the appropriate student object
                    if "ThesisTopic" in csv_reader.fieldnames:
                        thesis_topic = str(
                            row.get("ThesisTopic") or ""
                        ).strip()

                        if thesis_topic:
                            student = GraduateStudent(
                                row["StudentID"],
                                row["StudentName"],
                                row["Major"],
                                row["GPA"],
                                row["TotalCredits"],
                                thesis_topic
                            )
                        else:
                            student = Student(
                                row["StudentID"],
                                row["StudentName"],
                                row["Major"],
                                row["GPA"],
                                row["TotalCredits"]
                            )
                    else:
                        student = Student(
                            row["StudentID"],
                            row["StudentName"],
                            row["Major"],
                            row["GPA"],
                            row["TotalCredits"]
                        )

                    # Check for duplicate student IDs
                    normalized_id = student.student_id.casefold()

                    if normalized_id in seen_ids:
                        print(
                            f"Warning: Duplicate Student ID "
                            f"'{student.student_id}' skipped."
                        )
                        duplicate_count += 1
                        continue

                    seen_ids.add(normalized_id)
                    new_students.append(student)

            self.students = new_students
            self.csv_loaded = bool(self.students)

            print()
            print(f"Successfully processed '{self.csv_filename}'.")
            print(f"Records loaded: {len(self.students)}")
            print(f"Duplicate records skipped: {duplicate_count}")
            print(f"Rows skipped for missing data: {skipped_count}")

            if not self.csv_loaded:
                print("No valid student records were loaded.")

        except FileNotFoundError:
            print("Error: CSV file not found.")
        except PermissionError:
            print("Error: You do not have permission to read this file.")
        except (csv.Error, OSError) as error:
            print(f"Error reading CSV file: {error}")

    def list_students(self):
        if not self.csv_loaded:
            print("No data loaded. Please use Option 1 to read a CSV file first.")
            return

        print()
        print("=" * 100)
        print("Student Roster")
        print("=" * 100)

        for number, student in enumerate(self.students, start=1):
            print(f"{number}. {student}")

        print("=" * 100)
        print(f"Total records: {len(self.students)}")

    def search_student(self):
        if not self.csv_loaded:
            print("No data loaded. Please use Option 1 to read a CSV file first.")
            return

        search_id = input("Enter the Student ID to search for: ").strip()

        found_student = None

        for student in self.students:
            if student.student_id.casefold() == search_id.casefold():
                found_student = student
                break

        print()

        if found_student is None:
            print(f"No student found with ID '{search_id}'.")
        else:
            print("Student found!")
            print("-" * 50)
            print(f"Student ID    : {found_student.student_id}")
            print(f"Student Name  : {found_student.student_name}")
            print(f"Major         : {found_student.major}")
            print(f"GPA           : {found_student.gpa}")
            print(f"Total Credits : {found_student.total_credits}")

            if isinstance(found_student, GraduateStudent):
                print(f"Thesis Topic  : {found_student.thesis_topic}")

            print("-" * 50)

    def run(self):
        print("=" * 60)
        print("   Student Record Management System")
        print("=" * 60)

        while True:
            print()
            print("Please select an option:")
            print("  1. Read CSV")
            print("  2. List CSV Contents")
            print("  3. Search for Student by ID")
            print("  4. Exit")
            print()

            menu_choice = input("Enter your choice (1-4): ").strip()

            if menu_choice == "1":
                self.read_csv()
            elif menu_choice == "2":
                self.list_students()
            elif menu_choice == "3":
                self.search_student()
            elif menu_choice == "4":
                print()
                print(
                    "Thank you for using the Student Record Management "
                    "System. Goodbye!"
                )
                break
            else:
                print()
                print(
                    f"'{menu_choice}' is not a valid option. "
                    "Please enter 1, 2, 3, or 4."
                )


# Main program
if __name__ == "__main__":
    roster = StudentRoster()
    roster.run()