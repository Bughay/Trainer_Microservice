import os
import psycopg2
from dotenv import load_dotenv
from .model import LogTrainingRequest,TrainingRoutineRequest,TrainingRoutineResponse
load_dotenv()

database_url = os.getenv('DATABASE_URL')


def log_training(training:LogTrainingRequest,user_id):
    try:

        conn = psycopg2.connect(database_url)
        cur = conn.cursor()


        insert_query = """
        INSERT INTO training(user_id,exercise_name,weight_,reps,notes)

        VALUES(%s,%s,%s,%s,%s)
        RETURNING user_id,exercise_name,weight_,reps,notes
        """

        
        data_to_insert = (
            user_id,
            training.exercise_name,
            training.weight,
            training.reps,
            training.notes
        )
        response = { 
            "user_id":user_id,
            "exercise_name": training.exercise_name,
            "weight":training.weight,
            "reps":training.reps,
            "notes":training.notes

        }


 
        cur.execute(insert_query,data_to_insert)


        

        conn.commit()

        return response
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def create_training_routine(routine: TrainingRoutineRequest, user_id):
    try:

        conn = psycopg2.connect(database_url)
        cur = conn.cursor()


        insert_query = """
        INSERT INTO training_routine(user_id,training_routine_name,notes)

        VALUES(%s,%s,%s)
        RETURNING routine_id
        """
        
        data_to_insert = (
            user_id,
            routine.training_routine_name,
            routine.notes
        )
        cur.execute(insert_query,data_to_insert)
        routine_id = cur.fetchone()[0]

        for exercise in routine.exercise_list:

            insert_query_2 = """
            INSERT INTO training_ingredients(user_id,routine_id,exercise_name,weight_,sets_,reps,notes)


            VALUES(%s,%s,%s,%s,%s,%s,%s)
            """

            
            data_to_insert_2 = (
                user_id,
                routine_id,
                exercise.exercise_name,
                exercise.weight_,
                exercise.sets_,
                exercise.reps,
                exercise.notes
            )
            cur.execute(insert_query_2,data_to_insert_2)

        response = {  
            "user_id":user_id,
            "training_routine_name":routine.training_routine_name,
            "notes":routine.notes
        }
        conn.commit()

        return response
    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()


def view_training(user_id,date_from,date_to):
    try:
        conn = psycopg2.connect(database_url)
        cur = conn.cursor()


        insert_query = """
        SELECT exercise_name, weight_, reps
        FROM training
        WHERE user_id = %s 
        AND DATE(created_at) BETWEEN %s AND %s
        """
        
        data_to_insert = (
            user_id,
            date_from,
            date_to
        )
        cur.execute(insert_query,data_to_insert)
        results = cur.fetchall()


        return results

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
