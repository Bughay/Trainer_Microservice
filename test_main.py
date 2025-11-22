# import asyncio
# from bot.workflow import create_training, create_food
# from database import init_db, close_db
# async def test_functions():
#     await init_db()  

#     answer = await create_training('hi ,Full body power workout. Squats at 245 lbs, 5 sets of 3. Bench press at 200 lbs, 5 sets of 3. Barbell rows at 155 lbs, 4 sets of 5. Accessory: planks for 60 seconds, 3 sets. Working on pure strength gains."', 3)
#     answer_2 = await create_food('So the food i wana create is brazilian fish, it has 200 calories 20 g protein 5 g fats and 0 carbs', 2)
    
#     print('test answer 1 ')
#     print(answer)
    
#     print('test answer 2')
#     print(answer_2)
#     await close_db()  

# # Run the async test
# asyncio.run(test_functions())


from openai import OpenAI
import os
from dotenv import load_dotenv
import json
from bot.workflow import personal_trainer_agent

load_dotenv()
api_key = os.getenv('DEEPSEEK_APIKEY')

def test_agent(user_prompt: str):
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"   # no trailing space
    )
    tools = function_schemas
    system_prompt = (
        "You are a personal-trainer AI. "
        "Pick exactly one of these tools: log_message, create_training, create_food. "
        "Here is the tools {tools}"
        "Reply in valid JSON that matches this schema:\n"
        '{"name": "tool_name"}'
    )

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}   # ← must be dict, not string
    ]

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        response_format={"type": "json_object"},  # DeepSeek: only 'type' is allowed
        temperature=0
    )

    return response.choices[0].message.content


test = [
    ["I just ate 200 g of salmon and a 100g of rice for dinner.", "log_message"],
    ["Create a push-day template: bench-press 2 sets 3 reps 100kg, incline DB press 25 kg for 5 sets of 8reps", "create_training"],
    ["Add a food template: skinless chicken breast, 165 kcal, 31 g protein, 0 g carbs, 3.6 g fat per 100 g.", "create_food"],
    ["Create a food entry: cooked quinoa, 120 kcal, 4.4 g protein, 21 g carbs, 1.9 g fat per 100 g.", "create_food"],
    ["Create a food template for avocado: 160 kcal, 2 g protein, 15 g fat.","create_food"],
    ['Today i did 100kg bench for 5 reps and then i squatted 50 kg for 2 sets of 50 reps and ended the day with 12 kg bicep curls for 3x12',"log_message"]

]
import asyncio



async def main():
    user_id = 2
    for item in test:
        await personal_trainer_agent(item[0],user_id)


if __name__ == '__main__':
    asyncio.run(main())
