from fastapi import FastAPI
from pydantic import BaseModel
from modelLoader import LattueseModelLoader
import pandas as pd

app = FastAPI()

class InputData(BaseModel):
    DaySincePlanted: int
    Humidity: float
    Tempreture: float
    DailySunExposure: float
    WaterPhLevel: float
    NutrientLevel: float
    SunExposureIntensityLux: float
    VisibleLightWaveLength: float
    TempretureDeviation: float
    HumidityDeviation: float
    FanSpeed: float

@app.post("/")
def predict(input_data: InputData):
    data = {
        'Day since planted': input_data.DaySincePlanted,
        'Humidity (%)': input_data.Humidity,
        'Temperature (°C)': input_data.Tempreture,
        'Daily Sun Exposure (hours)': input_data.DailySunExposure,
        'Water pH Level': input_data.WaterPhLevel,
        'Nutrient Level': input_data.NutrientLevel,
        'Sun Exposure Intensity (Lux)': input_data.SunExposureIntensityLux,
        'Visible Light Wavelength (nm)': input_data.VisibleLightWaveLength,
        'Temperature Deviation (°C)': input_data.TempretureDeviation,
        'Humidity Deviation (%)': input_data.HumidityDeviation,
        'Fan Speed (%)': input_data.FanSpeed,
    }
    X = pd.DataFrame(data, index=[0])

    model_loader = LattueseModelLoader()
    prediction = model_loader.predict(X)

    return {"prediction": prediction.tolist()}