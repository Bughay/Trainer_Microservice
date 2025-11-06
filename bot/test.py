from agents.classification_agent import ClassificationAgent




from agents.food_agent import DeepseekExtractor
import os
from dotenv import load_dotenv
from tools.examples import food_extraction_schema,food_classification_examples,food_example_schema
api_key = os.getenv("DEEPSEEK_API_KEY")
user_message = 'today i ate 500g chicken breast and 300g rice'
agent_c = ClassificationAgent(api_key,categories=['food','exercise'],examples=food_classification_examples)


agent_e = DeepseekExtractor(user_message=user_message,
                          extraction_schema=food_extraction_schema,
                          example_schema = food_example_schema,
                          api_key=api_key)

print(agent_e.extract())

