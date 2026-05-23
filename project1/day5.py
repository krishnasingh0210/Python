# ============================================================
#         STUDENT MANAGEMENT SYSTEM - CUI PROJECT
#           Created by: Krishna Singh | Python Project
# ============================================================

import os
import json
import random
import datetime

# ─────────────────────────────────────────────────────────────
#  FILE SETTINGS
# ─────────────────────────────────────────────────────────────
DATA_FILE = "Studentrecords.json"
SUBJECTS = ["Maths", "Science", "English", "SST", "Hindi"]
TOTAL_MARKS = 100  # marks per subject
MAX_MARKS = TOTAL_MARKS * len(SUBJECTS)  # 500


# ─────────────────────────────────────────────────────────────
#  UTILITY FUNCTIONS
# ─────────────────────────────────────────────────────────────

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input("\n  Press ENTER to continue...")


def separator(char="═", width=55):
    print("  " + char * width)


def header(title):
    clear_screen()
    separator()
    print(f"  {'STUDENT MANAGEMENT SYSTEM':^55}")
    separator()
    print(f"  {title:^55}")
    separator()
    print()


def success(msg):
    print(f"\n  ✔  {msg}")


def error(msg):
    print(f"\n  ✘  ERROR: {msg}")


def info(msg):
    print(f"\n  ℹ  {msg}")


# ─────────────────────────────────────────────────────────────
#  DATA FUNCTIONS
# ─────────────────────────────────────────────────────────────

