from dotenv import load_dotenv
from database import get_pool 
from .model import UserFoodItem,ReadRecipeResponse,CreateRecipeRequest
from typing import List
load_dotenv()



async def read_food_items(user_id):
    try:


        pool = get_pool()
        async with pool.acquire() as conn:
            select_query = """
            SELECT food_id,food_name,calories_100
            FROM food
            WHERE user_id = $1

            
            """
        


            data_to_insert=user_id
            results = await conn.fetch(select_query, data_to_insert)
            
            food_dict = [dict(food) for food in results]
            food_items = ReadRecipeResponse(
                food_items = food_dict
            )
            return food_items
    except Exception as e:
        print(f"Error: {e}")
    
async def create_recipe(recipe:CreateRecipeRequest,user_id):
    try:


        pool = get_pool()
        async with pool.acquire() as conn:
            insert_query = """
            INSERT INTO recipes(user_id,recipe_name,instructions)

            VALUES($1, $2, $3)
            RETURNING recipe_id
            
            """
        

            data_to_insert= (
                user_id,
                recipe.recipe_name,
                recipe.recipe_instructions,

            )
            result = await conn.fetchrow(insert_query, *data_to_insert)
            recipe_id = result['recipe_id']
            

            recipe_ingridients_list = recipe.ingredients
            for food in recipe_ingridients_list:
                food_id = food.food_id
                total_grams = food.total_grams
                insert_query_2 = """
                INSERT INTO recipe_ingredients(recipe_id,food_id,total_grams)

                VALUES($1,$2,$3)

                """

                data_to_insert_2 = (
                    recipe_id,
                    food_id,
                    total_grams
                )
                await conn.execute(insert_query_2, *data_to_insert_2)
            return recipe

    except Exception as e:
        print(f"Error here: {e}")




async def get_recipe(user_id):
    try:


        pool = get_pool()
        async with pool.acquire() as conn:
            select_query = """
            SELECT DISTINCT
                r.recipe_name,
                r.instructions
            FROM   recipes r
            JOIN   recipe_ingredients ri ON ri.recipe_id = r.recipe_id
            WHERE  r.user_id = $1;
            
            """
        


            data_to_insert=user_id
            results = await conn.fetch(select_query, data_to_insert)
            
            return results
    except Exception as e:
        print(f"Error: {e}")   