from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI
import pandas as pd
import pickle

pickle_win = open('model/model.pkl', 'rb')
model = pickle.load(pickle_win)
print(model)

class BodyModel(BaseModel):
    Age: int
    Sex: str
    ChestPainType: str
    RestingBP: int
    Cholesterol: int
    FastingBS: int
    RestingECG: str
    MaxHR: int
    ExerciseAngina: str
    Oldpeak: float
    ST_Slope: str

app = FastAPI()

@app.post('/predict')
async def predict(_body_: BodyModel):
    data = _body_.dict()
    data = pd.DataFrame([data])
    prediction = model.predict(data)
    return {"prediction": prediction.tolist()}