import requests
import json
import pandas as pd
import os
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class DataCollector:
    """
    Class to collect data from various sources
    """
    
    def __init__(self, api_keys: Dict[str, str] = None):
        """
        Initialize the data collector
        
        Args:
            api_keys: Dictionary of API keys for different services
        """
        self.api_keys = api_keys or {}
    
    def collect_social_media_data(self, platform: str, query: str, days: int = 7) -> pd.DataFrame:
        """
        Collect data from social media platforms
        
        Args:
            platform: Social media platform (twitter, reddit, etc.)
            query: Search query
            days: Number of days to look back
            
        Returns:
            DataFrame with collected data
        """
        logger.info(f"Collecting social media data from {platform} for query: {query}")
        
        # In a real application, this would call the platform's API
        # For now, we'll return mock data
        
        # Generate mock data
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        dates = []
        current_date = start_date
        while current_date <= end_date:
            dates.append(current_date)
            current_date += timedelta(days=1)
        
        # Generate random posts with the query term
        import random
        
        posts = []
        for date in dates:
            num_posts = random.randint(5, 20)
            for _ in range(num_posts):
                sentiment = random.choice(["positive", "neutral", "negative"])
                text_templates = {
                    "positive": [
                        f"I really love the {query}! It's amazing!",
                        f"Just got the new {query} and it's fantastic!",
                        f"The {query} is the best product I've used this year!"
                    ],
                    "neutral": [
                        f"Just heard about the {query}. Anyone tried it?",
                        f"Looking for reviews of {query}. Any thoughts?",
                        f"Thinking about getting the {query}. Not sure yet."
                    ],
                    "negative": [
                        f"Not impressed with the {query}. Expected better.",
                        f"Having issues with my {query}. Customer service is terrible.",
                        f"Disappointed with the {query}. Don't recommend it."
                    ]
                }
                
                text = random.choice(text_templates[sentiment])
                engagement = random.randint(1, 100)
                
                posts.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "platform": platform,
                    "text": text,
                    "engagement": engagement,
                    "implied_sentiment": sentiment
                })
        
        return pd.DataFrame(posts)
    
    def collect_reviews_data(self, product: str, source: str = "api") -> pd.DataFrame:
        """
        Collect product reviews data
        
        Args:
            product: Product name or ID
            source: Source of reviews (api, scrape, etc.)
            
        Returns:
            DataFrame with collected reviews
        """
        logger.info(f"Collecting reviews for {product} from {source}")
        
        # In a real application, this would call an API or scrape data
        # For now, we'll return mock data
        
        # Generate mock reviews
        import random
        import numpy as np
        
        reviews = []
        for _ in range(100):  # 100 mock reviews
            rating = random.randint(1, 5)
            
            # Make text sentiment match rating
            if rating >= 4:
                sentiment = "positive"
                text_templates = [
                    f"Great {product}! Exactly what I needed.",
                    f"Love this {product}. Highly recommend it!",
                    f"The {product} is excellent. Works as advertised!"
                ]
            elif rating == 3:
                sentiment = "neutral"
                text_templates = [
                    f"The {product} is okay. Nothing special.",
                    f"{product} works, but has some issues.",
                    f"Average {product}. Gets the job done."
                ]
            else:
                sentiment = "negative"
                text_templates = [
                    f"Disappointed with this {product}. Wouldn't recommend.",
                    f"The {product} doesn't work as expected.",
                    f"Had issues with the {product}. Waste of money."
                ]
            
            text = random.choice(text_templates)
            date = (datetime.now() - timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d")
            
            reviews.append({
                "date": date,
                "product": product,
                "rating": rating,
                "text": text,
                "source": source,
                "implied_sentiment": sentiment
            })
        
        return pd.DataFrame(reviews)
    
    def collect_customer_service_data(self, days: int = 90) -> pd.DataFrame:
        """
        Collect customer service data
        
        Args:
            days: Number of days to look back
            
        Returns:
            DataFrame with customer service data
        """
        logger.info(f"Collecting customer service data for the past {days} days")
        
        # In a real application, this would query a database or API
        # For now, we'll return mock data
        
        # Generate dates for the past X days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Generate daily data
        dates = []
        current_date = start_date
        while current_date <= end_date:
            dates.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)
        
        # Generate random metrics with a slightly improving trend
        import random
        import numpy as np
        
        # Create base metrics with upward trends
        n = len(dates)
        tickets = [random.randint(80, 120) for _ in range(n)]
        resolution_rate = list(np.linspace(0.7, 0.85, n) + np.random.normal(0, 0.03, n))
        resolution_rate = [min(max(x, 0), 1) for x in resolution_rate]  # Clip to 0-1
        avg_response_time = list(np.linspace(5.0, 3.5, n) + np.random.normal(0, 0.2, n))
        avg_response_time = [max(x, 1.0) for x in avg_response_time]  # Ensure positive
        customer_satisfaction = list(np.linspace(3.5, 4.2, n) + np.random.normal(0, 0.15, n))
        customer_satisfaction = [min(max(x, 1), 5) for x in customer_satisfaction]  # Clip to 1-5
        
        # Combine into DataFrame
        data = []
        for i, date in enumerate(dates):
            data.append({
                "date": date,
                "tickets": tickets[i],
                "resolution_rate": round(resolution_rate[i], 2),
                "avg_response_time": round(avg_response_time[i], 1),
                "customer_satisfaction": round(customer_satisfaction[i], 1)
            })
        
        return pd.DataFrame(data)