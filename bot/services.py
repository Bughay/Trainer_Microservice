from bot.agents.food_agent import DeepseekExtractor
import os
from dotenv import load_dotenv
from bot.tools.examples import food_extraction_schema,food_example_schema
api_key = os.getenv("DEEPSEEK_API_KEY")


def workflow(user_message):

    # agent_c = ClassificationAgent(api_key,categories=['food','exercise'],examples=food_classification_examples)


    agent_e = DeepseekExtractor(user_message=user_message,
                            extraction_schema=food_extraction_schema,
                            example_schema = food_example_schema,
                            api_key=api_key)
    return agent_e.extract()