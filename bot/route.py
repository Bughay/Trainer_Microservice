from fastapi import APIRouter, HTTPException, status,Depends
from auth.security import get_current_user 
from .model import ResponseLogFoodBot
from .workflow import log_message
from pydantic import BaseModel
router = APIRouter(prefix="/agent", tags=["bot"])


@router.post(
    "/agent",
    status_code = status.HTTP_201_CREATED,
    summary="bot",
    description="AI personal trainer agent that takes an input and then finds the correct python function",
)
async def agent(
    message_request:str,
    current_user:dict=Depends(get_current_user)
    ):
    user_id = current_user['user_id']
    answer = log_message(message_request,user_id)

    return answer

    