function_schemas = [
    {
        "type": "function",
        "function": {
            "name": "log_message",
            "description": "Log daily food intake or exercise training. This is for logging completed activities, not creating new templates.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_message": {
                        "type": "string",
                        "description": "The user's message describing what they ate or what exercise they completed. Examples: 'I ate chicken and rice for lunch', 'Just finished my chest workout with bench press'"
                    },
                    "user_id": {
                        "type": "integer",
                        "description": "The ID of the user who is logging the activity"
                    }
                },
                "required": ["user_message", "user_id"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_training",
            "description": "Create a new training routine template. This is for creating reusable workout plans, not logging completed workouts.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_message": {
                        "type": "string",
                        "description": "The user's message describing the training routine to create. Examples: 'Create a push day routine with bench press, overhead press, and tricep pushdowns', 'Make a leg day workout with squats and lunges'"
                    },
                    "user_id": {
                        "type": "integer",
                        "description": "The ID of the user who is creating the training routine"
                    }
                },
                "required": ["user_message", "user_id"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_food",
            "description": "Create a new food item template with nutritional information. This is for creating reusable food entries, not logging daily consumption.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_message": {
                        "type": "string",
                        "description": "The user's message describing the food item and its nutritional values per 100g. Examples: 'Add grilled chicken with 165 calories, 31g protein, 0g carbs, 3.6g fat', 'Create a food entry for brown rice with 111 calories, 2.6g protein, 23g carbs'"
                    },
                    "user_id": {
                        "type": "integer",
                        "description": "The ID of the user who is creating the food item"
                    }
                },
                "required": ["user_message", "user_id"],
                "additionalProperties": False
            }
        }
    }
]