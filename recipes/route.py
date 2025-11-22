from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from auth.security import get_current_user 
from .model import ReadRecipeResponse,CreateRecipeRequest,CreateRecipeResponse
from .database import read_food_items,create_recipe,get_recipe
router = APIRouter(prefix="/recipe", tags=["recipe"])



@router.get(
    "/read_foods",
    response_model=ReadRecipeResponse,
    status_code = status.HTTP_201_CREATED,
    summary="Create a new food item",
    description="Create a new food item for the database",
)

async def read_recipe_endpoint(current_user: dict = Depends(get_current_user)):
    user_id = current_user['user_id']
    food_items = await read_food_items(user_id)
    return food_items    

@router.post(
    "/create_recipe",
    response_model= CreateRecipeResponse,
    status_code = status.HTTP_201_CREATED,
    summary="Create a new food item",
    description="Create a new food item for the database",
)

async def create_recipe_endpoint(recipe:CreateRecipeRequest ,current_user: dict = Depends(get_current_user)):
    user_id = current_user['user_id']

    recipe = await create_recipe(recipe,user_id)

    response = CreateRecipeResponse(
        recipe=recipe
    )
    return response


@router.get(
    "/read_recipe",
    summary="Create a new food item",
    description="Create a new food item for the database",
)


async def read_recipe_endpoint(current_user: dict = Depends(get_current_user)):
    user_id = current_user['user_id']

    recipe = await get_recipe(user_id)

    return recipe
    


