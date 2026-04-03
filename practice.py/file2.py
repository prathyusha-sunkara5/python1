# main.py

from file1 import User   # Import class from user.py

# Create object
u1 = User()

# Set user details
u1.set_user("john", "1234")

# Call methods
u1.register()
u1.login()

# Access username using getter
print("Username is:", u1.get_user())