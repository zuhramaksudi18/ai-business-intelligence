from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from typing import Dict, List, Any
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

router = APIRouter()

@router.get("/metrics")
def get_dashboard_metrics():
    """Get key metrics for the dashboard"""
    try:
        # In a real application, these would come from a database
        # For now, we'll generate some sample data
        
        # Calculate date range for the past 30 days
        today = datetime.now()
        date_range = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(30)]
        date_range.reverse()  # Oldest to newest
        
        # Generate sample metrics
        sentiment_scores = {
            "positive": 0.65,
            "neutral": 0.25,
            "negative": 0.10,
            "average_score": 0.75
        }
        
        engagement_metrics = {
            "total_interactions": 12500,
            "response_time_avg": 3.5,  # hours
            "resolution_rate": 0.85,
            "daily_trend": [5.5, 6.2, 7.0, 6.8, 7.5, 8.0, 8.2, 8.1, 7.9, 8.5,
                           8.6, 8.7, 8.5, 8.3, 8.2, 8.0, 8.1, 8.3, 8.5, 8.6,
                           8.8, 8.7, 8.5, 8.4, 8.2, 8.1, 8.3, 8.5, 8.7, 8.8]
        }
        
        demand_forecast = {
            "dates": [(today + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(1, 15)],
            "values": [120, 125, 130, 128, 135, 140, 138, 142, 145, 150, 155, 152, 158, 160]
        }
        
        # Return combined metrics
        return {
            "sentiment": sentiment_scores,
            "engagement": engagement_metrics,
            "forecast": demand_forecast,
            "date_range": date_range
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/sentiment-over-time")
def get_sentiment_over_time():
    """Get sentiment analysis results over time"""
    try:
        # Calculate date range for the past 30 days
        today = datetime.now()
        date_range = [(today - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(30)]
        date_range.reverse()  # Oldest to newest
        
        # Generate random sentiment data
        np.random.seed(42)  # For reproducibility
        positive_trend = np.linspace(0.50, 0.70, 30) + np.random.normal(0, 0.05, 30)
        neutral_trend = np.linspace(0.30, 0.20, 30) + np.random.normal(0, 0.03, 30)
        negative_trend = np.linspace(0.20, 0.10, 30) + np.random.normal(0, 0.02, 30)
        
        # Normalize to ensure they sum to 1.0
        sentiment_data = []
        for i in range(len(date_range)):
            total = positive_trend[i] + neutral_trend[i] + negative_trend[i]
            sentiment_data.append({
                "date": date_range[i],
                "positive": round(positive_trend[i] / total, 2),
                "neutral": round(neutral_trend[i] / total, 2),
                "negative": round(negative_trend[i] / total, 2)
            })
        
        return sentiment_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))