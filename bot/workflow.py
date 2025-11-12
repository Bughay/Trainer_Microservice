from .other_agents.extractor import DeepseekExtractor
from .other_agents.classification_agent import ClassificationAgent
from .other_agents.deepseek import DeepseekChat
import os
from dotenv import load_dotenv
from .personal_trainer.prompts import food_extraction_schema,food_example_schema,classification_examples,training_extraction_schema,training_example_schema

import sys
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]          
sys.path.insert(0, str(project_root))                       
from training.database import log_training
from training.model import LogTrainingRequest
from food.database import log_food
from food.model import LogFood
from pydantic import BaseModel
api_key = os.getenv("DEEPSEEK_API_KEY")


def log_message(user_message,user_id):

    agent_c = ClassificationAgent(api_key,categories=['food','exercise'],examples=classification_examples)
    classification_result = agent_c.classify(user_message)
    print(classification_result)
    print(type(classification_result))
    if classification_result == 'food':

        extraction_schema = food_extraction_schema
        example_schema = food_example_schema
        agent_e = DeepseekExtractor(user_message=user_message,
                            extraction_schema=extraction_schema,
                            example_schema = example_schema,
                            api_key=api_key)
        extracted_list = agent_e.extract()
        print(extracted_list)
        for item in extracted_list['foods']:
            food_obj = LogFood(**item)
            log_food(food_obj,1)
            return "sucess"
    elif classification_result == 'exercise':
        extraction_schema = training_extraction_schema
        example_schema = training_example_schema
        agent_e = DeepseekExtractor(user_message=user_message,
                            extraction_schema=extraction_schema,
                            example_schema = example_schema,
                            api_key=api_key)
        extracted_list = agent_e.extract()
        for item in extracted_list['trainings']:
            training_obj = LogTrainingRequest(**item)
            log_training(training_obj,1)
            print(log_training(training_obj,user_id))

    return "sucess"


system_message= 'you are layne norton and you will answer nutrition and training to the best of your ability'

def answer_questions(user_message,apikey):
    agent = DeepseekChat(system_message,apikey)
    ####RAG RAG RAG good sources######
    ### search search  good sites##
    answer = agent.one_shot(user_message)


            
            
            
            