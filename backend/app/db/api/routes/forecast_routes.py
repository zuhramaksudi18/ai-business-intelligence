from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.ai.time_series_forecasting import TimeSeriesForecaster
from pydantic import BaseModel
from typing import List, Dict, Any, Optional
import pandas as pd

router = APIRouter()

class ForecastRequest(BaseModel):
    date_column: str
    target_column: str
    periods: int = 30
    frequency: str = 'D'
    model_type: str = 'prophet'
    data: Optional[List[Dict[str, Any]]] = None
    file_path: Optional[str] = None

@router.post("/train")
def train_forecast_model(request: ForecastRequest):
    """Train a forecasting model"""
    try:
        forecaster = TimeSeriesForecaster(model_type=request.model_type)
        
        # Use provided data or load from file
        if request.data:
            df = pd.DataFrame(request.data)
        elif request.file_path:
            df = pd.read_csv(request.file_path)
        else:
            raise HTTPException(status_code=400, detail="No data or file path provided")
        
        # Train the model
        result = forecaster.train(
            data=df,
            date_column=request.date_column,
            target_column=request.target_column
        )
        
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/predict")
def generate_forecast(request: ForecastRequest):
    """Generate a forecast"""
    try:
        forecaster = TimeSeriesForecaster(model_type=request.model_type)
        
        # Use provided data or load from file
        if request.data:
            df = pd.DataFrame(request.data)
        elif request.file_path:
            df = pd.read_csv(request.file_path)
        else:
            raise HTTPException(status_code=400, detail="No data or file path provided")
        
        # Train the model first
        forecaster.train(
            data=df,
            date_column=request.date_column,
            target_column=request.target_column
        )
        
        # Generate forecast
        forecast = forecaster.predict(
            periods=request.periods,
            frequency=request.frequency
        )
        
        return forecast
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))