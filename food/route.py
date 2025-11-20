from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from .model import AddFood, FoodItem,LogFood,ResponseLogFood
from .database import add_food, get_all_food,log_food,get_food_by_user
from auth.security import get_current_user 
router = APIRouter(prefix="/food", tags=["food"])


@router.post(
    "/food/log_food/log",
    response_model=ResponseLogFood,
    status_code = status.HTTP_201_CREATED,
    summary="Log food",
    description="Logs the food and Create a new food item for the database",
)
async def log_food_endpoint(item:LogFood,current_user: dict = Depends(get_current_user) ):
    try:
        user_id = current_user['user_id']
        answer = await log_food(item,user_id)
        print(answer)
        response = ResponseLogFood(
            food_logged=item,
            food_saved_db=answer
        )
        return response

    except HTTPException:
        raise  
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating food item: {str(e)}"
        )




@router.post(
    "/food/create_food/log",
    response_model=AddFood,
    status_code = status.HTTP_201_CREATED,
    summary="Create a new food item",
    description="Create a new food item for the database",
)

async def create_food_endpoint(food: AddFood,current_user: dict = Depends(get_current_user)):
    try:
        user_id = current_user['user_id']
        all_food = await get_food_by_user(user_id) 
        
        existing_food_names = [item[0] for item in all_food] 
        
        if food.food_name in existing_food_names:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Food '{food.food_name}' already exists in database"
            )
        else:
            await add_food(food,user_id)
            return food

    except HTTPException:
        raise  
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating food item: {str(e)}"
        )



    
@router.get(
    "/food",
    response_model=List[FoodItem],
    status_code = status.HTTP_201_CREATED,
    summary="get all food items",
    description="view your saved foods",
)

async def get_all_food_endpoint():
    try:
        all_food = await get_all_food()
        food_list = []
        for food_name, calories in all_food:
            food_list.append(FoodItem(
                food_name=food_name,
                calories_100=float(calories)
            ))
        
        return food_list
        

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating food item: {str(e)}"
        )
    


@router.get(
    "/food/all_items",
    response_model=List[FoodItem],
    status_code = status.HTTP_201_CREATED,
    summary="get all food items of the user",
    description="view your saved foods of the user",
)

async def get_users_food_endpoint(
    current_user: dict = Depends(get_current_user)
):
    try:
        user_id = current_user['user_id']
        all_food = await get_food_by_user(user_id)
        food_list = []
        for food_name, calories in all_food:
            food_list.append(FoodItem(
                food_name=food_name,
                calories_100=float(calories)
            ))
        
        return food_list
        

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating food item: {str(e)}"
        )

    