def load_data():
    """Load student records from JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)    
        except json.JSONDecodeError:
            error("Data file is corrupted. Starting with empty records.")
            return {}
    return {}


def save_data(records):
    """Save student records to JSON file."""
    with open(DATA_FILE, "w") as f:
        json.dump(records, f, indent=4)


def generate_roll_no(records):
    """Generate a unique 6-digit roll number."""
    while True:
        roll = str(random.randint(100000, 999999))
        if roll not in records:
            return roll


def get_grade(percentage):
    """Return grade based on percentage."""
    if percentage >= 90:
        return "A+ (Outstanding)"
    elif percentage >= 80:
        return "A  (Excellent)"
    elif percentage >= 70:
        return "B+ (Very Good)"
    elif percentage >= 60:
        return "B  (Good)"
    elif percentage >= 50:
        return "C  (Average)"
    elif percentage >= 33:
        return "D  (Below Average)"
    else:
        return "F  (Fail)"


def get_status(percentage):
    """Return Pass/Fail based on percentage."""
    return "Pass" if percentage >= 33 else "Fail"


def calculate_result(student):
    """Calculate percentage, grade and status for a student."""
    obtained = sum(student.get(sub, 0) for sub in SUBJECTS)
    percentage = round((obtained / MAX_MARKS) * 100, 2)
    return obtained, percentage, get_grade(percentage), get_status(percentage)


def validate_marks(marks_input, subject):
    """Validate that marks are between 0 and 100."""
    try:
        marks = int(marks_input)
        if 0 <= marks <= TOTAL_MARKS:
            return marks
        else:
            error(f"Marks for {subject} must be between 0 and {TOTAL_MARKS}.")
            return None
    except ValueError:
        error(f"Invalid input for {subject}. Please enter a number.")
        return None


# ─────────────────────────────────────────────────────────────
#  FEATURE FUNCTIONS
# ─────────────────────────────────────────────────────────────

def register_student(records):
    """Register a new student."""
    header("📋  REGISTER NEW STUDENT")

    name = input("  Enter Student Name       : ").strip()
    if not name:
        error("Name cannot be empty.")
        pause()
        return

    # Check for duplicate name
    for data in records.values():
        if data["Name"].lower() == name.lower():
            error(f"A student named '{name}' already exists.")
            pause()
            return

    # Age
    try:
        age = int(input("  Enter Age                : "))
        if not (5 <= age <= 25):
            error("Age must be between 5 and 25.")
            pause()
            return
    except ValueError:
        error("Age must be a number.")
        pause()
        return

    # Class
    try:
        cls = int(input("  Enter Class (1-12)       : "))
        if not (1 <= cls <= 12):
            error("Class must be between 1 and 12.")
            pause()
            return
    except ValueError:
        error("Class must be a number.")
        pause()
        return

    roll_no = generate_roll_no(records)
    enrolled_date = datetime.date.today().strftime("%d-%m-%Y")

    records[roll_no] = {
        "Name": name,
        "Age": age,
        "Class": cls,
        "Enrolled": enrolled_date,
        "Maths": None,
        "Science": None,
        "English": None,
        "SST": None,
        "Hindi": None,
        "Percentage": None,
        "Grade": None,
        "Status": "Pending"
    }

    save_data(records)
    separator("-")
    success(f"Student '{name}' registered successfully!")
    print(f"  🎫  Roll Number : {roll_no}")
    print(f"  📅  Enrolled On : {enrolled_date}")
    separator("-")
    pause()


def enter_marks(records):
    """Enter marks for a student by roll number."""
    header("📝  ENTER STUDENT MARKS")

    roll_no = input("  Enter Roll Number        : ").strip()
    if roll_no not in records:
        error(f"No student found with Roll Number '{roll_no}'.")
        pause()
        return

    student = records[roll_no]
    print(f"\n  Student  : {student['Name']}")
    print(f"  Class    : {student['Class']}")
    separator("-")
    print(f"  Enter marks out of {TOTAL_MARKS} for each subject:\n")

    new_marks = {}
    for subject in SUBJECTS:
        while True:
            raw = input(f"  {subject:<10}: ")
            marks = validate_marks(raw, subject)
            if marks is not None:
                new_marks[subject] = marks
                break

    # Update records
    for subject, marks in new_marks.items():
        records[roll_no][subject] = marks

    # Auto-calculate result
    obtained, percentage, grade, status = calculate_result(records[roll_no])
    records[roll_no]["Percentage"] = percentage
    records[roll_no]["Grade"] = grade
    records[roll_no]["Status"] = status

    save_data(records)
    separator("-")
    success("Marks saved successfully!")
    print(f"  📊  Percentage : {percentage}%")
    print(f"  🏆  Grade      : {grade}")
    print(f"  📌  Status     : {status}")
    separator("-")
    pause()


def view_report_card(records):
    """Display a detailed report card for a student."""
    header("📄  STUDENT REPORT CARD")

    roll_no = input("  Enter Roll Number        : ").strip()
    if roll_no not in records:
        error(f"No student found with Roll Number '{roll_no}'.")
        pause()
        return

    s = records[roll_no]

    # Check if marks have been entered
    if s["Status"] == "Pending":
        info("Marks have not been entered for this student yet.")
        pause()
        return

    obtained, percentage, grade, status = calculate_result(s)

    separator()
    print(f"  {'REPORT CARD':^55}")
    separator()
    print(f"  Name       : {s['Name']}")
    print(f"  Roll No.   : {roll_no}")
    print(f"  Age        : {s['Age']}")
    print(f"  Class      : {s['Class']}")
    print(f"  Enrolled   : {s.get('Enrolled', 'N/A')}")
    separator("-")
    print(f"  {'Subject':<15} {'Marks Obtained':>15} {'Max Marks':>12}")
    separator("-")
    for subject in SUBJECTS:
        marks = s.get(subject, 0) or 0
        print(f"  {subject:<15} {marks:>15} {TOTAL_MARKS:>12}")
    separator("-")
    print(f"  {'Total':<15} {obtained:>15} {MAX_MARKS:>12}")
    separator()
    print(f"  Percentage : {percentage}%")
    print(f"  Grade      : {grade}")
    print(f"  Result     : {'🎉 PASS' if status == 'Pass' else '❌ FAIL'}")
    separator()
    pause()


def view_all_students(records):
    """Display all registered students in a table."""
    header("👥  ALL STUDENTS LIST")

    if not records:
        info("No students are registered yet.")
        pause()
        return

    print(f"  {'Roll No.':<12} {'Name':<20} {'Class':<8} {'Status':<12} {'Percentage'}")
    separator("-")
    for roll, data in records.items():
        pct = f"{data['Percentage']}%" if data.get("Percentage") is not None else "N/A"
        print(f"  {roll:<12} {data['Name']:<20} {data['Class']:<8} {data['Status']:<12} {pct}")

    separator("-")
    print(f"\n  Total Students: {len(records)}")
    pause()


def search_student(records):
    """Search for a student by roll number or name."""
    header("🔍  SEARCH STUDENT")

    print("  Search by:")
    print("  [1] Roll Number")
    print("  [2] Name")
    choice = input("\n  Enter Choice             : ").strip()

    if choice == "1":
        roll_no = input("  Enter Roll Number        : ").strip()
        if roll_no in records:
            _display_student_summary(roll_no, records[roll_no])
        else:
            error(f"No student found with Roll Number '{roll_no}'.")

    elif choice == "2":
        name = input("  Enter Name (partial OK)  : ").strip().lower()
        found = {r: d for r, d in records.items() if name in d["Name"].lower()}
        if found:
            print(f"\n  Found {len(found)} result(s):\n")
            separator("-")
            for roll, data in found.items():
                _display_student_summary(roll, data)
                separator("-")
        else:
            error(f"No student found with name matching '{name}'.")
    else:
        error("Invalid choice.")

    pause()


def _display_student_summary(roll_no, data):
    """Helper to display a student's summary."""
    pct = f"{data['Percentage']}%" if data.get("Percentage") is not None else "Not Calculated"
    grade = data.get("Grade") or "N/A"
    print(f"\n  Roll No.   : {roll_no}")
    print(f"  Name       : {data['Name']}")
    print(f"  Age        : {data['Age']}")
    print(f"  Class      : {data['Class']}")
    print(f"  Enrolled   : {data.get('Enrolled', 'N/A')}")
    print(f"  Percentage : {pct}")
    print(f"  Grade      : {grade}")
    print(f"  Status     : {data['Status']}")


