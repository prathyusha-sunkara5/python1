#Task 5: Combined Task (Real-Time)
class User:
    users_count = 0
 
    def __init__(self, name, pwd):
        self.__name = name
        self.__pwd = pwd
        User.users_count += 1
 
    def get_name(self):
        return self.__name
   
    def register(self):
        print(f"{self.__name} registered")
        return self
 
    def login(self):
        print(f"{self.__name} logged in")
        return self
   
    def greet(self):
        print("Welcome User")
        return self
   
class Student(User):
    def greet(self):
        print("Welcome Student")
        return self
   
class Faculty(User):
    def greet(self):
        print("welcome Faculty")
        return self
   
 
s1 = Student("Ammu", "8106")
f1 = Faculty("admin", "admin1234")
 
s1.login().greet().register()
f1.login().greet().register()
 
print("Total Users:", User.users_count)