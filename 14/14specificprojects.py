import sqlite3
conn = sqlite3.connect('task_management.db')
cursor = conn.cursor()

project_id = 1
cursor.execute("SELECT * FROM Задачи WHERE project_id=?", (project_id,))
tasks = cursor.fetchall()

for task in tasks:
    print(task)

conn.close()
