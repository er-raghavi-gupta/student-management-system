def calculate_average(marks):
   
    if not marks:
        return 0.0
    return round(sum(marks) / len(marks), 2)

def find_topper_and_lowest(student_data):
   
    if not student_data:
        return None, None
    topper = max(student_data.items(), key=lambda item: item[1]['marks'])
    lowest = min(student_data.items(), key=lambda item: item[1]['marks'])
    return topper, lowest

def assign_grade(marks):
   
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