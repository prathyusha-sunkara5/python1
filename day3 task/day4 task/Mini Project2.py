# 2
# Student Report Card System
# Concepts: Dictionary, Functions, Formatting
# Create a report system.
# Requirements:
# Store student name and marks (3 subjects)
# Calculate total and average
# Print formatted report card
# Display grade based on average?

# Function to calculate grade based on average
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B+"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "F"
def report_card():
    student = {}
    
    student['name'] = input("Enter student name: ")
    student['marks'] = {}
    
    subjects = ["Math", "Science", "English"]
    
    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        student['marks'][subject] = mark
    
    total = sum(student['marks'].values())
    average = total / len(subjects)
    grade = calculate_grade(average)
    
    print("\n===== Report Card =====")
    print(f"Student Name: {student['name']}")
    print("-" * 30)
    print(f"{'Subject':<10}{'Marks':>10}")
    for subject, mark in student['marks'].items():
        print(f"{subject:<10}{mark:>10}")
    print("-" * 30)
    print(f"{'Total':<10}{total:>10}")
    print(f"{'Average':<10}{average:>10.2f}")
    print(f"{'Grade':<10}{grade:>10}")
    print("-" * 30)
report_card()
