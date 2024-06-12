import sqlite3

conn = sqlite3.connect('task_management.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Проекты (
        project_id INTEGER PRIMARY KEY,
        название TEXT,
        описание TEXT,
        статус TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Задачи (
        task_id INTEGER PRIMARY KEY,
        project_id INTEGER,
        описание TEXT,
        статус_выполнения TEXT,
        сроки TEXT,
        FOREIGN KEY (project_id) REFERENCES Проекты (project_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Исполнители (
        performer_id INTEGER PRIMARY KEY,
        task_id INTEGER,
        имя TEXT,
        контактные_данные TEXT,
        FOREIGN KEY (task_id) REFERENCES Задачи (task_id)
    )
''')

conn.commit()
conn.close()

print("База данных и таблицы успешно созданы.")
