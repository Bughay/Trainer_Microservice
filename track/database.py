import os
import psycopg2
from dotenv import load_dotenv
from .model import AddFood
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