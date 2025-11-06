from fastapi import APIRouter, HTTPException, status
from typing import List


router = APIRouter()


@router.post(
    "/food/log_food/{user_id}",
    response_model=ResponseLogFood,
    status_code = status.HTTP_201_CREATED,
    summary="Log food",
    description="Logs the food and Create a new food item for the database",
)
async def log_food_endpoint(item:LogFood,user_id:int):
    answer = log_food(item,user_id)
    print(answer)
    response = ResponseLogFood(
        food_logged=item,
        food_saved_db=answer
    )
    return response


from fastapi import APIRouter, HTTPException, status
from typing import List
from .model import AddFood, FoodItem,LogFood,ResponseLogFood
from .database import add_food, get_all_food,log_food,get_food_by_user

router = APIRouter()


@router.post(
    "/bot/{user_id}",
    status_code = status.HTTP_201_CREATED,
    summary="Log food",
    description="Logs the food and Create a new food item for the database",
)
async def log_food_endpoint(message,user_id:int):
    pass

