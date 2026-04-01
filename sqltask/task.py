import mysql.connector

conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Ammudeepu_01",
        port=3306,
        database="notes_db"
    )
cursor=conn.cursor()

#Create Note

# def create_note():
#     title = input("Enter title: ")
#     content = input("Enter content: ")

#     cursor.execute(
#         "INSERT INTO notes (title, content, created_at) VALUES (%s, %s, NOW())",
#         (title, content)
#     )
#     conn.commit()
# create_note()
    
# #View Notes 
# cursor.execute("SELECT * FROM notes_view ORDER BY title ASC");
# print(cursor.fetchall())

# #Search Notes
# title = input("Enter title: ")

# cursor.execute("SELECT * FROM notes WHERE title LIKE %s", ('%' + title + '%',))
# print(cursor.fetchall())

# #Update Note
# note_id = input("Enter note ID: ")
# new_title = input("Enter new title: ")
# new_content = input("Enter new content: ")

# cursor.execute(
#     "UPDATE notes SET title=%s, content=%s WHERE note_id=%s",
#     (new_title, new_content, note_id)
# )
# conn.commit()

# print("updated")

#Delete Note

title = input("Title: ")

cursor.execute("DELETE FROM notes WHERE title LIKE %s", ('%' + title + '%',))
conn.commit()

print("deleted")

   






     