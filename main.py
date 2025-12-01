from fastapi import FastAPI
from database import *
from food.route import router as food_router
from training.route import router as training_router
from auth.route import router as auth_router 
from recipes.route import router as recipe_router
from fastapi.middleware.cors import CORSMiddleware
from agent.route import router as agent_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5500",

        "http://127.0.0.1:5500"     
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

)

@app.on_event("startup")
async def startup():
    await init_db()  

@app.on_event("shutdown") 
async def shutdown():
    await close_db()  


app.include_router(food_router)
app.include_router(training_router)
app.include_router(auth_router)
app.include_router(recipe_router)
app.include_router(agent_router)




@app.get("/")
def root():
    return {"message": "Ego Nutrition API is running!"}

