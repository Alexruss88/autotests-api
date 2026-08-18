import sys
import os
from unittest.mock import MagicMock
from httpx import Response

# Добавляем корень проекта в пути импорта
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Импортируем созданный клиент и типы
from clients.exercises.exercises_client import ExercisesClient, ExercisePayload, ExerciseUpdatePayload


def test_exercises_client_workability():
    print("\n=== Запуск автономного тестирования ExercisesClient (без сторонних библиотек) ===")

    # 1. Создаем мок для httpx.Client
    mock_httpx_client = MagicMock()

    # Инициализируем наш клиент, передавая ему заглушку
    exercise_client = ExercisesClient(client=mock_httpx_client)

    # --- Тест 1: get_exercises_api ---
    print("Проверка метода: get_exercises_api...")
    mock_response_get_all = Response(200, json=[{"id": 1, "title": "Math", "description": "Easy", "course_id": 10}])
    mock_httpx_client.get.return_value = mock_response_get_all

    res_get_all = exercise_client.get_exercises_api(params={"course_id": 10})

    mock_httpx_client.get.assert_called_with("/api/v1/exercises", params={"course_id": 10})
    assert res_get_all[0]["id"] == 1
    print("-> Успешно: Метод GET сформирован корректно.")

    # --- Тест 2: get_exercise_api ---
    print("\nПроверка метода: get_exercise_api...")
    mock_response_get_one = Response(200,
                                     json={"id": 42, "title": "Python Basics", "description": "Intro", "course_id": 5})
    mock_httpx_client.get.return_value = mock_response_get_one

    res_get_one = exercise_client.get_exercise_api(exercise_id=42)

    # Исправлено: базовый клиент по умолчанию передает params=None
    mock_httpx_client.get.assert_called_with("/api/v1/exercises/42", params=None)
    assert res_get_one["id"] == 42
    print("-> Успешно: URL с exercise_id подставляется верно.")

    # --- Тест 3: create_exercise_api ---
    print("\nПроверка метода: create_exercise_api...")
    mock_response_post = Response(201,
                                  json={"id": 100, "title": "New Task", "description": "Create Client", "course_id": 1})
    mock_httpx_client.post.return_value = mock_response_post

    new_payload: ExercisePayload = {"title": "New Task", "description": "Create Client", "course_id": 1}
    res_post = exercise_client.create_exercise_api(payload=new_payload)

    # Исправлено: базовый клиент post() по умолчанию передает data=None и files=None
    mock_httpx_client.post.assert_called_with("/api/v1/exercises", json=new_payload, data=None, files=None)
    assert res_post["id"] == 100
    print("-> Успешно: Передача тела (json) в POST-запросе работает.")

    # --- Тест 4: update_exercise_api ---
    print("\nПроверка метода: update_exercise_api...")
    mock_response_patch = Response(200, json={"id": 100, "title": "Updated Task", "description": "Create Client",
                                              "course_id": 1})
    mock_httpx_client.patch.return_value = mock_response_patch

    update_payload: ExerciseUpdatePayload = {"title": "Updated Task"}
    res_patch = exercise_client.update_exercise_api(exercise_id=100, payload=update_payload)

    mock_httpx_client.patch.assert_called_with("/api/v1/exercises/100", json=update_payload)
    assert res_patch["title"] == "Updated Task"
    print("-> Успешно: Частичное обновление через PATCH работает.")

    # --- Тест 5: delete_exercise_api ---
    print("\nПроверка метода: delete_exercise_api...")
    mock_response_delete = Response(200, json={"status": "deleted"})
    mock_httpx_client.delete.return_value = mock_response_delete

    res_delete = exercise_client.delete_exercise_api(exercise_id=100)

    mock_httpx_client.delete.assert_called_with("/api/v1/exercises/100")
    assert res_delete["status"] == "deleted"
    print("-> Успешно: Удаление по ID через DELETE работает.")

    print("\n[РЕЗУЛЬТАТ] Все методы ExercisesClient работают абсолютно корректно и без ошибок!")


if __name__ == "__main__":
    test_exercises_client_workability()
