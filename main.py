from fastapi import FastAPI

from food.route import router as food_router
from training.route import router as training_router
from bot.route import router as bot_router
from auth.route import router as auth_router 
from bot.route import router as personal_trainer_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",
        "http://127.0.0.1:5500"     # <-- add this line
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(food_router)
app.include_router(training_router)
app.include_router(bot_router)
app.include_router(auth_router)
app.include_router(personal_trainer_router)




@app.get("/")
def root():
    return {"message": "Ego Nutrition API is running!"}

