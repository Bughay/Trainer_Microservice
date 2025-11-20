from fastapi import APIRouter, HTTPException, status,Depends
from auth.security import get_current_user 
from .model import ResponseLogBot,RequestLogBot
from .workflow import log_message
from pydantic import BaseModel

router = APIRouter(prefix="/agent", tags=["bot"])


@router.post(
    "/agent",
    status_code = status.HTTP_201_CREATED,
    response_model=ResponseLogBot,
    summary="bot",
    description="AI personal trainer agent that takes an input and then finds the correct python function",
)
async def agent(
    message_request:RequestLogBot,
    current_user:dict=Depends(get_current_user)
    ):
    user_id = current_user['user_id']
    message = message_request.message
    answer = log_message(message,user_id)
    return answer



    