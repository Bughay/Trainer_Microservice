from pydantic import BaseModel, PastDate ,Field,field_validator
from datetime import datetime
class UserCreate(BaseModel):
    first_name: str = Field(min_length=2, max_length=10)
    last_name: str = Field(min_length=2, max_length=10)
    date_of_birth: PastDate
    email: str
    gender: bool
    
    @field_validator('email')
    def email_to_lowercase(cls,v:str) -> str:
        return v.lower()



    

class UserResponse(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: PastDate
    email: str
    gender: bool




