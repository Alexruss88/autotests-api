from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client


class User(TypedDict):
    """Описание структуры пользователя."""
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserRequestDict(TypedDict):
    """Описание структуры запроса на создание пользователя."""
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str


class CreateUserResponseDict(TypedDict):
    """Описание структуры ответа создания пользователя."""
    user: User


class PublicUsersClient(APIClient):
    """Публичный класс для взаимодействия с API пользователей."""

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """Метод отправляет POST-запрос на создание пользователя."""
        return self.post("/api/v1/users", json=request)

    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        """Метод создает пользователя и автоматически возвращает распакованный JSON."""
        response = self.create_user_api(request)
        return response.json()


def get_public_users_client() -> PublicUsersClient:
    """Функция создаёт экземпляр PublicUsersClient с настроенным HTTP-клиентом."""
    return PublicUsersClient(client=get_public_http_client())
