import socket


def start_client():
    # 1. Создаем клиентский TCP-сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. Подключаемся к серверу на localhost и порт 12345
    client_socket.connect(('localhost', 12345))

    # 3. Отправляем серверу сообщение "Привет, сервер!"
    message = "Как дела?"
    client_socket.send(message.encode('utf-8'))

    # 4. Получаем ответ от сервера (буфер 1024 байта) и выводим его в консоль
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

    # 5. Закрываем соединение
    client_socket.close()


if __name__ == '__main__':
    start_client()
