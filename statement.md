# Project Statement: Student Performance Management System

## 1. Problem Statement
Manual computation of academic grades and record keeping in introductory engineering courses is repetitive, error-prone, and vulnerable to accidental data corruption. Instructors need a lightweight, persistent, and modular tool to record marks, detect duplicate roll numbers, and instantly compute cohort statistics (mean, highest, and lowest performance).

## 2. Scope of the Project
This project provides a command-line interface (CLI) to record, validate, search, and statistically analyze student performance. It operates with zero external dependencies, utilizing native Python dictionaries for $O(1)$ fast lookups and CSV persistence for data retention across sessions.

## 3. Target Users
* Course Instructors and Faculty members.
* Teaching Assistants managing laboratory evaluations.
* Academic coordinators managing batch-level marks.

## 4. High-Level Features
* **Duplicate Detection:** Prevents overwriting existing roll numbers.
* **Input Validation:** Restricts mark inputs strictly between 0 and 100.
* **Algorithmic Analytics:** Calculates cohort average, topper, and lowest scorer.
* **Automated Grading:** Applies rule-based letter grades (A, B, C, D, E, F).
* **Persistent Storage:** Synchronizes in-memory records with `students.csv`.