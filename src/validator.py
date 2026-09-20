def validate_marks(raw_marks):
    """Validates that entered marks are a valid number between 0 and 100."""
    try:
        score = float(raw_marks)
        if 0.0 <= score <= 100.0:
            return True, score
        return False, 0.0
    except ValueError:
        return False, 0.0

def is_duplicate_roll(roll_no, records):
    """Checks if a roll number already exists in the records dictionary."""
    return str(roll_no).strip() in records