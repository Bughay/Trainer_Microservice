
log_classification_examples = [
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
  ,
    "trainings": [
    {
      "exercise_name": "Barbell Back Squat",
      "weight": 100.0,
      "reps": 5,
      "notes": "RPE 8, felt strong"
    },
    {
      "exercise_name": "Barbell Back Squat",
      "weight": 90.0,
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

training_routine_schema ="""
class TrainingRoutineRequest(BaseModel):
    training_routine_name:str
    exercise_list: List[TrainingRoutineRequestList]
    notes:str

class TrainingRoutineResponse(BaseModel):
    training_routine_name:str
    notes:str
"""
training_routine_extraction_examples = [
    {
        "user_message": "Just crushed push day at the gym. Started with bench press at 185 lbs for 5 sets of 5 reps. Then did overhead press with 95 lbs, 3 sets of 8 reps. Finished with some tricep pushdowns at 50 lbs, 4 sets of 12 reps. Feeling strong today!",
        "json_output": {
            "training_routine_name": "Push Day",
            "exercise_list": [
                {
                    "exercise_name": "bench press",
                    "weight_": 185,
                    "sets_": 5,
                    "reps": 5,
                    "notes": "main lift"
                },
                {
                    "exercise_name": "overhead press",
                    "weight_": 95,
                    "sets_": 3,
                    "reps": 8,
                    "notes": "shoulder work"
                },
                {
                    "exercise_name": "tricep pushdowns",
                    "weight_": 50,
                    "sets_": 4,
                    "reps": 12,
                    "notes": "accessory"
                }
            ],
            "notes": "Feeling strong today!"
        }
    },
    {
        "user_message": "Leg day was brutal. Did back squats at 225 lbs for 4 sets of 6 reps. Then leg press at 315 lbs, 3 sets of 10. Finished with walking lunges holding 40 lb dumbbells, 3 sets of 12 each leg. My legs are shaking!",
        "json_output": {
            "training_routine_name": "Leg Day",
            "exercise_list": [
                {
                    "exercise_name": "back squats",
                    "weight_": 225,
                    "sets_": 4,
                    "reps": 6,
                    "notes": "primary leg movement"
                },
                {
                    "exercise_name": "leg press",
                    "weight_": 315,
                    "sets_": 3,
                    "reps": 10,
                    "notes": "quad focus"
                },
                {
                    "exercise_name": "walking lunges",
                    "weight_": 40,
                    "sets_": 3,
                    "reps": 12,
                    "notes": "each leg"
                }
            ],
            "notes": "My legs are shaking!"
        }
    },
    {
        "user_message": "Great pull session today. Deadlifted 275 lbs for 3 sets of 5. Did wide-grip pull-ups (bodyweight) for 3 sets of 8. Barbell rows at 135 lbs for 4 sets of 10. Also threw in some bicep curls at 25 lbs, 3 sets of 15. Focused on form.",
        "json_output": {
            "training_routine_name": "Pull Session",
            "exercise_list": [
                {
                    "exercise_name": "deadlifts",
                    "weight_": 275,
                    "sets_": 3,
                    "reps": 5,
                    "notes": "heavy compound"
                },
                {
                    "exercise_name": "wide-grip pull-ups",
                    "weight_": 0,
                    "sets_": 3,
                    "reps": 8,
                    "notes": "bodyweight"
                },
                {
                    "exercise_name": "barbell rows",
                    "weight_": 135,
                    "sets_": 4,
                    "reps": 10,
                    "notes": "back thickness"
                },
                {
                    "exercise_name": "bicep curls",
                    "weight_": 25,
                    "sets_": 3,
                    "reps": 15,
                    "notes": "arm finisher"
                }
            ],
            "notes": "Focused on form"
        }
    },
    {
        "user_message": "Upper body pump day. Incline dumbbell press with 60 lb dumbbells, 4 sets of 12. Lat pulldowns at 120 lbs, 3 sets of 15. Cable flies at 30 lbs, 3 sets of 20. Face pulls at 40 lbs, 4 sets of 15. Great mind-muscle connection.",
        "json_output": {
            "training_routine_name": "Upper Body Pump Day",
            "exercise_list": [
                {
                    "exercise_name": "incline dumbbell press",
                    "weight_": 60,
                    "sets_": 4,
                    "reps": 12,
                    "notes": "hypertrophy focus"
                },
                {
                    "exercise_name": "lat pulldowns",
                    "weight_": 120,
                    "sets_": 3,
                    "reps": 15,
                    "notes": "back width"
                },
                {
                    "exercise_name": "cable flies",
                    "weight_": 30,
                    "sets_": 3,
                    "reps": 20,
                    "notes": "chest isolation"
                },
                {
                    "exercise_name": "face pulls",
                    "weight_": 40,
                    "sets_": 4,
                    "reps": 15,
                    "notes": "rear delts"
                }
            ],
            "notes": "Great mind-muscle connection"
        }
    },
    {
        "user_message": "Full body power workout. Squats at 245 lbs, 5 sets of 3. Bench press at 200 lbs, 5 sets of 3. Barbell rows at 155 lbs, 4 sets of 5. Accessory: planks for 60 seconds, 3 sets. Working on pure strength gains.",
        "json_output": {
            "training_routine_name": "Full Body Power Workout",
            "exercise_list": [
                {
                    "exercise_name": "squats",
                    "weight_": 245,
                    "sets_": 5,
                    "reps": 3,
                    "notes": "strength focus"
                },
                {
                    "exercise_name": "bench press",
                    "weight_": 200,
                    "sets_": 5,
                    "reps": 3,
                    "notes": "heavy pressing"
                },
                {
                    "exercise_name": "barbell rows",
                    "weight_": 155,
                    "sets_": 4,
                    "reps": 5,
                    "notes": "pulling strength"
                },
                {
                    "exercise_name": "planks",
                    "weight_": 0,
                    "sets_": 3,
                    "reps": 60,
                    "notes": "core stability, hold in seconds"
                }
            ],
            "notes": "Working on pure strength gains"
        }
    }
]
