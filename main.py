from fastapi import FastAPI
from users.route import router as user_router

app = FastAPI()

app.include_router(user_router)






