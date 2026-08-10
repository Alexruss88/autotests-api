import socket

# Список для хранения всей истории сообщений от клиентов
messages_history = []


def start_server():
    # 1. Создаем TCP-сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Позволяет повторно использовать порт сразу после перезапуска сервера
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. Привязываем сервер к localhost и порту 12345
    server_socket.bind(("localhost", 12345))

    # 3. Устанавливаем очередь в 10 одновременных подключений
    server_socket.listen(10)
    print("TCP-сервер запущен и ожидает подключений на порту 12345...")

    while True:
        # 4. Принимаем новое подключение клиента
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")

        try:
            while True:
                # 5. Ожидаем сообщение от клиента (буфер 1024 байта)
                data = client_socket.recv(1024)

                # Если данные не пришли, значит клиент разорвал соединение
                if not data:
                    break

                # Декодируем байты в строку
                message = data.decode("utf-8").strip()

                # 5.1 Выводим в лог полученное сообщение
                print(
                    f"Пользователь с адресом: {client_address} отправил сообщение: {message}"
                )

                # 5.2 Добавляем сообщение в общий список истории
                messages_history.append(message)

                # 5.3 Формируем всю историю сообщений, объединяя их через новую строку
                history_response = "\n".join(messages_history)

                # Отправляем историю обратно клиенту, закодировав её в байты
                client_socket.sendall(history_response.encode("utf-8"))

        except ConnectionResetError:
            # Обработка ситуации, если клиент резко закрыл программу
            print(f"Клиент {client_address} резко оборвал соединение")
        finally:
            # Обязательно закрываем сокет текущего клиента после выхода из цикла
            client_socket.close()
            print(f"Соединение с {client_address} закрыто")


if __name__ == "__main__":
    start_server()
