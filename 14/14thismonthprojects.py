import datetime
import sqlite3

conn = sqlite3.connect('task_management.db')
cursor = conn.cursor()

current_month = datetime.datetime.now().month
cursor.execute("SELECT * FROM Задачи WHERE strftime('%m', сроки) = ?", (str(current_month),))
tasks = cursor.fetchall()

for task in tasks:
    print(task)

conn.close()
