from .other_agents.extractor import DeepseekExtractor
from .other_agents.classification_agent import ClassificationAgent
from .other_agents.deepseek import DeepseekChat
import os
from .personal_trainer.prompts import food_extraction_schema,food_example_schema,log_classification_examples,training_extraction_schema,training_example_schema,training_routine_schema,training_routine_extraction_examples
from .model import ResponseLogBot
import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]          
sys.path.insert(0, str(project_root))                       
from training.database import log_training
from training.model import LogTrainingRequest
from food.database import log_food
from food.model import LogFood
from training.database import create_training_routine
from pydantic import BaseModel
api_key = os.getenv("DEEPSEEK_API_KEY")


async def log_message(user_message,user_id):

    agent_c = ClassificationAgent(api_key,categories=['food','exercise'],examples=log_classification_examples)
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




async def create_training(user_message,user_id):
    agent_e = DeepseekExtractor(user_message=user_message,
                            extraction_schema=training_routine_schema,
                            example_schema = training_routine_extraction_examples,
                            api_key=api_key)
    extracted_list = await agent_e.extract()
    create_training_routine(extracted_list,user_id)
    return extracted_list




            
            
            