# 9.course enrollment system
# Concepts: List + Dictionary
# Manage student enrollments.
# Requirements:
# Add student with course list
# Update courses
# Display student details?
# Dictionary to store students and their courses
students = {}

def add_student():
    name = input("Enter student name: ")
    courses = input("Enter courses (comma-separated): ").split(",")
    
   
    courses = [course.strip() for course in courses]
    
    students[name] = courses
    print(" Student added successfully!")


def update_courses():
    name = input("Enter student name: ")
    
    if name in students:
        print(f"Current courses: {students[name]}")
        action = input("Add or Remove course? (add/remove): ").lower()
        
        if action == "add":
            course = input("Enter course to add: ")
            students[name].append(course)
            print(" Course added!")
        
        elif action == "remove":
            course = input("Enter course to remove: ")
            if course in students[name]:
                students[name].remove(course)
                print(" Course removed!")
            else:
                print(" Course not found")
        else:
            print(" Invalid action")
    else:
        print(" Student not found")


def display_students():
    if not students:
        print("No student records found.")
    else:
        print(" Student Details:")
        for name, courses in students.items():
            print(f"{name}: {', '.join(courses)}")
while True:
    print("\n===== Course Menu =====")
    print("1. Add Student")
    print("2. Update Courses")
    print("3. Display Students")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_student()
    elif choice == "2":
        update_courses()
    elif choice == "3":
        display_students()
    elif choice == "4":
        print(" Exiting system")
        break
    else:
        print(" Invalid choice")
