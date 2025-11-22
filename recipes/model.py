from pydantic import BaseModel
from typing import List, Optional
from decimal import Decimal

class UserFoodItem(BaseModel):
    food_id: int
    food_name: str
    calories_100: Decimal


class ReadRecipeResponse(BaseModel):
    food_items: List[UserFoodItem]

class RecipeFoodItem(BaseModel):
    food_id: int
    total_grams: Decimal

class CreateRecipeRequest(BaseModel):
    recipe_name:str
    recipe_instructions: str
    ingredients: List[RecipeFoodItem]


class CreateRecipeResponse(BaseModel):
    message:str = 'recipe_succesfully_created'
    recipe:CreateRecipeRequest
    