from openai import OpenAI
from dotenv import load_dotenv
import os
import json
from .function_caller import DeepseekFunctionCaller

load_dotenv()



class ReActAgent():
    def __init__(self, api_key, tools, function_map):
        self.api_key = api_key
        self.tools = tools
        self.function_map = function_map
        self.memory = []

        self.tools['task_complete'] = {
            "description": "Call this when the task is finished and no more actions are needed",
            "parameters": {
                "completion_message": {
                    "type": "string", 
                    "description": "Confirmation that the task is complete",
                    "required": False
                }}
        }
        self.function_map['task_complete'] = lambda **_: "Task completed"
    async def run(self,user_prompt):

        self.memory = []
        self.memory.append(f'User Prompt: {user_prompt}')
        i = 0
        while i < 6:
            i = i +1

            current_prompt = f'Here is the memory {self.memory}, \n '
            function_caller = DeepseekFunctionCaller(
                api_key=self.api_key,
                user_prompt=current_prompt,
                tools=self.tools
            )
            action = function_caller.get_json_output()
            self.memory.append(f'Reasoning: {action["reasoning"]}')
            
            if action["tool_name"] == "task_complete" or action["tool_name"].strip() == "":
                self.memory.append("No more tools required - ending loop")
                print('ENDING THIS WORKED')
                break
                
            self.memory.append(f'Action: function_name {action["tool_name"]}, parameters: {action["parameters"]}')
            
            tool_name = action["tool_name"] 
            if tool_name in self.function_map :
                function_result = await self.function_map[tool_name](**action["parameters"])
                self.memory.append(f'Observation: {function_result}')
                
                current_prompt = f"Previous result: {function_result}. What should we do next?"
            else:
                self.memory.append(f'Observation: Function {tool_name} not found in function map')
                break
        
        return self.memory
    

    async def get_memory(self):
        return self.memory

    async def clear_memory(self):
        self.memory = []



    