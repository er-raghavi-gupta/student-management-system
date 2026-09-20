import csv
import os

def load_records(filepath):
    """Reads student records from a CSV file into an in-memory dictionary."""
    records = {}
    if not os.path.exists(filepath):
        return records

    with open(filepath, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            records[row['roll_no']] = {
                'name': row['name'],
                'marks': float(row['marks'])
            }
    return records

def save_records(filepath, records):
    """Writes the dictionary records back to the CSV file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, mode='w', newline='', encoding='utf-8') as f:
        fieldnames = ['roll_no', 'name', 'marks']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for roll_no, info in records.items():
            writer.writerow({
                'roll_no': roll_no,
                'name': info['name'],
                'marks': info['marks']
            })