# from typing import TypedDict, List, Optional
# from httpx import QueryParams, Response
# from clients.api_client import APIClient
#
#
# # --- 1. Описание типов данных (TypedDict) ---
#
# class ExercisePayload(TypedDict):
#     """Тип данных для создания нового задания."""
#     title: str
#     description: str
#     course_id: int
#
#
# class ExerciseUpdatePayload(TypedDict, total=False):
#     """Тип данных для частичного обновления задания (PATCH)."""
#     title: str
#     description: str
#     course_id: int
#
#
# class ExerciseResponse(TypedDict):
#     """Структура ответа API, содержащая данные упражнения."""
#     id: int
#     title: str
#     description: str
#     course_id: int
#
#
# # --- 2. Основной класс API-клиента ---
#
# class ExercisesClient(APIClient):
#     """Класс для взаимодействия с API упражнений/заданий (/api/v1/exercises).
#
#     Наследуется от базового класса APIClient.
#     """
#
#     def get_exercises_api(self, params: Optional[QueryParams] = None) -> List[ExerciseResponse]:
#         """Получение списка заданий для определенного курса.
#
#         Аргументы:
#             params (QueryParams, optional): GET-параметры запроса для фильтрации списка.
#
#         Возвращаемое значение:
#             List[ExerciseResponse]: Список словарей с данными упражнений.
#         """
#         response: Response = self.get("/api/v1/exercises", params=params)
#         return response.json()
#
#     def get_exercise_api(self, exercise_id: int) -> ExerciseResponse:
#         """Получение информации о конкретном задании по его exercise_id.
#
#         Аргументы:
#             exercise_id (int): Уникальный идентификатор задания.
#
#         Возвращаемое значение:
#             ExerciseResponse: Словарь с подробными данными запрашиваемого упражнения.
#         """
#         response: Response = self.get(f"/api/v1/exercises/{exercise_id}")
#         return response.json()
#
#     def create_exercise_api(self, payload: ExercisePayload) -> ExerciseResponse:
#         """Создание нового задания.
#
#         Аргументы:
#             payload (ExercisePayload): Данные для создания в формате JSON.
#
#         Возвращаемое значение:
#             ExerciseResponse: Данные созданного упражнения с присвоенным ID.
#         """
#         response: Response = self.post("/api/v1/exercises", json=payload)
#         return response.json()
#
#     def update_exercise_api(self, exercise_id: int, payload: ExerciseUpdatePayload) -> ExerciseResponse:
#         """Обновление данных существующего задания.
#
#         Аргументы:
#             exercise_id (int): Уникальный идентификатор задания.
#             payload (ExerciseUpdatePayload): Изменяемые поля задания.
#
#         Возвращаемое значение:
#             ExerciseResponse: Словарь с обновленными данными упражнения.
#         """
#         response: Response = self.patch(f"/api/v1/exercises/{exercise_id}", json=payload)
#         return response.json()
#
#     def delete_exercise_api(self, exercise_id: int) -> dict:
#         """Удаление задания по его идентификатору.
#
#         Аргументы:
#             exercise_id (int): Уникальный идентификатор удаляемого задания.
#
#         Возвращаемое значение:
#             dict: Ответ сервера в формате JSON, подтверждающий успешное удаление.
#         """
#         response: Response = self.delete(f"/api/v1/exercises/{exercise_id}")
#         return response.json()



from typing import TypedDict, List, Optional
from httpx import QueryParams, Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


# --- 1. Описание типов данных (TypedDict) ---

class ExercisePayload(TypedDict):
    """Тип данных для создания нового задания."""
    title: str
    description: str
    course_id: int


class ExerciseUpdatePayload(TypedDict, total=False):
    """Тип данных для частичного обновления задания (PATCH)."""
    title: str
    description: str
    course_id: int


class ExerciseResponse(TypedDict):
    """Структура ответа API, содержащая данные упражнения."""
    id: int
    title: str
    description: str
    course_id: int


# ТЗ Пункт 2.2: Создать структуру Exercise для JSON-объекта нового вида
class Exercise(TypedDict):
    """Описание структуры задания нового вида."""
    id: str
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


# ТЗ Пункт 2.3: Описание типа GetExercisesResponseDict для аннотации
class GetExercisesResponseDict(TypedDict):
    """Структура ответа списка упражнений."""
    exercises: List[Exercise]


class GetExercisesQueryDict(TypedDict):
    """Структура параметров запроса для фильтрации упражнений."""
    courseId: str


class CreateExerciseRequestDict(TypedDict):
    """Структура запроса на создание нового упражнения."""
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: int
    description: str
    estimatedTime: str


class CreateExerciseResponseDict(TypedDict):
    """Структура ответа при создании упражнения."""
    exercise: Exercise


# --- 2. Основной класс API-клиента ---

class ExercisesClient(APIClient):
    """Класс для взаимодействия с API упражнений/заданий (/api/v1/exercises)."""

    def get_exercises_api(self, params: Optional[QueryParams] = None) -> List[ExerciseResponse]:
        """Получение списка заданий для определенного курса."""
        response: Response = self.get("/api/v1/exercises", params=params)
        return response.json()

    def get_exercise_api(self, exercise_id: int) -> ExerciseResponse:
        """Получение информации о конкретном задании по его exercise_id."""
        response: Response = self.get(f"/api/v1/exercises/{exercise_id}")
        return response.json()

    def create_exercise_api(self, payload: ExercisePayload) -> ExerciseResponse:
        """Создание нового задания."""
        response: Response = self.post("/api/v1/exercises", json=payload)
        return response.json()

    def update_exercise_api(self, exercise_id: int, payload: ExerciseUpdatePayload) -> ExerciseResponse:
        """Обновление данных существующего задания."""
        response: Response = self.patch(f"/api/v1/exercises/{exercise_id}", json=payload)
        return response.json()

    def delete_exercise_api(self, exercise_id: int) -> dict:
        """Удаление задания по его идентификатору."""
        response: Response = self.delete(f"/api/v1/exercises/{exercise_id}")
        return response.json()

    # --- ТЗ Пункт 2.4: Реализация новых методов без приставки _api ---

    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """Метод выполняет запрос к API, извлекает JSON-ответ списка заданий и возвращает его."""
        response = self.get("/api/v1/exercises", params=query)
        return response.json()

    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """Метод выполняет запрос к API, создает задание и возвращает распакованный JSON."""
        response = self.post("/api/v1/exercises", json=request)
        return response.json()


# --- ТЗ Пункт 3.5.4: Добавляем фабричную функцию (Билдер) для клиента ---

def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    """Функция создаёт экземпляр ExercisesClient с настроенным приватным HTTP-клиентом."""
    return ExercisesClient(client=get_private_http_client(user))
