# from clients.courses.courses_client import get_courses_client, CreateCourseRequestDict
# from clients.exercises.exercises_client import get_exercises_client, CreateExerciseRequestDict
# from clients.files.files_client import get_files_client, CreateFileRequestDict
# from clients.private_http_builder import AuthenticationUserDict
# from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
# from tools.fakers import get_random_email
#
# public_users_client = get_public_users_client()
#
# create_user_request = CreateUserRequestDict(
#     email=get_random_email(),
#     password="string",
#     lastName="string",
#     firstName="string",
#     middleName="string"
# )
# create_user_response = public_users_client.create_user(create_user_request)
#
# authentication_user = AuthenticationUserDict(
#     email=create_user_request['email'],
#     password=create_user_request['password']
# )
#
# files_client = get_files_client(authentication_user)
# courses_client = get_courses_client(authentication_user)
# exercises_client = get_exercises_client(authentication_user)
#
# create_file_request = CreateFileRequestDict(
#     filename="image.png",
#     directory="courses",
#     upload_file="clients/files/image.png"
# )
# create_file_response = files_client.create_file(create_file_request)
# print('Create file data:', create_file_response)
#
# create_course_request = CreateCourseRequestDict(
#     title="Python",
#     maxScore=100,
#     minScore=10,
#     description="Python API course",
#     estimatedTime="2 weeks",
#     previewFileId=create_file_response['file']['id'],
#     createdByUserId=create_user_response['user']['id']
# )
# create_course_response = courses_client.create_course(create_course_request)
# print('Create course data:', create_course_response)
#
# create_exercise_request = CreateExerciseRequestDict(
#     title="Exercise 1",
#     courseId=create_course_response['course']['id'],
#     maxScore=5,
#     minScore=1,
#     orderIndex=0,
#     description="Exercise 1",
#     estimatedTime="5 minutes"
# )
# create_exercise_response = exercises_client.create_exercise(create_exercise_request)
# print('Create exercise data:', create_exercise_response)


from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import CreateFileRequestSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from tools.fakers import get_random_email

# Создаем клиента для публичных пользователей (без авторизации)
public_users_client = get_public_users_client()

# Создаем пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string",
)
create_user_response = public_users_client.create_user(create_user_request)

# Получаем данные пользователя через атрибуты (автодополнение в IDE, защита от опечаток)
user_id = create_user_response.user.id
email = create_user_response.user.email
print(f"User created: id={user_id}, email={email}")

# Инициализируем объект для авторизации
authentication_user = AuthenticationUserSchema(
    email=email,
    password="string",
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

# Загружаем файл
# Путь к файлу лучше делать абсолютным или относительно корня проекта, чтобы не ломался при запуске из разных директорий
create_file_request = CreateFileRequestSchema(
    filename="image.png",
    directory="courses",
    upload_file="./testdata/files/image.png",  # Исправлено: относительный путь от корня проекта
)
create_file_response = files_client.create_file(create_file_request)

file_id = create_file_response.file.id
print(f"File created: id={file_id}")

# Создаем курс
create_course_request = CreateCourseRequestSchema(
    title="Python",
    max_score=100,
    min_score=10,
    description="Python API course",
    estimated_time="2 weeks",
    preview_file_id=file_id,
    created_by_user_id=user_id,
)
create_course_response = courses_client.create_course(create_course_request)

course_id = create_course_response.course.id
print(f"Course created: id={course_id}")

# Создаем упражнение
create_exercise_request = CreateExerciseRequestSchema(
    title="Exercise 1",
    course_id=course_id,
    max_score=5,
    min_score=1,
    order_index=0,
    description="Exercise 1",
    estimated_time="5 minutes",
)
create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print("Create exercise data:", create_exercise_response)
