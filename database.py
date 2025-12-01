import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')
pool = None

async def init_db():
    global pool
    pool = await asyncpg.create_pool(
        DATABASE_URL,
        min_size=5,
        max_size=20
    )
    print("✅ Database pool created for all services")
    return pool

async def close_db():
    global pool
    if pool:
        await pool.close()
        print("✅ Database pool closed")

def get_pool():
    if pool is None:
        raise RuntimeError("Database not initialized. Call init_db() first.")
    return pool