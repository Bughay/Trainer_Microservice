from fastapi import APIRouter, HTTPException, status,Depends
from auth.security import get_current_user 
from .model import ResponseLogBot,RequestLogBot
from .other_agents.react_agent import ReActAgent
from .tools import *

router = APIRouter(prefix="/react_agent", tags=["bot"])




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
    function_map = create_wrapped_function_map(user_id)

    agent = ReActAgent(api_key=api_key,
                   tools=function_schemas,
                   function_map=function_map)
    result = await agent.run(message)
    return result