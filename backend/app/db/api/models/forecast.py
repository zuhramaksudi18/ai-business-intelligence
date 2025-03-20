from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class TimeSeriesDataPoint(BaseModel):
    date: str
    value: float

class ForecastRequest(BaseModel):
    date_column: str
    target_column: str
    periods: int = 30
    frequency: str = 'D'
    model_type: str = 'prophet'
    data: Optional[List[Dict[str, Any]]] = None
    file_path: Optional[str] = None

class ForecastResult(BaseModel):
    forecast: List[Dict[str, Any]]
    plot: Optional[str] = None
    components_plot: Optional[str] = None