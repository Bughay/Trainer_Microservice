from fastapi import APIRouter, HTTPException, status,Depends
from .model import LogTrainingRequest,LogTrainingResponse,TrainingRoutineRequest,TrainingRoutineResponse
from .database import log_training,create_training_routine,view_training
from datetime import date
from auth.security import get_current_user 

router = APIRouter(prefix="/training", tags=["training"])



@router.post(
    "/training/log/training",
    response_model=LogTrainingResponse,
    status_code = status.HTTP_201_CREATED,
    summary="Log training",
    description="Logs the the training completed for the day",
)
async def log_training_endpoint(training:LogTrainingRequest,current_user:dict=Depends(get_current_user)):
    user_id = current_user['user_id']
    response = await log_training(training,user_id)
    
    return response




@router.post(
    "/training/create/training",
    response_model=TrainingRoutineResponse,
    status_code = status.HTTP_201_CREATED,
    summary="Create a new training routine",
    description="Create a training routine to follow",
)
async def create_training_routine_endpoint(routine:TrainingRoutineRequest,current_user: dict = Depends(get_current_user)):
    user_id = current_user['user_id']
    response = await create_training_routine(routine,user_id)
    return response
    





@router.get(
    "/training/view/training",
    # response_model=List[FoodItem],
    status_code = status.HTTP_201_CREATED,
    summary="track training based on date",
    description="view all the training performed in a date range",
)
async def view_training_endpoint(
    date_from:date,
    date_to:date,
    current_user:dict = Depends(get_current_user),

):
    user_id = current_user['user_id']
    response = await view_training(user_id,date_from,date_to)
    print(response)
    return response