import socket


def screen(server_address, server_port, num):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_address, server_port))
        print(f"Подключение к серверу {server_address}:{server_port} установлено.")
        s.send(f"get_screenshot|{num}".encode())
        result = s.recv(1024).decode()
        print(result)
        s.close()
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def kill_process(server_address, server_port, taskname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_address, server_port))
        print(f"Подключение к серверу {server_address}:{server_port} установлено.")
        s.send(f"kill_task|{taskname}".encode())
        result = s.recv(1024).decode()
        print(result)
        s.close()
    except Exception as e:
        print(f"Произошла ошибка: {e}")


def weblink(server_address, server_port, url):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server_address, server_port))
        print(f"Подключение к серверу {server_address}:{server_port} установлено.")
        s.send(f"weblink|{url}".encode())
        result = s.recv(1024).decode()
        print(result)
        s.close()
    except Exception as e:
        print(f"Произошла ошибка: {e}")


server_ip_address = '127.0.0.1'
server_port = 12345

commands = {
    "1": kill_process,
    "2": weblink,
    "3": screen,
}

while True:
    print("Выберите команду:")
    print("1. Убить процесс")
    print("2. Открыть ссылку")
    print("3. Сделать скриншот")
    choice = input("Введите цифру команды: ")
    if choice not in commands:
        print("Неверный выбор команды. Попробуйте еще раз.")
        continue

    if choice == "1":
        process_name = input('Процесс: \n')
        commands[choice](server_ip_address, server_port, f"{process_name}.exe")
    elif choice == "2":
        url1 = input('Ссылка: \n')
        kill_process(server_ip_address, server_port, f"{url1}")
    elif choice == "3":
        number = input('Число')
        commands[choice](server_ip_address, server_port, f"{number}")
    else:
        print("Неверный выбор команды. Попробуйте еще раз.")
        continue
