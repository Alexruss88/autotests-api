# from clients.private_http_builder import AuthenticationUserDict
# from clients.users.PrivateUsersClient import get_private_users_client
# from clients.PublicUsersClient import get_public_users_client, CreateUserRequestDict
# from tools.fakers import get_random_email
#
#
# # Инициализируем клиент PublicUsersClient
# public_users_client = get_public_users_client()
#
# # Инициализируем запрос на создание пользователя
# create_user_request = CreateUserRequestDict(
#     email=get_random_email(),
#     password="string",
#     lastName="string",
#     firstName="string",
#     middleName="string"
# )
# # Отправляем POST запрос на создание пользователя
# create_user_response = public_users_client.create_user_api(create_user_request)
# create_user_response_data = create_user_response.json()
# print('Create user data:', create_user_response_data)
#
# # Инициализируем пользовательские данные для аутентификации
# authentication_user = AuthenticationUserDict(
#     email=create_user_request['email'],
#     password=create_user_request['password']
# )
# # Инициализируем клиент PrivateUsersClient
# private_users_client = get_private_users_client(authentication_user)
#
# # Отправляем GET запрос на получение данных пользователя
# get_user_response = private_users_client.get_user_api(create_user_response_data['user']['id'])
# get_user_response_data = get_user_response.json()
# print('Get user data:', get_user_response_data)



from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

# Создаём клиента для публичных пользователей (без авторизации)
public_users_client = get_public_users_client()

# Формируем запрос на создание пользователя
create_user_request = CreateUserRequestSchema(
    email=get_random_email(),
    password="string",
    last_name="string",
    first_name="string",
    middle_name="string",
)

# Отправляем запрос и получаем ответ
create_user_response = public_users_client.create_user(create_user_request)
print('Create user data:', create_user_response)

# Инициализируем объект для авторизации (данные созданного пользователя)
authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

# Получаем приватный клиент для работы с пользователями (с авторизацией)
private_users_client = get_private_users_client(authentication_user)

# Запрашиваем данные пользователя по его ID
get_user_response = private_users_client.get_user(create_user_response.user.id)
print('Get user data:', get_user_response)