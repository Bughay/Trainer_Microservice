from pydantic import BaseModel
from typing import List

class LogTrainingRequest(BaseModel):
    exercise_name: str
    weight: float
    reps: int
    notes: str

class LogTrainingResponse(BaseModel):
    user_id: int
    exercise_name: str
    weight: float
    reps: int
    notes: str


class TrainingRoutineRequestList(BaseModel):
    exercise_name:str
    weight_: int
    sets_: int
    reps: int
    notes: str

class TrainingRoutineRequest(BaseModel):
    training_routine_name:str
    exercise_list: List[TrainingRoutineRequestList]
    notes:str

class TrainingRoutineResponse(BaseModel):
    training_routine_name:str
    notes:str



