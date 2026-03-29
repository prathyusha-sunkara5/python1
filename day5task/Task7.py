def create_user(name, age, role):
    return {
        "name": name.title(),
        "age": age,
        "role": role
    }


users = [
    create_user("ammu", 26, "developer"),
    create_user("deepu", 31, "designer"),
    create_user("pardhu", 24, "tester")
]


file = open("team_data.txt", "w")

for user in users:
    file.write(f"{user['name']}, {user['age']}, {user['role']}\n")

print("File written successfully")

file.close()

file = open("team_data.txt", "r")

# Read content
content = file.read()

# Display content
print(content)


file.close()
print("Is file closed?", file.closed)
