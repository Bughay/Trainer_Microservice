from dotenv import load_dotenv
from .model import AddFood,LogFood, ResponseAddFood
from database import get_pool 
load_dotenv()



async def add_food(food: AddFood,user_id:int):
    try:

        pool = get_pool()
        async with pool.acquire() as conn:         
            async with conn.transaction():
                insert_query = """
                INSERT INTO food(user_id,food_name,calories_100,protein_100,carbs_100,fats_100)

                VALUES($1, $2, $3, $4, $5, $6)
                """
                data_to_insert = (
                    user_id,
                    food.food_name,
                    food.calories_100,
                    food.protein_100,
                    food.carbs_100,
                    food.fats_100
                )
                await conn.execute(insert_query,*data_to_insert)

                response = ResponseAddFood(*data_to_insert)
                return response
    except Exception as e:
        print(f"Error: {e}")
        return False
 





async def get_all_food():

    try:
        pool = get_pool()
        async with pool.acquire() as conn:         


            read_query = """
            SELECT DISTINCT(food_name), calories_100
            FROM food
            """
            results = await conn.fetch(read_query)

            return results


    except Exception as e:
        print(f"Error: {e}")
        return []
    




async def log_food(food:LogFood,user_id):
    try:
        pool = get_pool()
        async with pool.acquire() as conn:   
            async with conn.transaction():       

                calories_100 = (food.total_calories / food.total_grams) * 100
                protein_100 = (food.total_protein / food.total_grams) * 100
                carbs_100 = (food.total_carbs / food.total_grams) * 100
                fats_100 = (food.total_fats / food.total_grams) * 100 

                insert_query = """
                INSERT INTO food_Cache(user_id,food_name,is_solid,calories_100,protein_100,carbs_100,fats_100)

                VALUES($1, $2, $3, $4, $5, $6, $7)
                RETURNING food_id
                """

                
                data_to_insert = (
                    user_id,
                    food.food_name,
                    True,
                    calories_100,
                    protein_100,
                    carbs_100,
                    fats_100,
                )
                food_id = await conn.fetchval(insert_query, *data_to_insert)

                insert_query_2 = """
                INSERT INTO food_entries(user_id,food_id,recipe_id,calories,total_grams,protein,carbs,fats)
                VALUES($1, $2, $3, $4, $5, $6, $7, $8)

                """
                
                data_to_insert_2 = (
                    user_id,
                    food_id,
                    None,
                    food.total_calories,
                    food.total_grams,
                    food.total_protein,
                    food.total_carbs,
                    food.total_fats
                )
                await conn.execute(insert_query_2,*data_to_insert_2)
                
                response = ResponseAddFood(
                    user_id=user_id,
                    food_name=food.food_name,
                    is_solid=True,
                    calories_100=calories_100, 
                    protein_100=protein_100,
                    carbs_100=carbs_100,
                    fats_100=fats_100
                )
                return response
        
    except Exception as e:
        if conn:
            await conn.rollback()
        print(f"Error: {e}")




async def get_food_by_user(user_id:int):
    try:
        pool = get_pool()
        async with pool.acquire() as conn:         

            read_query = """
            SELECT DISTINCT(food_name), calories_100
            FROM food
            WHERE user_id = $1
            """

            results = await conn.fetch(read_query,user_id)

            return results


    except Exception as e:
        print(f"Error: {e}")
        return []

