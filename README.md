# student-management-system
Student Management System

A modular Python-based management and statistical analysis suite developed for **CSE1021: Introduction to Problem Solving and Programming** at VIT Bhopal.

## Features
* **Validation Engine:** Strict numeric bounds checking and duplicate roll number protection.
* **Analytical Computations:** Calculates class averages and extracts top/lowest scoring students.
* **Grade Assignment:** Categorizes marks into standardized academic letter grades.
* **CSV Persistence:** Automatically loads and writes records to a local CSV file.
* **Automated Unit Testing:** Includes test coverage for statistical functions.

## Technology Stack
* **Language:** Python 3
* **Storage:** Comma Separated Values (CSV)
* **Libraries:** Standard library (`csv`, `os`, `sys`)

## Project Structure
```text
Student_Management_System/
├── data/
│   └── students.csv
├── src/
│   ├── __init__.py
│   ├── validator.py
│   ├── algorithms.py
│   ├── storage.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_algorithms.py
├── README.md
├── statement.md
└── requirements.txt