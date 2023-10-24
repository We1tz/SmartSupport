import sqlite3
from tkinter import *
from tkinter import messagebox
import win32gui
from datetime import datetime
import telebot

bot_token = '5167808596:AAEpeOhuLDrZdhbJ13BsOCXOhOG8GkvoU_A'
chat_id = '1922232899'
pc = '№11'


bot = telebot.TeleBot(bot_token)




def verify_login(username, password):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM registrations WHERE login=? AND password=?", (username, password))
    result = c.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False




def update_last_login(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("UPDATE registrations SET last_login=? WHERE login=?", (now, username))
    conn.commit()
    conn.close()


def get_user_details(username):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM registrations WHERE login=?", (username,))
    result = c.fetchone()
    conn.close()
    return result


def block(event):
    if event.keysym in ['Alt_L', 'Tab', 'Super_L', 'Super_R']:
        return "break"


def check_password():
    username = username_entry.get()
    password = password_entry.get()
    if verify_login(username, password) or (username == 'admin' and password == '1237'):
        if username == 'admin' and password == '2585':
            screen.destroy()
            messagebox.showinfo("Admin Access", "Вы вошли как администратор")
        else:
            user_details = get_user_details(username)
            if user_details:
                first_name, last_name = user_details[0], user_details[1]
                update_last_login(username)  # Обновление даты последнего входа
                screen.withdraw()
                screen.destroy()
                messagebox.showinfo("Success", f"С успешной авторизацией, {first_name} {last_name}! Удачной работы :)")

                    # отправка оповещения

                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message_to_send = (f'Пользователь {username}, ({first_name} {last_name}) авторизовался. \n'
                                       f'\n'
                                       f'Дата входа: {now}, \n'
                                       f'\n'
                                       f'Направление - {user_details[5]}, \n'
                                       f'\n'
                                       f'Номер компьютера - {pc}.')
                bot.send_message(chat_id, message_to_send)
            else:
                    messagebox.showerror("Error", "Информация о пользователе не найдена")
                    screen.quit()  # Закрыть приложение после ошибки
    else:
            messagebox.showerror("Error", "Неправильное имя пользователя или пароль")


def check_focus():
    try:
        hwnd = win32gui.GetForegroundWindow()
        window_title = win32gui.GetWindowText(hwnd)
        if window_title != "Authorization Form":
            screen.attributes("-topmost", True)
            screen.attributes("-topmost", False)
    except:
        pass
    screen.after(100, check_focus)


screen = Tk()
screen.title("Authorization Form")
screen.attributes('-fullscreen', True)
screen.configure(background='white')

label_username = Label(screen, text="Имя пользователя", font=('Arial', 20), bg='white')
label_username.pack(pady=20)
username_entry = Entry(screen, font=('Arial', 20))
username_entry.pack()

label_password = Label(screen, text="Пароль", font=('Arial', 20), bg='white')
label_password.pack(pady=20)
password_entry = Entry(screen, show="*", font=('Arial', 20))
password_entry.pack()

submit_button = Button(screen, text="Войти", command=check_password, font=('Arial', 20), bg='blue', fg='white')
submit_button.pack(pady=20)

screen.bind("<Alt-KeyPress>", block)
screen.bind("<F4>", block)
screen.bind("<Control-Alt-Delete>", block)
screen.bind("<Command-q>", block)
screen.bind("<Tab>", block)
screen.bind("<Control-Tab>", block)
screen.bind("<Shift-Tab>", block)
screen.bind("<Control-Shift-Tab>", block)
screen.bind("<Alt-Tab>", block)
screen.bind("<Escape>", block)
screen.bind("<Alt-Escape>", block)
screen.bind("<Button-1>", block)
screen.bind("<Button-2>", block)
screen.bind("<Button-3>", block)
screen.protocol("WM_DELETE_WINDOW", block)

screen.after(100, check_focus)

screen.mainloop()
