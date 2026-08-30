import sys
import os

# Гарантируем корректное определение путей импорта в корне проекта
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

# Импортируем все необходимые клиенты и билдеры (с учетом ваших заглавных букв)
from clients.PublicUsersClient import get_public_users_client, CreateUserRequestDict
from clients.FilesClient import get_files_client, CreateFileRequestDict
from clients.courses.CoursesClient import get_courses_client, CreateCourseRequestDict
from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
from clients.private_http_builder import AuthenticationUserDict
from tools.fakers import get_random_email


# === Шаг 1: Создание пользователя через открытый клиент ===
public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)
create_user_response = public_users_client.create_user(create_user_request)


# === Шаг 2: Подготовка авторизационных данных для приватного билдера ===
authentication_user = AuthenticationUserDict(
    email=create_user_request['email'],
    password=create_user_request['password']
)

# Инициализируем приватные клиенты с зашитыми токенами
files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)


# === Шаг 3: Загрузка файла обложки курса ===
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png"
)
create_file_response = files_client.create_file(create_file_request)
print('Create file data:', create_file_response)


# === Шаг 4: Создание курса на базе созданного пользователя и файла ===
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)
create_course_response = courses_client.create_course(create_course_request)
print('Create course data:', create_course_response)


# === Шаг 5: Создание задания (Exercise) внутри созданного курса ===
create_exercise_request = CreateExerciseRequestDict(
    title="Exercise 1",
    courseId=create_course_response['course']['id'],
    maxScore=5,
    minScore=1,
    orderIndex=0,
    description="Exercise 1",
    estimatedTime="5 minutes"
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print('Create exercise data:', create_exercise_response)
