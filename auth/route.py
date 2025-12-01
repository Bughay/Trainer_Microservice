from fastapi import APIRouter, HTTPException, status
import os
from dotenv import load_dotenv
import psycopg2
from .model import CreateUserRequest,CreateUserResponse,UserResponse,LoginRequest,LoginResponse
from .security import create_jwt_token,verify_password,get_password_hash
load_dotenv()

database_url = os.getenv('DATABASE_URL')
router = APIRouter(prefix="/auth", tags=["authentication"])

@router.post(
    "/register",
    response_model=CreateUserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register new user",
    description="Create a new user account"
)
async def registration_endpoint(user:CreateUserRequest):
    conn = None         
    cur  = None 
    try:
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        
        cur.execute(
            "SELECT EXISTS(SELECT 1 FROM users WHERE user_name = %s OR email = %s)",
            (user.user_name, user.email)
        )
        if cur.fetchone()[0]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username or email already exists"
            )
        
        hashed_password = get_password_hash(user.password)

        cur.execute(
            "INSERT INTO users(user_name,email,hashed_password) VALUES(%s,%s,%s) RETURNING user_id,user_name,email",
            (user.user_name, user.email,hashed_password)
        )


        user_id, username, email = cur.fetchone()

        cur.execute(
            "INSERT INTO users_profile(user_id) VALUES(%s)",
            (user_id,)
        )
        conn.commit()

        registration_response = CreateUserResponse(
            user=UserResponse(
                user_id=user_id,
                user_name=username,
                email=email
                ))

        return registration_response
    except psycopg2.IntegrityError:
        if conn:
            conn.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists"
        )
    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Registration failed: {str(e)}"
        )
    finally:
        if conn:
            cur.close()
            conn.close()

@router.post(
    "/login",
    response_model=LoginResponse,
    summary="Login user",
    description="Authenticate user and return JWT token"
)
async def login(user:LoginRequest):
    conn = None         
    cur  = None 
    try:
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        
        cur.execute(
            "SELECT user_id,user_name,hashed_password FROM users WHERE user_name = %s",(user.user_name,)
        )
        user_result = cur.fetchone()
        
        if not user_result:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password, please contact admin"
            )
        user_id, user_name,hashed_password= user_result

        if not verify_password(user.password, hashed_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid username or password, please contact admin"
            )
        
        access_token = create_jwt_token(
            data={
                "sub": user_name,
                "user_id": user_id
            }
        )
            
        user_response = LoginResponse(
            access_token=access_token
        )
        return user_response
        

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Login failed: {str(e)}"
        )
    finally:
        if conn:
            cur.close()
            conn.close()

