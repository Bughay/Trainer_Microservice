from fastapi import FastAPI

from food.route import router as food_router
from training.route import router as training_router
from bot.route import router as bot_router
from auth.route import router as auth_router 
app = FastAPI()


app.include_router(food_router)
app.include_router(training_router)
app.include_router(bot_router)
app.include_router(auth_router)



@app.get("/")
def root():
    return {"message": "Ego Nutrition API is running!"}

