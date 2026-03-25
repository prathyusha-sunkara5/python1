#1
# Employee Management System
# Concepts: Dictionary, List, Functions
# Build a system to manage employees.
# Requirements:
# Store multiple employees (list of dictionaries)
# Each employee: name, age, role, salary
# Add new employee
# Update employee details
# Delete employee
# Display all employees?
# List to store multiple employees
employees = []
def add_employee():
    name = input("Enter employee name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))
    
    employee = {
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }
    
    employees.append(employee)
    print(" Employee added successfully!")
def update_employee():
    name = input("Enter the name of the employee to update: ")
    for emp in employees:
        if emp["name"].lower() == name.lower():
            emp["age"] = int(input("Enter new age: "))
            emp["role"] = input("Enter new role: ")
            emp["salary"] = float(input("Enter new salary: "))
            print(" Employee details updated!")
            return
    print(" Employee not found!")

def delete_employee():
    name = input("Enter the name of the employee to delete: ")
    for emp in employees:
        if emp["name"].lower() == name.lower():
            employees.remove(emp)
            print(" Employee deleted!")
            return
    print(" Employee not found!")

def display_employees():
    if not employees:
        print("No employees found.")
        return
    
    print("\n===== Employee List =====")
    print(f"{'Name':<15}{'Age':<5}{'Role':<15}{'Salary':<10}")
    print("-" * 45)
    for emp in employees:
        print(f"{emp['name']:<15}{emp['age']:<5}{emp['role']:<15}{emp['salary']:<10}")
    print("-" * 45)

while True:
    print("\n===== Employee Management Menu =====")
    print("1. Add Employee")
    print("2. Update Employee")
    print("3. Delete Employee")
    print("4. Display All Employees")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_employee()
    elif choice == "2":
        update_employee()
    elif choice == "3":
        delete_employee()
    elif choice == "4":
        display_employees()
    elif choice == "5":
        print(" Exiting Employee Management System")
        break
    else:
        print(" Invalid choice, try again!")
