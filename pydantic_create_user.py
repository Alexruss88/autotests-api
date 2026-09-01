from pydantic import BaseModel, Field, EmailStr, ConfigDict


# # Добавили модель UserSchema
class UserSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


# # Добавили модель CreateUserRequestSchema
class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr # Используем EmailStr вместо str
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


# # Добавили модель CreateUserResponseSchema
class CreateUserResponseSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    user: UserSchema # Вложенный объект для пользователя, созданного через API
