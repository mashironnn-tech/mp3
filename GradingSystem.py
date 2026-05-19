# ============================================
# MACHINE PROBLEM #3 - GRADEBOOK MANAGER
# ============================================

students = {}
categories = {}


def add_student():
    print("\n=== ADD STUDENT ===")

    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")

    students[student_id] = {
        "name": name,
        "grades": {}
    }

    print("Student added successfully!")


def create_category():
    print("\n=== CREATE GRADING CATEGORY ===")

    category = input("Enter Category Name: ")
    weight = float(input("Enter Weight Percentage: "))

    categories[category] = weight

    print("Category added successfully!")


def enter_grade():
    print("\n=== ENTER GRADE ===")

    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!")
        return

    category = input("Enter Category: ")

    if category not in categories:
        print("Category does not exist!")
        return

    grade = float(input("Enter Grade: "))

    if category not in students[student_id]["grades"]:
        students[student_id]["grades"][category] = []

    students[student_id]["grades"][category].append(grade)

    print("Grade entered successfully!")


def calculate_final_grade(student_id):
    total = 0

    for category, weight in categories.items():

        if category in students[student_id]["grades"]:

            grades = students[student_id]["grades"][category]

            average = sum(grades) / len(grades)

            weighted = average * (weight / 100)

            total += weighted

    return total


def letter_grade(grade):

    if grade >= 90:
        return "A"

    elif grade >= 80:
        return "B"

    elif grade >= 70:
        return "C"

    elif grade >= 60:
        return "D"

    else:
        return "F"


def view_report_card():
    print("\n=== REPORT CARD ===")

    student_id = input("Enter Student ID: ")

    if student_id not in students:
        print("Student not found!")
        return

    final_grade = calculate_final_grade(student_id)

    print("-" * 50)
    print(f"Student ID   : {student_id}")
    print(f"Student Name : {students[student_id]['name']}")

    for category, grades in students[student_id]["grades"].items():
        average = sum(grades) / len(grades)

        print(f"{category} Average : {average:.2f}")

    print(f"Final Grade  : {final_grade:.2f}")
    print(f"Letter Grade : {letter_grade(final_grade)}")


def grade_statistics():
    print("\n=== GRADE DISTRIBUTION ===")

    if not students:
        print("No students available!")
        return

    total = []

    for student_id in students:
        final = calculate_final_grade(student_id)
        total.append(final)

    average = sum(total) / len(total)

    highest = max(total)
    lowest = min(total)

    print(f"Average Grade : {average:.2f}")
    print(f"Highest Grade : {highest:.2f}")
    print(f"Lowest Grade  : {lowest:.2f}")


def view_students():
    print("\n=== STUDENT LIST ===")

    if not students:
        print("No students available!")
        return

    for student_id, info in students.items():
        print("-" * 40)
        print(f"Student ID   : {student_id}")
        print(f"Student Name : {info['name']}")


while True:
    print("\n" + "=" * 50)
    print("         GRADEBOOK MANAGER")
    print("=" * 50)
    print("[1] Add Student")
    print("[2] Create Category")
    print("[3] Enter Grade")
    print("[4] View Report Card")
    print("[5] Grade Statistics")
    print("[6] View Students")
    print("[7] Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        create_category()

    elif choice == "3":
        enter_grade()

    elif choice == "4":
        view_report_card()

    elif choice == "5":
        grade_statistics()

    elif choice == "6":
        view_students()

    elif choice == "7":
        print("Thank you for using the Gradebook Manager!")
        break

    else:
        print("Invalid choice!")