from fastapi import FastAPI
import pickle
import pandas as pd
from pydantic import BaseModel
from prometheus_client import Counter, generate_latest
from fastapi.responses import Response

# Load the model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# FastAPI app
app = FastAPI()

# Metrics
prediction_counter = Counter("predictions_total", "Total predictions made")
error_counter = Counter("prediction_errors_total", "Total prediction errors")

class InputData(BaseModel):
    Pclass: int
    Sex: int
    Age: float
    Fare: float

@app.post("/predict")
def predict(data: InputData):
    try:
        df = pd.DataFrame([data.dict()])
        prediction = model.predict(df)[0]
        prediction_counter.inc()
        return {"prediction": int(prediction)}
    except Exception as e:
        error_counter.inc()
        return {"error": str(e)}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")
