import socket
import os
from metods import kill_task, weblink, get_screenshot

port = 5555


def main():
    host = '0.0.0.0'
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        data = conn.recv(1024).decode()
        if not data:
            break
        params = data.split('|')
        if params[0] == 'kill_process':
            result = kill_task(params[1])
        elif params[0] == 'weblink':
            result = weblink(params[1])
        elif params[0] == 'get_screenshot':
            result = get_screenshot(params[1])
        else:
            result = "Invalid command"
        conn.send(result.encode())
        conn.close()


if __name__ == '__main__':
    main()
