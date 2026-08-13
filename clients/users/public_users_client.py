from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient


class UserCreateRequest(TypedDict):
    """
    Описание структуры запроса на создание пользователя.
    """
    username: str
    email: str
    password: str
    firstName: str
    lastName: str
    middleName: str


class PublicUsersClient(APIClient):
    """
    Клиент для работы с /api/v1/users
    """

    def create_user_api(self, request: UserCreateRequest) -> Response:
        """
        Метод создаёт нового пользователя.

        :param request: Словарь с полями username, email, password.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/users", json=request)

