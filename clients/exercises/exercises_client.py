
# from typing import TypedDict
# from httpx import Response
# from clients.api_client import APIClient
# from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
#
#
# class GetExercisesQueryDict(TypedDict):
#     """Описание структуры параметров запроса списка упражнений."""
#     courseId: str
#
#
# class CreateExerciseRequestDict(TypedDict):
#     """Описание структуры запроса на создание упражнения."""
#     title: str
#     courseId: str
#     maxScore: int
#     minScore: int
#     orderIndex: int
#     description: str
#     estimatedTime: str
#
#
# class UpdateExerciseRequestDict(TypedDict):
#     """Описание структуры запроса на обновление упражнения."""
#     title: str | None
#     maxScore: int | None
#     minScore: int | None
#     orderIndex: int | None
#     description: str | None
#     estimatedTime: str | None
#
#
# class ExercisesClient(APIClient):
#     """Клиент для работы с /api/v1/exercises"""
#
#     # --- Низкоуровневые методы (_api) ---
#
#     def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
#         """Метод получения списка заданий.
#
#         :param query: Словарь с courseId.
#         :return: Ответ от сервера в виде объекта httpx.Response
#         """
#         return self.get("/api/v1/exercises", params=query)
#
#     def get_exercise_api(self, exercise_id: str) -> Response:
#         """Метод получения задания.
#
#         :param exercise_id: Идентификатор задания.
#         :return: Ответ от сервера в виде объекта httpx.Response
#         """
#         return self.get(f"/api/v1/exercises/{exercise_id}")
#
#     def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
#         """Метод создания задания.
#
#         :param request: Словарь с данными задания.
#         :return: Ответ от сервера в виде объекта httpx.Response
#         """
#         return self.post("/api/v1/exercises", json=request)
#
#     def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestDict) -> Response:
#         """Метод обновления задания.
#
#         :param exercise_id: Идентификатор задания.
#         :param request: Словарь с обновляемыми полями задания.
#         :return: Ответ от сервера в виде объекта httpx.Response
#         """
#         return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)
#
#     def delete_exercise_api(self, exercise_id: str) -> Response:
#         """Метод удаления задания.
#
#         :param exercise_id: Идентификатор задания.
#         :return: Ответ от сервера в виде объекта httpx.Response
#         """
#         return self.delete(f"/api/v1/exercises/{exercise_id}")
#
#     # --- Высокоуровневые методы ---
#
#     def get_exercises(self, query: GetExercisesQueryDict) -> dict:
#         """Метод получает список заданий и автоматически возвращает распакованный JSON.
#
#         :param query: Словарь с courseId.
#         :return: Распакованный JSON-ответ от сервера.
#         """
#         response = self.get_exercises_api(query)
#         return response.json()
#
#     def get_exercise(self, exercise_id: str) -> dict:
#         """Метод получает конкретное задание и автоматически возвращает распакованный JSON.
#
#         :param exercise_id: Идентификатор задания.
#         :return: Распакованный JSON-ответ от сервера.
#         """
#         response = self.get_exercise_api(exercise_id)
#         return response.json()
#
#     def create_exercise(self, request: CreateExerciseRequestDict) -> dict:
#         """Метод создает задание и автоматически возвращает распакованный JSON.
#
#         :param request: Словарь с данными задания.
#         :return: Распакованный JSON-ответ от сервера.
#         """
#         response = self.create_exercise_api(request)
#         return response.json()
#
#     def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestDict) -> dict:
#         """Метод обновляет задание и автоматически возвращает распакованный JSON.
#
#         :param exercise_id: Идентификатор задания.
#         :param request: Словарь с обновляемыми полями.
#         :return: Распакованный JSON-ответ от сервера.
#         """

# from httpx import Response
# from clients.api_client import APIClient
# from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
# from .exercises_schema import (
#     GetExercisesQuerySchema,
#     CreateExerciseRequestSchema,
#     UpdateExerciseRequestSchema,
# )
#
#
# class ExercisesClient(APIClient):
#     def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
#         return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))
#
#     def get_exercise_api(self, exercise_id: str) -> Response:
#         return self.get(f"/api/v1/exercises/{exercise_id}")
#
#     def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
#         return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))
#
#     def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
#         return self.patch(
#             f"/api/v1/exercises/{exercise_id}",
#             json=request.model_dump(by_alias=True, exclude_none=True),
#         )
#
#     def delete_exercise_api(self, exercise_id: str) -> Response:
#         return self.delete(f"/api/v1/exercises/{exercise_id}")
#
#     def get_exercises(self, query: GetExercisesQuerySchema):
#         response = self.get_exercises_api(query)
#         return response.json()
#
#     def get_exercise(self, exercise_id: str):
#         response = self.get_exercise_api(exercise_id)
#         return response.json()
#
#     def create_exercise(self, request: CreateExerciseRequestSchema):
#         response = self.create_exercise_api(request)
#         return response.json()
#
#     def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema):

#         response = self.update_exercise_api(exercise_id, request)
#         return response.json()
#
#

# def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
#     """Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.
#
#     :return: Готовый к использованию ExercisesClient.
#     """
#     return ExercisesClient(client=get_private_http_client(user))



# # Единственное изменение – замена типа параметра
# def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
#     return ExercisesClient(client=get_private_http_client(user))


from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from .exercises_schema import (
    GetExercisesQuerySchema,
    CreateExerciseRequestSchema,
    UpdateExerciseRequestSchema,
    CreateExerciseResponseSchema,
    GetExerciseResponseSchema,
    UpdateExerciseResponseSchema,
    exercises_list_adapter,
)


class ExercisesClient(APIClient):
    # --- Низкоуровневые методы ---
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        return self.get("/api/v1/exercises", params=query.model_dump(by_alias=True))

    def get_exercise_api(self, exercise_id: str) -> Response:
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        return self.post("/api/v1/exercises", json=request.model_dump(by_alias=True))

    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        return self.patch(
            f"/api/v1/exercises/{exercise_id}",
            json=request.model_dump(by_alias=True, exclude_none=True),
        )

    def delete_exercise_api(self, exercise_id: str) -> Response:
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    # --- Высокоуровневые методы с валидацией ---
    def get_exercises(self, query: GetExercisesQuerySchema):
        response = self.get_exercises_api(query)
        return exercises_list_adapter.validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))