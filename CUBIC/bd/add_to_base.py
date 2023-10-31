import sqlite3
from datetime import datetime

conn = sqlite3.connect('main.db')
cur = conn.cursor()
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# Функция для добавления пользователя
def add_user():
    first_name = input("Введите имя пользователя: ")
    last_name = input("Введите фамилию пользователя: ")
    login = input("Введите логин пользователя: ")
    password = input("Введите пароль пользователя: ")
    user_group = input("Введите группу пользователя: ")
    registration_date = now
    last_login_date = input("Введите дату последнего входа: ")

    cur.execute("INSERT INTO users (first_name, last_name, login, password, user_group, registration_date, last_login_date) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (first_name, last_name, login, password, user_group, registration_date, last_login_date))
    conn.commit()
    print("Пользователь успешно добавлен!")

# Вызов функции для добавления пользователя
add_user()

cur.close()
conn.close()
