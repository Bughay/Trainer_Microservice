
classification_examples = [
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
    total_calories: float = Field(description='How many calories are found in 100g serving of this food?')
    total_protein: float = Field(description='How much total protein are found in 100g serving of this food?')
    total_carbs: float = Field(description='How much total carbohydrates are found in 100g serving of this food?')
    total_fats: floa = Field(description='How much total fats are found in 100g serving of this food?')
    total_grams:float = Field(description='the total weight of the item, the total number of Grams)"""

food_example_schema = {
  "foods": [
    {
      "food_name": "chicken breast",
      "total_calories": 165.0,
      "total_protein": 31.0,
      "total_carbs": 0.0,
      "total_fats": 3.6,
      "total_grams": 270
    },
    {
      "food_name": "rice",
      "total_calories": 130.0,
      "total_protein": 2.7,
      "total_carbs": 28.0,
      "total_fats": 0.3,
      "total_grams": 125
    }
  ]
}

training_extraction_schema = """
class LogTrainingRequest(BaseModel):
    exercise_name: str = Field(
        description="The canonical name of the exercise (e.g. 'Barbell Back Squat', 'Dumbbell Bench Press').",
        examples=["barbell back squat", "lat pulldown", "dumbbell bicep curl", "treadmill run"])
    weight: float = Field(
        description="External load in kilograms.  Body-weight moves should use 0.0.",
        examples=[20.0, 60.0, 0.0])
    reps: int = Field(
        description="Number of successful repetitions performed in this set.",
        examples=[5, 8, 12, 1])
    notes: str = Field(
        description="Free-form coaching notes: tempo, RPE, failure point, pain, PR flag, etc.",
        examples=["RPE 8, last rep grindy", "tempo 3-1-1", "PR +2.5 kg", "left shoulder felt tight"])

"""

training_example_schema = """
{
  "trainings": [
    {
      "exercise_name": "Barbell Back Squat",
      "weight": 100.0,
      "reps": 5,
      "notes": "RPE 8, felt strong"
    },
    {
      "exercise_name": "Dumbbell Bench Press",
      "weight": 30.0,
      "reps": 10,
      "notes": "tempo 2-0-2, last rep slow"
    }
  ]
}
"""
