import httpx
from tools.fakers import get_random_email

# Используем рабочий порт локального сервера курса
BASE_URL = "http://localhost:8001"


def main():
    # Генерируем случайный email для регистрации
    registration_email = get_random_email()

    # --- ШАГ 1: Создание пользователя (POST /api/v1/users) ---
    create_url = f"{BASE_URL}/api/v1/users"
    create_payload = {
        "email": registration_email,
        "password": "SecurePassword123",
        "lastName": "Иванов",
        "firstName": "Иван",
        "middleName": "Иванович"
    }
    create_response = httpx.post(create_url, json=create_payload)
    print(f"Шаг 1 (Создание) - Статус: {create_response.status_code}")

    # Извлекаем id созданного пользователя
    user_id = create_response.json()["user"]["id"]

    # --- ШАГ 2: Авторизация (POST /api/v1/authentication/login) ---
    login_url = f"{BASE_URL}/api/v1/authentication/login"
    login_payload = {
        "email": registration_email,
        "password": "SecurePassword123"
    }
    login_response = httpx.post(login_url, json=login_payload)
    print(f"Шаг 2 (Авторизация) - Статус: {login_response.status_code}")

    # Извлекаем accessToken из вложенного словаря token
    access_token = login_response.json()["token"]["accessToken"]

    # --- ШАГ 3: Обновление пользователя (PATCH /api/v1/users/{user_id}) ---
    update_url = f"{BASE_URL}/api/v1/users/{user_id}"

    # Генерируем НОВЫЙ случайный email для обновления
    updated_email = get_random_email()

    update_payload = {
        "email": updated_email,
        "lastName": "Петров",
        "firstName": "Пётр",
        "middleName": "Петрович"
    }

    # Передаем токен в заголовке для авторизации PATCH-запроса
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    update_response = httpx.patch(update_url, json=update_payload, headers=headers)
    print(f"Шаг 3 (Обновление) - Статус: {update_response.status_code}")

    # Выводим финальный JSON-ответ в консоль
    print("\nФинальный JSON-ответ:")
    print(update_response.json())


if __name__ == "__main__":
    main()
