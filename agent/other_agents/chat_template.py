
from openai import OpenAI

class DeepseekChat:
    def __init__(self,api_key,system_message):
        self.client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")
        self.system_message = system_message
        self.memory = [
            {"role": "system", "content": self.system_message}
        ]
    def begin_conversation(self):
        while True:
            print('ask your question to deep seek')
            message = input()
            if message == 'break':
                print('closing deep seek')
                break
            self.memory.append({"role":"user","content":message})
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=self.memory,
            )
            self.memory.append({"role": "assistant", "content": response.choices[0].message.content})
            print('LLM answer')
            print(response.choices[0].message.content)

    def one_shot(self,user_message,temperature=0.6,max_tokens=4096):
        response = self.client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content":self.system_message },
            {"role": "user", "content": user_message},
        ],
        stream=False,
        temperature = temperature,
        max_tokens = max_tokens
    )
        return response.choices[0].message.content























        

        