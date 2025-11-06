from pydantic import BaseModel, Field


class AddFoodSchema(BaseModel):
    food_name: str = Field(
        description='the name of the food, how is the food called?',
        examples=['apples',"red meat","banana", "chicken breast","letuce"])
    is_solid: bool = Field(
        description="is the food solid or not ? if it is then true"
    )
    calories_100: float = Field(description='How many calories are found in 100g serving of this food?')
    protein_100: float = Field(description='How much total protein are found in 100g serving of this food?')
    carbs_100: float = Field(description='How much total carbohydrates are found in 100g serving of this food?')
    fats_100: float = Field(description='How much total fats are found in 100g serving of this food?')