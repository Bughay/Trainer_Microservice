from .other_agents.deep_seek_extraction import DeepseekExtractor
from .other_agents.classification import DeepseekClassification
from .other_agents.chat_template import DeepseekChat
import os
from .prompts import *
from .model import ResponseLogBot
import sys
from pathlib import Path
from functools import partial

project_root = Path(__file__).resolve().parents[2]          
sys.path.insert(0, str(project_root))                       
from training.database import log_training
from training.model import LogTrainingRequest,TrainingRoutineRequest
from food.database import log_food,add_food
from food.model import LogFood,AddFood
from training.database import create_training_routine
from pydantic import BaseModel
api_key = os.getenv("DEEPSEEK_API_KEY")



function_schemas = {
    "log_message": {
        "description": "Log daily food intake or exercise training...",
        "parameters": {
            "user_message": {
                "type": "string",
                "description": "The user's message describing what they ate...",
                "required": True  # ← Add this if needed
            }
        }
    },
    "create_training": {
        "description": "Create a new training routine template...",
        "parameters": {
            "user_message": {
                "type": "string", 
                "description": "The user's message describing the training...",
                "required": True
            }
        }
    },
    "create_food": {
        "description": "Create a new food item template...",
        "parameters": {
            "user_message": {
                "type": "string",
                "description": "The user's message describing the food item...",
                "required": True
            }
        }
    }
}


async def log_message(user_message,user_id):
    try:

        agent_c = DeepseekClassification(api_key,categories=['food','exercise'],examples=log_classification_examples)
        classification_result = await agent_c.classify(user_message)
        if classification_result == 'food':

            extraction_schema = food_extraction_schema
            example_schema = food_example_schema
            agent_e = DeepseekExtractor(user_message=user_message,
                                extraction_schema=extraction_schema,
                                example_schema = example_schema,
                                api_key=api_key)
            extracted_list = await agent_e.extract()
            for item in extracted_list['foods']:
                food_obj = LogFood(**item)
                await log_food(food_obj,user_id)
            response = ResponseLogBot(message='your food has been succesfully added',request_data=extracted_list)
            return response
        elif classification_result == 'exercise':
            extraction_schema = training_extraction_schema
            example_schema = training_example_schema
            agent_e = DeepseekExtractor(user_message='KEEP NOTE, EACH SET IS ONE ITEM, SO FOR E.G IF I DID 2 SETS MEANS WE NEED 2 ITEMS IN THE LIST\n'+user_message,
                                extraction_schema=extraction_schema,
                                example_schema = example_schema,
                                api_key=api_key)
            extracted_list = await agent_e.extract()

            for item in extracted_list['trainings']:
                training_obj = LogTrainingRequest(**item)
                await log_training(training_obj,user_id)
            response = ResponseLogBot(message='your food has been succesfully added',request_data=extracted_list)
            return response
    except Exception as e:
        print(f"Error: {e}")





async def create_training(user_message,user_id):
    try:
        agent_e = DeepseekExtractor(user_message=user_message,
                                extraction_schema=training_routine_schema,
                                example_schema = training_routine_extraction_examples,
                                api_key=api_key)
        extracted_list = await agent_e.extract()
        training_model = TrainingRoutineRequest(**extracted_list)

        await create_training_routine(training_model,user_id)
        return training_model
    except Exception as e:
        print(f"Error: {e}")


async def create_food(user_message,user_id):
    try:
        agent_e = DeepseekExtractor(user_message=user_message,
                                extraction_schema=addfood_schema,
                                example_schema = addfood_extraction_examples,
                                api_key=api_key)
        extracted_list = await agent_e.extract()
        food_model = AddFood(**extracted_list)
        await add_food(food_model,user_id)
        return food_model
    except Exception as e:
        print(f"Error: {e}")



def create_wrapped_function_map(user_id: str):
    async def _log(**kw):
        return await log_message(kw["user_message"], user_id)

    async def _training(**kw):
        return await create_training(kw["user_message"], user_id)

    async def _food(**kw):
        return await create_food(kw["user_message"], user_id)

    async def _done(**_):
        return "Task completed"

    return {
        "log_message":     _log,
        "create_training": _training,
        "create_food":     _food,
        "task_complete":   _done,
    }