import os
from validator import validate_marks, is_duplicate_roll
from algorithms import calculate_average, find_topper_and_lowest, assign_grade
from storage import load_records, save_records

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'students.csv')

def display_menu():
    print("\n" + "=" * 45)
    print("   STUDENT PERFORMANCE MANAGEMENT SYSTEM")
    print("=" * 45)
    print("1. Add New Student")
    print("2. Display All Student Records")
    print("3. Search Student by Roll Number")
    print("4. View Performance Analytics (Mean, Max, Min)")
    print("5. Save & Exit")
    print("=" * 45)

def main():
    records = load_records(DATA_PATH)

    while True:
        display_menu()
        choice = input("Enter choice (1-5): ").strip()

        if choice == '1':
            roll = input("Enter Roll Number: ").strip()
            if is_duplicate_roll(roll, records):
                print("[ERROR] Roll number already exists.")
                continue
            name = input("Enter Student Name: ").strip()
            if not name:
                print("[ERROR] Name cannot be blank.")
                continue
            raw_score = input("Enter Marks (0-100): ").strip()
            is_valid, score = validate_marks(raw_score)
            if not is_valid:
                print("[ERROR] Invalid marks. Enter a number between 0 and 100.")
                continue
            records[roll] = {'name': name, 'marks': score}
            save_records(DATA_PATH, records)  
            print(f"[SUCCESS] Record for {name} added and saved to CSV.")
        elif choice == '2':
            if not records:
                print("[INFO] No student records available.")
            else:
                print("\n{:<15} {:<20} {:<10} {:<6}".format("Roll No", "Name", "Marks", "Grade"))
                print("-" * 55)
                for roll, data in records.items():
                    grade = assign_grade(data['marks'])
                    print("{:<15} {:<20} {:<10} {:<6}".format(roll, data['name'], data['marks'], grade))

        elif choice == '3':
            query = input("Enter Roll Number to search: ").strip()
            if query in records:
                student = records[query]
                grade = assign_grade(student['marks'])
                print(f"\nFound: {student['name']} | Marks: {student['marks']} | Grade: {grade}")
            else:
                print("[INFO] No student found with that Roll Number.")

        elif choice == '4':
            if not records:
                print("[INFO] Not enough data to compute statistics.")
                continue
            scores = [info['marks'] for info in records.values()]
            avg = calculate_average(scores)
            topper, lowest = find_topper_and_lowest(records)
            print("\n--- Cohort Analytics ---")
            print(f"Total Enrolled : {len(records)}")
            print(f"Class Average  : {avg}")
            print(f"Top Performer  : {topper[1]['name']} ({topper[0]}) - {topper[1]['marks']} marks")
            print(f"Lowest Score   : {lowest[1]['name']} ({lowest[0]}) - {lowest[1]['marks']} marks")

        elif choice == '5':
            save_records(DATA_PATH, records)
            print("[INFO] All changes saved to CSV. Program terminated.")
            break
        else:
            print("[ERROR] Invalid selection. Choose options 1 through 5.")

if __name__ == '__main__':
    main()