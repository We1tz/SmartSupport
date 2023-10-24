import sqlite3
from tkinter import *
from tkinter import messagebox
from datetime import datetime

conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS registrations 
             (first_name TEXT, last_name TEXT, login TEXT, password TEXT, registration_date TEXT, group_name TEXT, last_login TEXT)''')
conn.commit()
conn.close()

def add_registration():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    login = login_entry.get()
    password = password_entry.get()
    registration_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    group_name = group_entry.get()
    last_login = ""
    c.execute("INSERT INTO registrations (first_name, last_name, login, password, registration_date, group_name, last_login) VALUES (?, ?, ?, ?, ?, ?, ?)",
              (first_name, last_name, login, password, registration_date, group_name, last_login))
    conn.commit()
    conn.close()
    messagebox.showinfo("Успех", "Регистрация добавлена в базу данных")


def exit_application():
    registration_screen.destroy()


registration_screen = Tk()
registration_screen.title("Форма регистрации")
registration_screen.geometry("400x600")


label_first_name = Label(registration_screen, text="Имя", font=('Arial', 14))
label_first_name.pack(pady=10)
first_name_entry = Entry(registration_screen, font=('Arial', 12))
first_name_entry.pack()

label_last_name = Label(registration_screen, text="Фамилия", font=('Arial', 14))
label_last_name.pack(pady=10)
last_name_entry = Entry(registration_screen, font=('Arial', 12))
last_name_entry.pack()

label_login = Label(registration_screen, text="Логин", font=('Arial', 14))
label_login.pack(pady=10)
login_entry = Entry(registration_screen, font=('Arial', 12))
login_entry.pack()

label_password = Label(registration_screen, text="Пароль", font=('Arial', 14))
label_password.pack(pady=10)
password_entry = Entry(registration_screen, show="*", font=('Arial', 12))
password_entry.pack()

label_group = Label(registration_screen, text="Группа", font=('Arial', 14))
label_group.pack(pady=10)
group_entry = Entry(registration_screen, font=('Arial', 12))
group_entry.pack()

submit_button = Button(registration_screen, text="Зарегистрироваться", command=add_registration, font=('Arial', 12), bg='blue', fg='white')
submit_button.pack(pady=20)

exit_button = Button(registration_screen, text="Выход", command=exit_application, font=('Arial', 12), bg='red', fg='white')
exit_button.pack(pady=10)

registration_screen.mainloop()
