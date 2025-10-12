from pydantic import BaseModel

class FoodItem(BaseModel):
    food_name: str
    calories_100: float

class AddFood(BaseModel):
    user_id:int
    food_name: str
    is_solid: bool
    calories_100: float
    protein_100: float
    carbs_100: float
    fats_100: float






