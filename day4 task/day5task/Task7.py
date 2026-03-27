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

file.close()

print("File written successfully")
print("Is file closed?", file.closed)
