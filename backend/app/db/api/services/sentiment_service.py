from sqlalchemy.orm import Session
from app.core.ai.sentiment_analysis import SentimentAnalyzer
from typing import List, Dict, Any

class SentimentService:
    def __init__(self, db: Session = None, use_openai: bool = False):
        self.db = db
        self.analyzer = SentimentAnalyzer(use_openai=use_openai)
    
    def analyze_text(self, text: str) -> Dict[str, Any]:
        """
        Analyze sentiment of a single text
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary with sentiment analysis results
        """
        return self.analyzer.analyze_text(text)
    
    def analyze_batch(self, texts: List[str]) -> List[Dict[str, Any]]:
        """
        Analyze sentiment of multiple texts
        
        Args:
            texts: List of texts to analyze
            
        Returns:
            List of dictionaries with sentiment analysis results
        """
        return self.analyzer.analyze_batch(texts)
    
    def get_sentiment_trends(self, days: int = 30) -> Dict[str, Any]:
        """
        Get sentiment trends over time
        
        Args:
            days: Number of days to analyze
            
        Returns:
            Dictionary with sentiment trends
        """
        # In a real application, this would query the database
        # For now, return mock data
        return {
            "positive_trend": 0.15,  # 15% increase
            "negative_trend": -0.08,  # 8% decrease
            "overall_sentiment": "improving"
        }