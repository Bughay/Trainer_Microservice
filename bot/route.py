from fastapi import APIRouter, HTTPException, status,Depends
from auth.security import get_current_user 
from .model import ResponseLogBot,RequestLogBot
from .workflow import log_message,create_training,personal_trainer_agent
from pydantic import BaseModel

router = APIRouter(prefix="/agent", tags=["bot"])


@router.post(
    "/",
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
    answer = await log_message(message,user_id)
    return answer

@router.post(
    "/agent_test",
    status_code = status.HTTP_201_CREATED,
    summary="bot",
    description="AI personal trainer agent that takes an input and then finds the correct python function",
)
async def agent_2(
    message_request:RequestLogBot,
    current_user:dict=Depends(get_current_user)
    ):
    user_id = current_user['user_id']
    message = message_request.message
    answer = await create_training(message,user_id)
    return answer


@router.post(
    "/personal_trainer",
    status_code = status.HTTP_201_CREATED,
    summary="bot",
    description="AI personal trainer agent that takes an input and then finds the correct python function",
)
async def personal_trainer(
    message_request:RequestLogBot,
    current_user:dict=Depends(get_current_user)
    ):
    user_id = current_user['user_id']
    message = message_request.message
    answer = await personal_trainer_agent(message,user_id)
    print(answer)
    return answer



