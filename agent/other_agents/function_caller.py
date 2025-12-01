from openai import OpenAI
from dotenv import load_dotenv
import os
import json
load_dotenv()  


class DeepseekFunctionCaller():
    def __init__(self,api_key,user_prompt,tools):
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.user_prompt = user_prompt
        self.tools = tools
        self.system_prompt = self._create_system_prompt()
 
        
    def _tools_to_string(self):
        string = ''

        for function_name,_description in self.tools.items():
            
            string += f'FUNCTION NAME: {function_name}\n'
            string += f'FUNCTION DESCRIPTION: {_description['description']}\n'
            string += f'{function_name} PARAMETERS: \n'

            for parameter_name, parameter_details in _description['parameters'].items():
                if 'default' in parameter_details:
                    string += f'  - {parameter_name} :{parameter_details['description']}, DATA_TYPE:{parameter_details['type']}, REQUIRED: {parameter_details['required']}, DEFAULT: {parameter_details['default']}\n'
                else:
                    string += f'  - {parameter_name} :{parameter_details['description']}, DATA_TYPE:{parameter_details['type']}, REQUIRED: {parameter_details['required']}\n'
        return string
    
    def _create_system_prompt(self):
        tools_string = self._tools_to_string()

        system_prompt = f"""
            SYSTEM: You are an A function calling AI assitance who's sole job is extract the correct tool based on user_prompt and tool schema. 

            INSTRUCTIONS:
            1. Analyze the user's request carefully
            2. Analyze the tools provided
            3. Extract parameters accurately from the user's message

            Here is a description of available tools:
            {tools_string}

            Respond in the following JSON format:
            {{ 
                "reasoning": "Brief explanation of why you are/aren't using a tool",
                "action": "call_tool" or "direct_response",
                "tool_name": "name_of_tool_or_none",
                "parameters": {{
                    "param1": "value1",
                    "param2": "value2"
                }},
                "direct_response": "Your text response if no tool is needed"
            }}

            Examples:
            Example 1 (Tool call):
            {{
                "reasoning": "User asked for weather, so I'll use get_weather tool",
                "action": "call_tool", 
                "tool_name": "get_weather",
                "parameters": {{"location": "Tokyo", "unit": "celsius"}},
                "direct_response": ""
            }}

            Example 2 (Direct response):
            {{
                "reasoning": "User asked about AI concepts, no tool needed",
                "action": "direct_response",
                "tool_name": "",
                "parameters": {{}},
                "direct_response": "Artificial intelligence is the simulation of human intelligence processes by machines..."
            }}
            """
        return system_prompt
                
    def get_json_output(self):
        messages = [{"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": self.user_prompt}]

        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            response_format={
                'type': 'json_object'
            }
        )
        tool_schema = json.loads(response.choices[0].message.content)
        return tool_schema    

    

