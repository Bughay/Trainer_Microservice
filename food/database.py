import os
import psycopg2
from dotenv import load_dotenv
from .model import AddFood,LogFood
load_dotenv()

database_url = os.getenv('DATABASE_URL')


def add_food(food: AddFood) :
    try:

        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        

        insert_query = """
        INSERT INTO food(user_id,food_name,is_solid,calories_100,protein_100,carbs_100,fats_100)

        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """
        data_to_insert = (
            food.user_id,
            food.food_name,
            food.is_solid,
            food.calories_100,
            food.protein_100,
            food.carbs_100,
            food.fats_100
        )
        cur.execute(insert_query,data_to_insert)
        conn.commit()
        
        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def get_all_food():
    try:
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()

        read_query = """
        SELECT DISTINCT(food_name), calories_100
        FROM food
        """
        cur.execute(read_query)
        results = cur.fetchall()

        return results


    except Exception as e:
        print(f"Error: {e}")
        return []

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def log_food(food:LogFood,user_id=1):
    try:

        conn = psycopg2.connect(database_url)
        cur = conn.cursor()
        calories_100 = (food.total_calories / food.total_grams) * 100
        protein_100 = (food.total_protein / food.total_grams) * 100
        carbs_100 = (food.total_carbs / food.total_grams) * 100
        fats_100 = (food.total_fats / food.total_grams) * 100 

        insert_query = """
        INSERT INTO food(user_id,food_name,is_solid,calories_100,protein_100,carbs_100,fats_100)

        VALUES(%s,%s,%s,%s,%s,%s,%s)
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
        cur.execute(insert_query,data_to_insert)

        insert_query_2 = """
        INSERT INTO food_entries(user_id,food_id,recipe_id,calories,total_grams,protein,carbs,fats)
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s)

        """
        
        food_id = cur.fetchone()[0]

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
        cur.execute(insert_query_2,data_to_insert_2)
        
        conn.commit()

        return AddFood(
            user_id=user_id,
            food_name=food.food_name,
            is_solid=True,
            calories_100=calories_100, 
            protein_100=protein_100,
            carbs_100=carbs_100,
            fats_100=fats_100
        )
        


    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()