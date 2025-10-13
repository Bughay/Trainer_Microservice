from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from .model import AddFood, FoodItem,LogFood,ResponseLogFood
from .database import add_food, get_all_food,log_food

router = APIRouter()

@router.post(
    "/food",
    response_model=AddFood,
    status_code = status.HTTP_201_CREATED,
    summary="Create a new food item",
    description="Create a new food item for the database",
)

async def create_food_endpoint(food: AddFood):
    try:
        all_food = get_all_food() 
        
        existing_food_names = [item[0] for item in all_food] 
        
        if food.food_name in existing_food_names:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Food '{food.food_name}' already exists in database"
            )
        else:
            add_food(food)
            return food

    except HTTPException:
        raise  
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating food item: {str(e)}"
        )

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
        all_food = get_all_food()
        print(all_food)
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


@router.post(
    "/food/entry",
    response_model=ResponseLogFood,
    status_code = status.HTTP_201_CREATED,
    summary="Log food",
    description="Logs the food and Create a new food item for the database",
)

async def log_food_endpoint(item:LogFood):
    answer = log_food(item)
    print(answer)
    response = ResponseLogFood(
        food_logged=item,
        food_saved_db=answer
    )
    print(response)
    return response