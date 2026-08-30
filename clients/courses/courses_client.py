from typing import TypedDict, Optional
from httpx import Response
from clients.api_client import APIClient
from clients.files.files_client import File
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client
from clients.users.private_users_client import User



class Course(TypedDict):
    """Описание структуры курса."""
    id: str
    title: str
    maxScore: int
    minScore: int
    description: str
    previewFile: File
    estimatedTime: str
    createdByUser: User


class GetCoursesQueryDict(TypedDict):
    """Описание структуры запроса на получение списка курсов."""
    userId: str


class CreateCourseRequestDict(TypedDict):
    """Описание структуры запроса на создание курса."""
    title: str
    maxScore: int
    minScore: int
    description: str
    estimatedTime: str
    previewFileId: str
    createdByUserId: str


class CreateCourseResponseDict(TypedDict):
    """Описание структуры ответа создания курса."""
    course: Course


class UpdateCourseRequestDict(TypedDict):
    """Описание структуры запроса на обновление курса."""
    title: Optional[str]
    maxScore: Optional[int]
    minScore: Optional[int]
    description: Optional[str]
    estimatedTime: Optional[str]


class CoursesClient(APIClient):
    """Клиент для работы с /api/v1/courses"""

    def get_courses_api(self, query: GetCoursesQueryDict) -> Response:
        """Метод получения списка курсов."""
        return self.get("/api/v1/courses", params=query)

    def get_course_api(self, course_id: str) -> Response:
        """Метод получения курса."""
        return self.get(f"/api/v1/courses/{course_id}")

    def create_course_api(self, request: CreateCourseRequestDict) -> Response:
        """Метод создания курса."""
        return self.post("/api/v1/courses", json=request)

    def update_course_api(self, course_id: str, request: UpdateCourseRequestDict) -> Response:
        """Метод обновления курса."""
        return self.patch(f"/api/v1/courses/{course_id}", json=request)

    def delete_course_api(self, course_id: str) -> Response:
        """Метод удаления курса."""
        return self.delete(f"/api/v1/courses/{course_id}")

    def create_course(self, request: CreateCourseRequestDict) -> CreateCourseResponseDict:
        """Метод создает курс и автоматически возвращает распакованный JSON."""
        response = self.create_course_api(request)
        return response.json()


def get_courses_client(user: AuthenticationUserDict) -> CoursesClient:
    """Функция создаёт экземпляр CoursesClient с уже настроенным HTTP-клиентом."""
    return CoursesClient(client=get_private_http_client(user))
