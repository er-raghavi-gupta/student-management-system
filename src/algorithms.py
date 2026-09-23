def calculate_average(marks):
    """Calculates class mean score using summation and counting (CSE1021 Unit 3)."""
    if not marks:
        return 0.0
    return round(sum(marks) / len(marks), 2)

def find_topper_and_lowest(student_data):
    """Finds highest and lowest performers in the records (CSE1021 Unit 5)."""
    if not student_data:
        return None, None
    topper = max(student_data.items(), key=lambda item: item[1]['marks'])
    lowest = min(student_data.items(), key=lambda item: item[1]['marks'])
    return topper, lowest

def assign_grade(marks):
    """Assigns letter grade based on conditional branching (CSE1021 Unit 3)."""
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    elif marks >= 60:
        return 'D'
    elif marks >= 50:
        return 'E'
    else:
        return 'F'