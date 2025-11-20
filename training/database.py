from dotenv import load_dotenv
from .model import LogTrainingRequest,TrainingRoutineRequest,TrainingRoutineResponse,LogTrainingResponse
from database import get_pool 

load_dotenv()


async def log_training(training:LogTrainingRequest,user_id):
    try:


        pool = get_pool()
        async with pool.acquire() as conn:  
            insert_query = """
            INSERT INTO training(user_id,exercise_name,weight_,reps,notes)

            VALUES($1,$2,$3,$4,$5)
            RETURNING user_id,exercise_name,weight_,reps,notes
            """

            
            data_to_insert = (
                user_id,
                training.exercise_name,
                training.weight,
                training.reps,
                training.notes
            )
            result = await conn.fetchrow(insert_query, *data_to_insert)

            response = LogTrainingResponse(
                user_id=result['user_id'],
                exercise_name=result['exercise_name'],
                weight=result['weight_'],  
                reps=result['reps'],
                notes=result['notes']
            )
            
            return response
    except Exception as e:

        print(f"Error: {e}")


async def create_training_routine(routine: TrainingRoutineRequest, user_id):

    try:

        pool = get_pool()
        async with pool.acquire() as conn:  
            async with conn.transaction():


                insert_query = """
                INSERT INTO training_routine(user_id,training_routine_name,notes)

                VALUES($1,$2,$3)
                RETURNING routine_id
                """
                
                data_to_insert = (
                    user_id,
                    routine.training_routine_name,
                    routine.notes
                )
                result = await conn.fetchrow(insert_query, *data_to_insert)

                routine_id = result['routine_id']

                for exercise in routine.exercise_list:

                    insert_query_2 = """
                    INSERT INTO training_ingredients(user_id,routine_id,exercise_name,weight_,sets_,reps,notes)


                    VALUES($1, $2, $3, $4, $5, $6, $7)
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
                    await conn.execute(insert_query_2, *data_to_insert_2)

                response = {  
                    "user_id":user_id,
                    "training_routine_name":routine.training_routine_name,
                    "notes":routine.notes
                }

                return response
    except Exception as e:
        print(f"Error: {e}")
        




async def view_training(user_id,date_from,date_to):

    try:

        pool = get_pool()
        async with pool.acquire() as conn:  


            insert_query = """
            SELECT exercise_name, weight_, reps
            FROM training
            WHERE user_id = $1
            AND DATE(created_at) BETWEEN $2 AND $3
            """
            
            data_to_insert = (
                user_id,
                date_from,
                date_to
            )
            results = await conn.fetch(insert_query, *data_to_insert)


            return results

    except Exception as e:
        print(f"Error: {e}")
