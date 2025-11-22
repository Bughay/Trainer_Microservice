import asyncio
from bot.workflow import create_training, create_food
from database import init_db, close_db
async def test_functions():
    await init_db()  

    answer = await create_training('hi ,Full body power workout. Squats at 245 lbs, 5 sets of 3. Bench press at 200 lbs, 5 sets of 3. Barbell rows at 155 lbs, 4 sets of 5. Accessory: planks for 60 seconds, 3 sets. Working on pure strength gains."', 3)
    answer_2 = await create_food('So the food i wana create is brazilian fish, it has 200 calories 20 g protein 5 g fats and 0 carbs', 2)
    
    print('test answer 1 ')
    print(answer)
    
    print('test answer 2')
    print(answer_2)
    await close_db()  

# Run the async test
asyncio.run(test_functions())