import sqlite3
from faker import Faker
import random

conn = sqlite3.connect('task_management.db')
cursor = conn.cursor()

fake = Faker()
def populate_projects():
    for _ in range(5):
        название = fake.company()
        описание = fake.sentence()
        статус = random.choice(['В процессе', 'Завершен', 'Отложен'])
        cursor.execute("INSERT INTO Проекты (название, описание, статус) VALUES (?, ?, ?)",
                       (название, описание, статус))

def populate_tasks():
    for project_id in range(1, 6):
        for _ in range(random.randint(3, 7)):
            описание = fake.text()
            статус_выполнения = random.choice(['В работе', 'Выполнено', 'Отменено'])
            сроки = fake.date_time_this_year()
            cursor.execute("INSERT INTO Задачи (project_id, описание, статус_выполнения, сроки) VALUES (?, ?, ?, ?)",
                           (project_id, описание, статус_выполнения, сроки))

def populate_performers():
    for task_id in range(1, 21):
        имя = fake.name()
        контактные_данные = fake.email()
        cursor.execute("INSERT INTO Исполнители (task_id, имя, контактные_данные) VALUES (?, ?, ?)",
                       (task_id, имя, контактные_данные))

populate_projects()
populate_tasks()
populate_performers()
conn.commit()
conn.close()

print("Данные успешно добавлены в таблицы.")


