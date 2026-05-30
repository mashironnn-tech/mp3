# ============================================
# MACHINE PROBLEM #3 - GRADEBOOK MANAGER (UPDATED)
# ============================================

students = {}
categories = {}


def add_student():
    print("\n=== ADD STUDENT ===")
    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty!")
        return

    if student_id in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ").strip()
    students[student_id] = {
        "name": name,
        "grades": {}
    }
    print("Student added successfully!")


def create_category():
    print("\n=== CREATE GRADING CATEGORY ===")
    category = input("Enter Category Name: ").strip()
    
    if not category:
        print("Category name cannot be empty!")
        return

    try:
        weight = float(input("Enter Weight Percentage (e.g., 20): "))
        categories[category] = weight
        print("Category added successfully!")
    except ValueError:
        print("Invalid input! Weight must be a number.")


def enter_grade():
    print("\n=== ENTER GRADE ===")
    student_id = input("Enter Student ID: ").strip()

    if student_id not in students:
        print("Student not found!")
        return

    category = input("Enter Category: ").strip()

    if category not in categories:
        print("Category does not exist!")
        return

    try:
        grade = float(input("Enter Grade: "))
        if category not in students[student_id]["grades"]:
            students[student_id]["grades"][category] = []
        
        students[student_id]["grades"][category].append(grade)
        print("Grade entered successfully!")
    except ValueError:
        print("Invalid input! Grade must be a number.")

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
    if grade >= 90: return "A"
    elif grade >= 80: return "B"
    elif grade >= 70: return "C"
    elif grade >= 60: return "D"
    else: return "F"


def view_report_card():
    print("\n=== REPORT CARD ===")
    student_id = input("Enter Student ID: ").strip()

    if student_id not in students:
        print("Student not found!")
        return

    print("-" * 50)
    print(f"Student ID   : {student_id}")
    print(f"Student Name : {students[student_id]['name']}")
    print("-" * 50)

    student_grades = students[student_id]["grades"]
    
    # Check if they have actual elements inside their grades tracking
    has_any_grades = any(len(g) > 0 for g in student_grades.values())
    
    if not has_any_grades:
        print("No grades recorded for this student yet.")
        print("-" * 50)
        return

    for category, grades in student_grades.items():
        if grades:  # Ensure list isn't empty
            average = sum(grades) / len(grades)
            print(f"{category} Average : {average:.2f}")

    final_grade = calculate_final_grade(student_id)
    print("-" * 50)
    print(f"Final Grade  : {final_grade:.2f}")
    print(f"Letter Grade : {letter_grade(final_grade)}")


def grade_statistics():
    print("\n=== GRADE DISTRIBUTION ===")

    if not students:
        print("No students available!")
        return

    total = []
    print("Active Student Grades Summary:")
    print("-" * 45)
    
    for student_id, info in students.items():
        # Verify the student has at least one actual numerical grade entered
        has_grades = any(len(grades_list) > 0 for grades_list in info["grades"].values())
        
        if has_grades:
            final = calculate_final_grade(student_id)
            total.append(final)
            print(f"ID: {student_id:<6} | Name: {info['name']:<12} | Final Grade: {final:.2f}")
        else:
            print(f"ID: {student_id:<6} | Name: {info['name']:<12} | [No Grades Recorded]")

    print("-" * 45)

    if not total:
        print("No grades have been entered for any student yet!")
        return

    average = sum(total) / len(total)
    highest = max(total)
    lowest = min(total)

    print(f"Class Average : {average:.2f}")
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


# ============================================
# MAIN INTERFACE LOOP
# ============================================
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

    choice = input("Enter Choice: ").strip()

    if choice == "1": add_student()
    elif choice == "2": create_category()
    elif choice == "3": enter_grade()
    elif choice == "4": view_report_card()
    elif choice == "5": grade_statistics()
    elif choice == "6": view_students()
    elif choice == "7":
        print("Thank you for using the Gradebook Manager!")
        break
    else:
        print("Invalid choice!")