def update_student(records):
    """Update a student's personal details."""
    header("✏️   UPDATE STUDENT DETAILS")

    roll_no = input("  Enter Roll Number        : ").strip()
    if roll_no not in records:
        error(f"No student found with Roll Number '{roll_no}'.")
        pause()
        return

    student = records[roll_no]
    print(f"\n  Current Name  : {student['Name']}")
    print(f"  Current Age   : {student['Age']}")
    print(f"  Current Class : {student['Class']}")
    separator("-")
    print("  (Press ENTER to keep current value)\n")

    new_name = input(f"  New Name [{student['Name']}]  : ").strip()
    new_age  = input(f"  New Age  [{student['Age']}]   : ").strip()
    new_cls  = input(f"  New Class[{student['Class']}]  : ").strip()

    if new_name:
        records[roll_no]["Name"] = new_name
    if new_age:
        try:
            age = int(new_age)
            if 5 <= age <= 25:
                records[roll_no]["Age"] = age
            else:
                error("Age must be between 5 and 25. Skipping age update.")
        except ValueError:
            error("Invalid age. Skipping age update.")
    if new_cls:
        try:
            cls = int(new_cls)
            if 1 <= cls <= 12:
                records[roll_no]["Class"] = cls
            else:
                error("Class must be 1-12. Skipping class update.")
        except ValueError:
            error("Invalid class. Skipping class update.")

    save_data(records)
    success(f"Student '{records[roll_no]['Name']}' updated successfully!")
    pause()


def delete_student(records):
    """Delete a student record."""
    header("🗑️   DELETE STUDENT RECORD")

    roll_no = input("  Enter Roll Number        : ").strip()
    if roll_no not in records:
        error(f"No student found with Roll Number '{roll_no}'.")
        pause()
        return

    student = records[roll_no]
    print(f"\n  Student to delete  : {student['Name']} (Class {student['Class']})")
    confirm = input("  Are you sure? (yes/no) : ").strip().lower()

    if confirm == "yes":
        del records[roll_no]
        save_data(records)
        success(f"Student '{student['Name']}' deleted successfully.")
    else:
        info("Deletion cancelled.")

    pause()


