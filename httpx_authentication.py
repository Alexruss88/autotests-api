
import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
payload = {
    "email": "my_test_user@example.com",
    "password": "StrongPassword123"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8001/api/v1/authentication/login", json=payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)

# Формируем payload для обновления токена
refresh_payload = {
    "refreshToken": login_response_data["token"]["refreshToken"]
}

# Выполняем запрос на обновление токена
refresh_response = httpx.post("http://localhost:8001/api/v1/authentication/refresh", json=refresh_payload)
refresh_response_data = refresh_response.json()

# Выводим обновленные токены
print("Refresh response:", refresh_response_data)
print("Status Code:", refresh_response.status_code)
