from fastapi import APIRouter
import requests
from bot.services import workflow
router = APIRouter()

@router.post("/bot")
async def bot_endpoint(user_id: int, user_message: str):
    # Call your existing log_food endpoint
    reply = workflow(user_message)
    print(reply)
    user_id = 1
    response = requests.post(
        f"http://localhost:8000/food/log_food/{user_id}",
        json={"user_message": user_message}
    )
    
    return {
            "workflow_reply": reply,
            "food_log_response": response.json()
        }