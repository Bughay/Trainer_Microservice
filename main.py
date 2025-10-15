from fastapi import FastAPI
from users.route import router as user_router
from food.route import router as food_router
from training.route import router as training_router
app = FastAPI()

app.include_router(user_router)
app.include_router(food_router)
app.include_router(training_router)




