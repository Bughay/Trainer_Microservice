
food_classification_examples = [
    {
        "user_message": "I just found an amazing recipe for a creamy mushroom risotto. What kind of wine pairs best with it?",
        "categories": ["food", "exercise"],
        "agent_classification": "food"
    },
    {
        "user_message": "The secret to a perfect fluffy omelette is to whisk the eggs vigorously and use a non-stick pan with plenty of butter.",
        "categories": ["food", "exercise"], 
        "agent_classification": "food"
    },
    {
        "user_message": "My quads are so sore from yesterday's leg day. I did heavy squats and lunges, and now I can barely walk downstairs.",
        "categories": ["food", "exercise"],
        "agent_classification": "exercise"
    },
    {
        "user_message": "For my marathon training, should I focus more on increasing my long run distance or my interval speed work?",
        "categories": ["food", "exercise"],
        "agent_classification": "exercise"
    }
]



food_extraction_schema = """
    food_name: str = Field(
        description='the name of the food, how is the food called?',
        examples=['apples',"red meat","banana", "chicken breast","letuce"])
    is_solid: bool = Field(
        description="is the food solid or not ? if it is then true"
    )
    calories_100: float = Field(description='How many calories are found in 100g serving of this food?')
    protein_100: float = Field(description='How much total protein are found in 100g serving of this food?')
    carbs_100: float = Field(description='How much total carbohydrates are found in 100g serving of this food?')
    fats_100: float = Field(description='How much total fats are found in 100g serving of this food?')"""

food_example_schema = {
  "foods": [
    {
      "food_name": "chicken breast",
      "calories": 165.0,
      "protein": 31.0,
      "carbs": 0.0,
      "fats": 3.6,
      "serving_g": 270
    },
    {
      "food_name": "rice",
      "calories": 130.0,
      "protein": 2.7,
      "carbs": 28.0,
      "fats": 0.3,
      "serving_g": 125
    }
  ]
}
