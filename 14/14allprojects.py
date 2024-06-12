import sqlite3
conn = sqlite3.connect('task_management.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Проекты")
projects = cursor.fetchall()

for project in projects:
    print(project)

conn.close()
