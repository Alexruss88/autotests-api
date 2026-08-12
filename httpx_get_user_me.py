import httpx

# 1. Учетные данные пользователя для авторизации
payload = {
    "email": "my_test_user@example.com",
    "password": "StrongPassword123"
}

# Используем рабочий порт локального сервера, который мы настроили ранее
BASE_URL = "http://localhost:8001"


def main():
    # --- ШАГ 1: Авторизация и получение accessToken ---
    login_url = f"{BASE_URL}/api/v1/authentication/login"
    login_response = httpx.post(login_url, json=payload)

    # Извлекаем JSON-данные ответа
    login_data = login_response.json()
    print("Ответ сервера:", login_data)

    # Достаем accessToken (FastAPI использует camelCase для токенов)
    access_token = login_data["token"]["accessToken"]

    # --- ШАГ 2: Запрос профиля пользователя с токеном в заголовке ---
    me_url = f"{BASE_URL}/api/v1/users/me"

    # Формируем заголовок авторизации по ТЗ
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    me_response = httpx.get(me_url, headers=headers)

    # --- ШАГ 3: Вывод JSON-ответа и статус-кода в консоль ---
    print(me_response.json())
    print(f"Статус код ответа: {me_response.status_code}")


if __name__ == "__main__":
    main()
