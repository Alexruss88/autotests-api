# import httpx
# from clients.users.public_users_client import PublicUsersClient, UserCreateRequest
#
# base_client = httpx.Client(base_url="http://localhost:8001")
# users_client = PublicUsersClient(base_client)
#
# payload: UserCreateRequest = {
#     "username": "test_user_123",
#     "email": "test@example.com",
#     "password": "StrongPassword123!",
#     "firstName": "Ivan",
#     "lastName": "Ivanov",
#     "middleName": "Petrovich"
# }
#
# response = users_client.create_user_api(payload)
# print(response.status_code)
# try:
#     print(response.json())
# except ValueError:
#     print(response.text)


import httpx
import time
from clients.users.public_users_client import PublicUsersClient, UserCreateRequest

# 1. Подготовка данных (динамические значения для уникальности)
timestamp = int(time.time())
payload: UserCreateRequest = {
    "username": f"test_user_{timestamp}",
    "email": f"test_{timestamp}@example.com",
    "password": "StrongPassword123!",
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "middleName": "Petrovich"
}

# 2. Инициализация клиента
base_client = httpx.Client(base_url="http://localhost:8001")
users_client = PublicUsersClient(base_client)

try:
    # 3. Отправка запроса
    response = users_client.create_user_api(payload)

    # --- БЛОК ПРОВЕРОК (ASSERT) ---

    # Проверяем статус код
    assert response.status_code == 200, f"Ожидался статус 200, но получен {response.status_code}. Ответ сервера: {response.text}"

    # Парсим JSON (если сервер вернул не JSON, это тоже ошибка)
    data = response.json()

    # Проверяем, что структура ответа верная (есть ключ 'user')
    assert "user" in data, "В ответе отсутствует ключ 'user'"

    user_data = data["user"]

    # Проверяем совпадение отправленных данных с полученными
    assert user_data.get("email") == payload[
        "email"], f"Email не совпадает. Ожидалось: {payload['email']}, получено: {user_data.get('email')}"
    assert user_data.get("lastName") == payload[
        "lastName"], f"Фамилия не совпадает. Ожидалось: {payload['lastName']}, получено: {user_data.get('lastName')}"
    assert user_data.get("firstName") == payload[
        "firstName"], f"Имя не совпадает. Ожидалось: {payload['firstName']}, получено: {user_data.get('firstName')}"

    # Проверяем наличие ID и его формат (простая проверка, что он не пустой)
    assert "id" in user_data and user_data["id"], "Отсутствует ID пользователя в ответе"

    # -----------------------------

    # 4. Вывод в консоль (только если все assert прошли)
    print("✅ Тест пройден успешно!")
    print(f"Создан пользователь: {user_data['id']}")
    print(f"Данные: {data}")

except AssertionError as e:
    # Если проверка не прошла, выводим понятную ошибку и прерываем
    print(f"❌ Тест упал с ошибкой проверки: {e}")
    raise e
except Exception as e:
    # Ловим любые другие ошибки (сеть, JSON decode error и т.д.)
    print(f"❌ Произошла непредвиденная ошибка: {e}")
    raise e
finally:
    # 5. Закрываем клиент (важно, чтобы не было утечек соединений)
    base_client.close()

