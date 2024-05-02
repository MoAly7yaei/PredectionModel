import joblib
import os
import pandas as pd

BASE_DIR = os.getcwd()
MODELS_DIR = BASE_DIR + '/models/'

class LattueseModelLoader:
    def __init__(self):
        self.model_dir = MODELS_DIR + '/lettuse_v01alpha.joblib'
        self.model = self.load(self.model_dir)

    def load(self, model_dir):
        return joblib.load(model_dir)

    def fetchingData(self, DaySincePlanted, Humidity, Tempreture, DailySunExposure,
                     WaterPhLevel, NutrientLevel, SunExposureIntensityLux,
                     VisibleLightWaveLength, TempretureDeviation, HumidityDeviation, FanSpeed):
        data = {
            'Day since planted': DaySincePlanted,
            'Humidity (%)': Humidity,
            'Temperature (°C)': Tempreture,
            'Daily Sun Exposure (hours)': DailySunExposure,
            'Water pH Level': WaterPhLevel,
            'Nutrient Level': NutrientLevel,
            'Sun Exposure Intensity (Lux)': SunExposureIntensityLux,
            'Visible Light Wavelength (nm)': VisibleLightWaveLength,
            'Temperature Deviation (°C)': TempretureDeviation,
            'Humidity Deviation (%)': HumidityDeviation,
            'Fan Speed (%)': FanSpeed,
        }
        X = pd.DataFrame(data, index=[0])
        return X

    def predict(self, X):
        return self.model.predict(X)

    def save(self):
        joblib.dump(self.model, self.model_dir)

    def train(self, X, y):
        self.model = self.model.fit(X, y)
        self.save()