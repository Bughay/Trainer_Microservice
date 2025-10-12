import psycopg2
from datetime import datetime


def create_user(first_name:str,last_name:str,date_of_birth:str,email:str,gender:bool):
    try:

        conn = psycopg2.connect(dbname="ego_nutrition", user="lordmark1")
        cur = conn.cursor()
        

        insert_query = """
        INSERT INTO users(first_name,last_name,date_of_birth,email,gender,created_at,last_updated)
        VALUES(%s,%s,%s,%s,%s,%s,%s)
        """
        data_to_insert = (first_name,last_name,date_of_birth,email,gender,datetime.now(),datetime.now() )
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



def get_user_emails(email:str):
    try:

        conn = psycopg2.connect(dbname="ego_nutrition", user="lordmark1")
        cur = conn.cursor()
        

        query = """
        SELECT email
        FROM users
        WHERE email = %s
        """
        data_to_insert = [email]
        cur.execute(query,data_to_insert)
        results = cur.fetchall()
        
        cur.close()
        conn.close()
        email_list = [row[0] for row in results]  
        return email_list

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print('added succesfully')
        if cur:
            cur.close()
        if conn:
            conn.close()

