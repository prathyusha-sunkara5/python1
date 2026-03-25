# 4 login
# Login & User Validation System
# Concepts: Dictionary, Condition
# Basic authentication system.
# Requirements:
# Store users (username & password)
# Take login input
# Validate credentials
# Print success or failure message?


# Dictionary to store username and password
users = {
    "admin": "1234",
    "ravi": "pass123",
    "sita": "welcome"
}
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    if username in users:
        if users[username] == password:
            print(" Login Successful!")
        else:
            print(" Incorrect Password")
    else:
        print(" Username not found")
print("===== Login System =====")
login()
