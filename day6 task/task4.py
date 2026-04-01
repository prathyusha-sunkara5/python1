#Task 4: Method Chaining
 
class User:
    def register(self):
        print("Registered")
        return self
   
    def login(self):
        print("Logined")
        return self
 
    def greet(self):
        print("Enjoy Everyone")
        return self
   
user = User()
user.login().greet().register()