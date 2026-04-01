#Task 2: Inheritance (User → Student, Faculty)
 
class User:
    def register(self):
        print("User Registered")
 
    def login(self):
        print("User Logged In")
 
class Student(User):
    def student_greet(self):
        print("Hi Student")
 
class Faculty(User):
    def faculty_greet(self):
        print("Hi Faculty")
 
class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")
 
s = Student()
s.register()
s.login()
s.student_greet()
 
f = Faculty()
f.register()
f.faculty_greet()
 
t = TempFaculty()
t.login()
t.faculty_greet()
t.tempFaculty_greet()
 

 
 


 