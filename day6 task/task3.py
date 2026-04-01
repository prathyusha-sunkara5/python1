# Task 3: Method Overriding
 
class User:
    def greet(self):
        print("Welcome User")
 
class Student:
    def greet(self):
        print("Welcome Student")
 
class Faculty():
    def greet(self):
        print("Welcome Faculty")
 
 
s = Student()
f = Faculty()
 
s.greet()
f.greet()