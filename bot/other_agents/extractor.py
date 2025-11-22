from openai import OpenAI
from dotenv import load_dotenv
import os
import json
load_dotenv()  

api_key = os.getenv("DEEPSEEK_API_KEY")
class DeepseekExtractor:
    def __init__(self,user_message,extraction_schema,example_schema,api_key):
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.user_message = user_message
        self.extraction_schema = extraction_schema
        self.example_schema = example_schema
        self.api_key = api_key
        self.extraction_prompt = """You will be performing extraction of data from the text as a JSON file using the following schema
                    keep note that the key is the variable and the value is the description
                                        """
    async def extract(self):
        response = self.client.chat.completions.create(
        model="deepseek-chat",
        messages=[
                {
                    "role": "system",
                    "content": f"""
                    <extraction_prompt>
                    {self.extraction_prompt}
                    </extraction_prompt>
                    <extraction_schema>
                    {self.extraction_schema}
                    </extraction_schema>

                    Stay true to the return format and do not deviate from it
                    <return_format>
                    {self.example_schema}
                    </return_format>
                                    """

                },
                {
                    "role": "user",
                    "content": self.user_message,
                },
            ],
            response_format={"type": "json_object"},
            temperature=0,
        )
        extracted_data = json.loads(response.choices[0].message.content)
        return extracted_data
    