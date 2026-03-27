#  Task 1: User Info Manager (Functions + Dictionary)
# Create a function:
# def create_user(name, age, role):
# Return user as a dictionary
# Store multiple users in a list
# Print all users
# 👉 Add:
# Format names using .title()

def create_user(name, age, role):
    user = {
        "name": name.title(),   
        "age": age,
        "role": role
    }
    return user
users_list = []
user1 = create_user("prathyusha", 28, "admin")
user2 = create_user("pardhu", 32, "analyst")
user3 = create_user("deepu", 22, "lead")

users_list.append(user1)
users_list.append(user2)
users_list.append(user3)

for user in users_list:
    print(user)