def class_topper(records):
    """Display the class topper (highest percentage)."""
    header("🏆  CLASS TOPPER")

    graded = {r: d for r, d in records.items() if d.get("Percentage") is not None}

    if not graded:
        info("No results have been calculated yet.")
        pause()
        return

    # Group by class
    classes = {}
    for roll, data in graded.items():
        cls = data["Class"]
        if cls not in classes:
            classes[cls] = []
        classes[cls].append((roll, data))

    for cls in sorted(classes.keys()):
        topper_roll, topper = max(classes[cls], key=lambda x: x[1]["Percentage"])
        print(f"\n  Class {cls} Topper:")
        separator("-")
        print(f"  Name       : {topper['Name']}")
        print(f"  Roll No.   : {topper_roll}")
        print(f"  Percentage : {topper['Percentage']}%")
        print(f"  Grade      : {topper['Grade']}")

    separator()
    pause()


def statistics(records):
    """Show overall statistics."""
    header("📊  STATISTICS")

    total = len(records)
    if total == 0:
        info("No students registered yet.")
        pause()
        return

    graded = [d for d in records.values() if d.get("Percentage") is not None]
    passed = [d for d in graded if d["Status"] == "Pass"]
    failed = [d for d in graded if d["Status"] == "Fail"]

    avg_pct = round(sum(d["Percentage"] for d in graded) / len(graded), 2) if graded else 0

    print(f"  Total Students Registered : {total}")
    print(f"  Results Calculated        : {len(graded)}")
    print(f"  Pending Results           : {total - len(graded)}")
    separator("-")
    print(f"  Passed                    : {len(passed)}")
    print(f"  Failed                    : {len(failed)}")
    print(f"  Pass Rate                 : {round(len(passed)/len(graded)*100, 2) if graded else 0}%")
    separator("-")
    print(f"  Average Percentage        : {avg_pct}%")

    if graded:
        best = max(graded, key=lambda d: d["Percentage"])
        worst = min(graded, key=lambda d: d["Percentage"])
        print(f"  Highest Score             : {best['Percentage']}% ({best['Name']})")
        print(f"  Lowest Score              : {worst['Percentage']}% ({worst['Name']})")

    separator()
    pause()


# ─────────────────────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────────────────────

def show_menu():
    header("MAIN MENU")
    print("  [1]  Register New Student")
    print("  [2]  Enter / Update Marks")
    print("  [3]  View Report Card")
    print("  [4]  View All Students")
    print("  [5]  Search Student")
    print("  [6]  Update Student Details")
    print("  [7]  Delete Student Record")
    print("  [8]  Class Topper")
    print("  [9]  Statistics")
    separator("-")
    print("  [0]  Exit")
    separator()


def main():
    records = load_data()

    while True:
        show_menu()
        try:
            choice = input("  Enter your choice        : ").strip()
        except KeyboardInterrupt:
            clear_screen()
            print("\n  Goodbye! 👋\n")
            break

        if   choice == "1":  register_student(records)
        elif choice == "2":  enter_marks(records)
        elif choice == "3":  view_report_card(records)
        elif choice == "4":  view_all_students(records)
        elif choice == "5":  search_student(records)
        elif choice == "6":  update_student(records)
        elif choice == "7":  delete_student(records)
        elif choice == "8":  class_topper(records)
        elif choice == "9":  statistics(records)
        elif choice == "0":
            clear_screen()
            separator()
            print(f"  {'Thank you for using SMS!':^55}")
            print(f"  {'Goodbye! 👋':^55}")
            separator()
            print()
            break
        else:
            error("Invalid option. Please choose from the menu.")
            pause()


# ─────────────────────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()