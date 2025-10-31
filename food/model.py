from pydantic import BaseModel

class FoodItem(BaseModel):
    food_name: str
    calories_100: float

class AddFood(BaseModel):
    food_name: str
    is_solid: bool
    calories_100: float
    protein_100: float
    carbs_100: float
    fats_100: float


class LogFood(BaseModel):
    food_name:str
    total_calories:float
    total_grams:float
    total_protein: float
    total_carbs: float
    total_fats: float

class ResponseAddFood(BaseModel):
    user_id: int
    food_name: str
    is_solid: bool
    calories_100: float
    protein_100: float
    carbs_100: float
    fats_100: float
    
class ResponseLogFood(BaseModel):
    food_logged:LogFood
    food_saved_db:ResponseAddFood










