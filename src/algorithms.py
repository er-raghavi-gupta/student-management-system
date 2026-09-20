def calculate_average(scores):
    """Calculates class mean score using summation and counting (CSE1021 Unit 3)."""
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)

def find_topper_and_lowest(records):
    """Finds highest and lowest performers in the records (CSE1021 Unit 5)."""
    if not records:
        return None, None
    topper = max(records.items(), key=lambda item: item[1]['marks'])
    lowest = min(records.items(), key=lambda item: item[1]['marks'])
    return topper, lowest

def assign_grade(score):
    """Assigns letter grade based on conditional branching (CSE1021 Unit 3)."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    elif score >= 50:
        return 'E'
    else:
        return 'F'