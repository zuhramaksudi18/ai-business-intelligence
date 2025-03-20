from pydantic import BaseModel
from typing import List, Dict, Any, Optional
from datetime import datetime

class SentimentAnalysisResult(BaseModel):
    text: str
    sentiment: str
    confidence: float
    source: str
    created_at: Optional[datetime] = None

class SentimentAnalysisRequest(BaseModel):
    text: str

class BatchSentimentRequest(BaseModel):
    texts: List[str]
    
class BatchSentimentResponse(BaseModel):
    results: List[SentimentAnalysisResult]