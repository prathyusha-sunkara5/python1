# user_module.py

# Step 1: Parent Class
class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


# Step 2: Student Class (inherits User)
class Student(User):
    def __init__(self, name, id, dept, fees):
        super().__init__(name, id)   # calling User constructor
        self.dept = dept
        self.fees = fees


# Step 3: Faculty Class (inherits User)
class Faculty(User):
    def __init__(self, name, id, salary):
        super().__init__(name, id)   # calling User constructor
        self.salary = salary


# Step 4: TempFaculty Class (inherits Faculty)
class TempFaculty(Faculty):
    def __init__(self, name, id, salary, duration):
        super().__init__(name, id, salary)  # calling Faculty constructor
        self.duration = duration