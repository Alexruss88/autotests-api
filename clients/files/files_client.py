from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class File(TypedDict):
    """Описание структуры файла."""
    id: str
    url: str
    filename: str
    directory: str


class CreateFileRequestDict(TypedDict):
    """Описание структуры запроса на создание файла."""
    filename: str
    directory: str
    upload_file: str


class CreateFileResponseDict(TypedDict):
    """Описание структуры ответа создания файла."""
    file: File


class FilesClient(APIClient):
    """Клиент для работы с /api/v1/files."""

    def get_file_api(self, file_id: str) -> Response:
        """Метод получения файла."""
        return self.get(f"/api/v1/files/{file_id}")

    def create_file_api(self, request: CreateFileRequestDict) -> Response:
        """Метод создания файла."""
        return self.post(
            "/api/v1/files",
            data=request,
            files={"upload_file": open(request['upload_file'], 'rb')}
        )

    def delete_file_api(self, file_id: str) -> Response:
        """Метод удаления файла."""
        return self.delete(f"/api/v1/files/{file_id}")

    def create_file(self, request: CreateFileRequestDict) -> CreateFileResponseDict:
        """Метод создает файл и автоматически возвращает распакованный JSON."""
        response = self.create_file_api(request)
        return response.json()


def get_files_client(user: AuthenticationUserDict) -> FilesClient:
    """Функция создаёт экземпляр FilesClient с уже настроенным HTTP-клиентом."""
    return FilesClient(client=get_private_http_client(user))
