from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from .database import get_user_emails, create_user
from .models import UserCreate,UserResponse,datetime

router = APIRouter()

@router.post(
    "/users",
    response_model=UserResponse,
    status_code = status.HTTP_201_CREATED,
    summary="Create a new user",
    description="Create a new user profile with personal information",
)
async def create_user_endpoint(user:UserCreate):
    ### check if user already exists script
    existing_emails = get_user_emails(user.email)
    print(existing_emails)
    if user.email in existing_emails:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,  
            detail="Email already registered"
        )
    ### check if user already exists script
    try:
        create_user(
            first_name = user.first_name,
            last_name = user.last_name,
            date_of_birth=user.date_of_birth,
            email = user.email,
            gender = user.gender
        )

        response = UserResponse(
            first_name=user.first_name,
            last_name = user.last_name,
            date_of_birth=user.date_of_birth,
            email = user.email,
            gender = user.gender,
            created_at = datetime.now(),
            last_updated= datetime.now()

        )
        
        return response
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating user: {str(e)}"
        )
