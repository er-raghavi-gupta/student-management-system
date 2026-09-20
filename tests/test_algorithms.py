import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from algorithms import calculate_average, assign_grade, find_topper_and_lowest

def test_average():
    assert calculate_average([80.0, 90.0, 100.0]) == 90.0
    assert calculate_average([]) == 0.0

def test_grade_assignment():
    assert assign_grade(95) == 'A'
    assert assign_grade(72) == 'C'
    assert assign_grade(45) == 'F'

def test_topper_and_lowest():
    sample = {
        '101': {'name': 'Alice', 'marks': 92.0},
        '102': {'name': 'Bob', 'marks': 54.0}
    }
    topper, lowest = find_topper_and_lowest(sample)
    assert topper[0] == '101'
    assert lowest[0] == '102'

if __name__ == '__main__':
    test_average()
    test_grade_assignment()
    test_topper_and_lowest()
    print("All unit tests passed successfully!")