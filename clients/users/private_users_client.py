
# from typing import TypedDict
# from httpx import Response
# from clients.api_client import APIClient
# from clients.private_http_builder import get_private_http_client, AuthenticationUserDict
#
#
# class User(TypedDict):
#     """Описание структуры пользователя."""
#     id: str
#     email: str
#     lastName: str
#     firstName: str
#     middleName: str
#
#
# class GetUserResponseDict(TypedDict):
#     """Описание структуры ответа получения пользователя."""
#     user: User
#
#
# class UpdateUserRequestDict(TypedDict):
#     """Описание структуры запроса на обновление пользователя."""
#     email: str | None
#     lastName: str | None
#     firstName: str | None
#     middleName: str | None
#
#
# class PrivateUsersClient(APIClient):
#     """Клиент для работы с /api/v1/users."""
#
#     def get_user_me_api(self) -> Response:
#         """Метод получения текущего пользователя."""
#         return self.get("/api/v1/users/me")
#
#     def get_user_api(self, user_id: str) -> Response:
#         """Метод получения пользователя по идентификатору."""
#         return self.get(f"/api/v1/users/{user_id}")
#
#     def update_user_api(self, user_id: str, request: UpdateUserRequestDict) -> Response:
#         """Метод обновления пользователя по идентификатору."""
#         return self.patch(f"/api/v1/users/{user_id}", json=request)
#
#     def delete_user_api(self, user_id: str) -> Response:
#         """Метод удаления пользователя по идентификатору."""
#         return self.delete(f"/api/v1/users/{user_id}")
#
#     def get_user(self, user_id: str) -> GetUserResponseDict:
#         """Метод получает пользователя и автоматически возвращает распакованный JSON."""
#         response = self.get_user_api(user_id)
#         return response.json()
#
#
# def get_private_users_client(user: AuthenticationUserDict) -> PrivateUsersClient:
#     """Функция создаёт экземпляр PrivateUsersClient с уже настроенным HTTP-клиентом."""
#     return PrivateUsersClient(client=get_private_http_client(user))



from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from .users_schema import UserSchema, GetUserResponseSchema, UpdateUserRequestSchema


class PrivateUsersClient(APIClient):
    """Клиент для работы с /api/v1/users (приватный)."""

    def get_user_me_api(self) -> Response:
        return self.get("/api/v1/users/me")

    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    def update_user_api(self, user_id: str, request: UpdateUserRequestSchema) -> Response:
        return self.patch(
            f"/api/v1/users/{user_id}",
            json=request.model_dump(by_alias=True, exclude_none=True)
        )

    def delete_user_api(self, user_id: str) -> Response:
        return self.delete(f"/api/v1/users/{user_id}")

    # --- Высокоуровневые методы ---

    def get_user_me(self) -> UserSchema:
        response = self.get_user_me_api()
        return UserSchema.model_validate_json(response.text)

    def get_user(self, user_id: str) -> dict:
        response = self.get_user_api(user_id)
        return response.json()

    def update_user(self, user_id: str, request: UpdateUserRequestSchema) -> UserSchema:
        response = self.update_user_api(user_id, request)
        return UserSchema.model_validate_json(response.text)


# Единственное изменение – замена типа параметра
def get_private_users_client(user: AuthenticationUserSchema) -> PrivateUsersClient:
    return PrivateUsersClient(client=get_private_http_client(user))