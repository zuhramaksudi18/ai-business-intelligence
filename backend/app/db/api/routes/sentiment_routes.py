from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.core.ai.sentiment_analysis import SentimentAnalyzer
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()
analyzer = SentimentAnalyzer(use_openai=False)  # Default to Hugging Face

class SentimentRequest(BaseModel):
    text: str

class BatchSentimentRequest(BaseModel):
    texts: List[str]

@router.post("/analyze")
def analyze_sentiment(request: SentimentRequest):
    """Analyze sentiment of a single text"""
    try:
        result = analyzer.analyze_text(request.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/batch")
def analyze_batch(request: BatchSentimentRequest):
    """Analyze sentiment of multiple texts"""
    try:
        results = analyzer.analyze_batch(request.texts)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))