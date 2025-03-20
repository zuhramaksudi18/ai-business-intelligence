from sqlalchemy.orm import Session
from app.core.ai.time_series_forecasting import TimeSeriesForecaster
from typing import List, Dict, Any
import pandas as pd

class ForecastService:
    def __init__(self, db: Session = None):
        self.db = db
    
    def train_model(self, 
                   data: pd.DataFrame,
                   date_column: str,
                   target_column: str,
                   model_type: str = 'prophet',
                   **kwargs) -> Dict[str, Any]:
        """
        Train a forecasting model
        
        Args:
            data: DataFrame with time series data
            date_column: Name of column containing dates
            target_column: Name of column containing target values
            model_type: Type of model to use ('prophet' or 'lstm')
            
        Returns:
            Dictionary with training results
        """
        forecaster = TimeSeriesForecaster(model_type=model_type)
        return forecaster.train(
            data=data,
            date_column=date_column,
            target_column=target_column,
            **kwargs
        )
    
    def generate_forecast(self, 
                         data: pd.DataFrame,
                         date_column: str,
                         target_column: str,
                         periods: int = 30,
                         frequency: str = 'D',
                         model_type: str = 'prophet',
                         **kwargs) -> Dict[str, Any]:
        """
        Train a model and generate forecast
        
        Args:
            data: DataFrame with time series data
            date_column: Name of column containing dates
            target_column: Name of column containing target values
            periods: Number of periods to forecast
            frequency: Frequency of predictions
            model_type: Type of model to use
            
        Returns:
            Dictionary with forecast results
        """
        forecaster = TimeSeriesForecaster(model_type=model_type)
        
        # Train the model
        forecaster.train(
            data=data,
            date_column=date_column,
            target_column=target_column,
            **kwargs
        )
        
        # Generate forecast
        return forecaster.predict(
            periods=periods,
            frequency=frequency
        )