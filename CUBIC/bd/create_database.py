import sqlite3

# Создание подключения к базе данных SQLite
conn = sqlite3.connect('main.db')

# Создание курсора для выполнения операций
cur = conn.cursor()

# Создание таблицы
cur.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        login TEXT,
        password TEXT,
        user_group TEXT,
        registration_date TEXT,
        last_login_date TEXT
    )
''')

# Закрытие курсора и соединения с базой данных
cur.close()
conn.close()
