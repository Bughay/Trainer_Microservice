from fastapi import APIRouter, HTTPException, status
from .model import LogTrainingRequest,LogTrainingResponse,TrainingRoutineRequest,TrainingRoutineResponse
from .database import log_training,create_training_routine,view_training
from datetime import date

router = APIRouter()



@router.post(
    "/training/log/{user_id}",
    response_model=LogTrainingResponse,
    status_code = status.HTTP_201_CREATED,
    summary="Log training",
    description="Logs the the training completed for the day",
)
async def log_training_endpoint(training:LogTrainingRequest,user_id):
    response = log_training(training,user_id)
    
    return response




@router.post(
    "/training/create/{user_id}",
    response_model=TrainingRoutineResponse,
    status_code = status.HTTP_201_CREATED,
    summary="Create a new training routine",
    description="Create a training routine to follow",
)
async def create_training_routine_endpoint(routine:TrainingRoutineRequest,user_id):
    response = create_training_routine(routine,user_id)
    return response
    





@router.get(
    "/training/view/{user_id}",
    # response_model=List[FoodItem],
    status_code = status.HTTP_201_CREATED,
    summary="track training based on date",
    description="view all the training performed in a date range",
)
async def view_training_endpoint(
    user_id:int,
    date_from:date,
    date_to:date
):
    response = view_training(user_id,date_from,date_to)
    print(response)
    return response