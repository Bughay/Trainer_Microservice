from openai import OpenAI
import os
from dotenv import load_dotenv
import json

load_dotenv()

api_key = os.getenv('DEEPSEEK_APIKEY')


class ClassificationAgent:
    def __init__(self,api_key,
                 categories,
                 examples):
        self.api_key = api_key
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

        self.system_message = f"""Act as a text classification expert. Follow these rules strictly:
                                                                                                           
                    1. Task: Classify the user's text into exactly one of these categories:  
                    {categories}

                    2. Guidelines:  
                    - Respond ONLY with the category name. No explanations.  
                    - If uncertain, choose the closest match.  
                    - Ignore typos/grammar errors. 
                    - Output in JSON format
                    - look clearly at the examples and the JSON format requirement

                    3. Examples (for context):  
                        {examples}"""

    async def classify(self,user_message):


        client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": self.system_message},
                    {"role": "user", "content": user_message},
                ],
            stream=False,
                    response_format={
                        'type': 'json_object'
                }
            )
        result_json = response.choices[0].message.content
        result_dict = json.loads(result_json)                          # -> dict
        return result_dict["category"]


