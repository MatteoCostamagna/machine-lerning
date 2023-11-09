import numpy as np
from fastapi import FastAPI, Request
from pydantic import BaseModel
import pickle
from sklearn.linear_model import LinearRegression

class WineQualityPredictionInput(BaseModel):
    fixed_acidity: float
    volatile_acidity: float
    citric_acid: float
    residual_sugar: float
    chlorides: float
    free_sulfur_dioxide: float
    density: float
    pH: float
    sulphates: float
    alcohol: float
    quality: int

# Ho caricato il training model
model = pickle.load(open(r"C:\Users\ICTS22-24.459\Desktop\cartella_progetto\cartella_modello_ml\il_mio_modello.pkl", "rb"))

app = FastAPI()

#Ho creato l'api che prende i dati e fa una predizione grazie al modello
@app.post("/predict")
async def predict(request: Request, wine_quality_prediction_input: WineQualityPredictionInput):
    data = await request.json()
    prediction = model.predict([wine_quality_prediction_input])
    return {"prediction": prediction}

