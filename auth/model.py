from pydantic import BaseModel, EmailStr, field_validator
from datetime import date

class CreateUserRequest(BaseModel):
    user_name: str
    password: str
    repeat_password: str
    email: EmailStr
    date_of_birth: date

class UserResponse(BaseModel):
    user_id: int
    user_name: str
    email: EmailStr

class CreateUserResponse(BaseModel):
    success: bool = True
    message: str = "User registered successfully"
    user: UserResponse


class LoginRequest(BaseModel):
    user_name: str
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    message:str = "User has succesfully signed in"