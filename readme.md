# FastAPI Lettuce Model Loader

This repository contains a FastAPI application that loads a trained machine learning model for lettuce prediction and provides an API endpoint for making predictions.

## Description

The FastAPI Lettuce Model Loader is a web application that allows users to input various parameters related to lettuce growth and receives predictions from a pre-trained machine learning model. The application is built using FastAPI, a modern and fast web framework for building APIs with Python.

## Features

- Loads a pre-trained machine learning model for lettuce classification
- Provides an API endpoint for making predictions
- Accepts input parameters related to lettuce growth
- Returns predictions as float value

## Installation

To run the FastAPI Lettuce Model Loader locally, follow these steps:

1. Clone the repository:

git clone https://github.com/MoAly7yaei/PredictionModel.git

2. Navigate to the project directory:

cd fastapi-lettuce-model-loader

3. Install the required dependencies:

pip install -r requirements.txt

4. Start the FastAPI application:

uvicorn main:app --reload

5. The application will be accessible at `http://localhost:8000`.

## Usage

To make predictions using the FastAPI Lettuce Model Loader, follow these steps:

1. Make a POST request to the `/predict` endpoint with the following parameters:
- `DaySincePlanted`: int
- `Humidity`: float
- `Tempreture`: float
- `DailySunExposure`: float
- `WaterPhLevel`: float
- `NutrientLevel`: float
- `SunExposureIntensityLux`: float
- `VisibleLightWaveLength`: float
- `TempretureDeviation`: float
- `HumidityDeviation`: float
- `FanSpeed`: float

2. The API will return a predictions for ETH.