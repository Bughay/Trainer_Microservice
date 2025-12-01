from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()  

api_key = os.getenv("DEEPSEEK_API_KEY")


client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

system_prompt = 'You will receive a question and you will need to answer it as concise as possible. in one sentence since its a simple question. think deeply '
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"What is the largest country in the world?"},
    ],
    stream=False
)

chain_1 = response.choices[0].message.content


response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"What is the size of land in km in: {chain_1}"},
    ],
    stream=False
)

chain_2 = response.choices[0].message.content



response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Which country have the highest population in the world?"},
    ],
    stream=False
)

chain_3 = response.choices[0].message.content

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"What is the population of {chain_3} approximately"},
    ],
    stream=False
)

chain_4 = response.choices[0].message.content


response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Tell me if this statement is correct, answer with Yes or no ONLY:{chain_1} is the largest country in the world which spans {chain_2} km. while {chain_3} has the highest population in the world and its population is {chain_4}"},
    ],
    stream=False
)

chain_5 = response.choices[0].message.content

print(chain_1, chain_2, chain_3, chain_4, chain_5)
