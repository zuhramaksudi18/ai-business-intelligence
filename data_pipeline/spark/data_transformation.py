import pandas as pd
import numpy as np
import logging
from typing import List, Dict, Any, Optional
import os
from datetime import datetime, timedelta

logger = logging.getLogger(__name__)

class DataTransformer:
    """Class for transforming and processing collected data using Spark"""
    
    def __init__(self, spark_config: Dict[str, Any] = None):
        """
        Initialize the transformer
        
        Args:
            spark_config: Dictionary of Spark configuration options
        """
        self.spark_config = spark_config or {}
        logger.info("Initializing DataTransformer")
        
        # In a real application, this would initialize a Spark session
        # For now, we'll use pandas for simplicity
        logger.info("Using pandas for data processing (Spark simulation)")
    
    def combine_data_sources(self, file_paths: List[str]) -> pd.DataFrame:
        """
        Combine multiple data sources into a single DataFrame
        
        Args:
            file_paths: List of file paths to combine
            
        Returns:
            Combined DataFrame
        """
        logger.info(f"Combining {len(file_paths)} data sources")
        
        # Load all files
        dataframes = []
        for file_path in file_paths:
            try:
                if os.path.exists(file_path):
                    df = pd.read_csv(file_path)
                    logger.info(f"Loaded {file_path} with {len(df)} rows")
                    dataframes.append(df)
                else:
                    logger.warning(f"File not found: {file_path}")
            except Exception as e:
                logger.error(f"Error loading {file_path}: {str(e)}")
        
        if not dataframes:
            logger.warning("No data sources were loaded")
            return pd.DataFrame()
        
        # Ensure all DataFrames have consistent columns
        common_columns = ['timestamp', 'text', 'sentiment', 'platform']
        processed_dfs = []
        
        for df in dataframes:
            # Process each DataFrame based on its contents
            processed_df = pd.DataFrame()
            
            # Extract text field (could be in 'text', 'content', etc.)
            if 'text' in df.columns:
                processed_df['text'] = df['text']
            elif 'content' in df.columns:
                processed_df['text'] = df['content']
            elif 'title' in df.columns and 'content' in df.columns:
                # Combine title and content for reddit posts
                processed_df['text'] = df['title'] + " " + df['content']
            else:
                # Create empty text column
                processed_df['text'] = ""
            
            # Add timestamp
            if 'timestamp' in df.columns:
                processed_df['timestamp'] = pd.to_datetime(df['timestamp'])
            else:
                # Use current time as fallback
                processed_df['timestamp'] = datetime.now()
            
            # Add sentiment
            if 'sentiment' in df.columns:
                processed_df['sentiment'] = df['sentiment']
            else:
                # Use neutral as fallback
                processed_df['sentiment'] = "neutral"
            
            # Add platform
            if 'platform' in df.columns:
                processed_df['platform'] = df['platform']
            else:
                # Use unknown as fallback
                processed_df['platform'] = "unknown"
            
            # Add all other columns from original DataFrame
            for col in df.columns:
                if col not in processed_df.columns:
                    processed_df[col] = df[col]
            
            processed_dfs.append(processed_df)
        
        # Concatenate all processed DataFrames
        combined_df = pd.concat(processed_dfs, ignore_index=True)
        
        # Sort by timestamp
        combined_df = combined_df.sort_values('timestamp')
        
        logger.info(f"Combined DataFrame has {len(combined_df)} rows")
        
        return combined_df
    
    def enrich_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Enrich the data with additional features
        
        Args:
            df: Input DataFrame
            
        Returns:
            Enriched DataFrame
        """
        logger.info("Enriching data with additional features")
        
        # Make a copy to avoid modifying the original
        enriched_df = df.copy()
        
        # Ensure timestamp is datetime
        if 'timestamp' in enriched_df.columns:
            enriched_df['timestamp'] = pd.to_datetime(enriched_df['timestamp'])
            
            # Extract date components
            enriched_df['date'] = enriched_df['timestamp'].dt.date
            enriched_df['hour'] = enriched_df['timestamp'].dt.hour
            enriched_df['day_of_week'] = enriched_df['timestamp'].dt.dayofweek
            enriched_df['is_weekend'] = enriched_df['day_of_week'].isin([5, 6]).astype(int)
        
        # Create engagement score based on available metrics
        engagement_cols = ['likes', 'retweets', 'upvotes', 'comments', 'helpful_votes']
        engagement_cols = [col for col in engagement_cols if col in enriched_df.columns]
        
        if engagement_cols:
            # Normalize each metric to 0-1 range and sum them
            for col in engagement_cols:
                max_val = enriched_df[col].max()
                if max_val > 0:  # Avoid division by zero
                    enriched_df[f'{col}_norm'] = enriched_df[col] / max_val
                else:
                    enriched_df[f'{col}_norm'] = 0
            
            # Sum normalized metrics for engagement score
            norm_cols = [f'{col}_norm' for col in engagement_cols]
            enriched_df['engagement_score'] = enriched_df[norm_cols].sum(axis=1) / len(norm_cols)
            
            # Clean up temporary columns
            enriched_df = enriched_df.drop(columns=norm_cols)
        
        # Add sentiment score (numeric representation)
        sentiment_map = {
            'positive': 1.0,
            'neutral': 0.5,
            'negative': 0.0
        }
        
        if 'sentiment' in enriched_df.columns:
            enriched_df['sentiment_score'] = enriched_df['sentiment'].map(sentiment_map).fillna(0.5)
        
        # Add text length feature
        if 'text' in enriched_df.columns:
            enriched_df['text_length'] = enriched_df['text'].str.len()
        
        # Calculate moving averages for sentiment (if we have dates)
        if 'date' in enriched_df.columns and 'sentiment_score' in enriched_df.columns:
            # Group by date and calculate daily average sentiment
            daily_sentiment = enriched_df.groupby('date')['sentiment_score'].mean().reset_index()
            daily_sentiment = daily_sentiment.sort_values('date')
            
            # Calculate 3-day and 7-day moving averages
            daily_sentiment['sentiment_ma3'] = daily_sentiment['sentiment_score'].rolling(window=3, min_periods=1).mean()
            daily_sentiment['sentiment_ma7'] = daily_sentiment['sentiment_score'].rolling(window=7, min_periods=1).mean()
            
            # Merge back to the main DataFrame
            enriched_df = enriched_df.merge(
                daily_sentiment[['date', 'sentiment_ma3', 'sentiment_ma7']], 
                on='date', 
                how='left'
            )
        
        logger.info(f"Enriched DataFrame has {len(enriched_df)} rows and {len(enriched_df.columns)} columns")
        
        return enriched_df
    
    def calculate_metrics(self, df: pd.DataFrame) -> Dict[str, Any]:
        """
        Calculate key metrics from the data
        
        Args:
            df: Input DataFrame
            
        Returns:
            Dictionary of metrics
        """
        logger.info("Calculating key metrics")
        
        metrics = {}
        
        # Count by platform
        if 'platform' in df.columns:
            platform_counts = df['platform'].value_counts().to_dict()
            metrics['platform_counts'] = platform_counts
            metrics['total_records'] = len(df)
        
        # Sentiment distribution
        if 'sentiment' in df.columns:
            sentiment_counts = df['sentiment'].value_counts().to_dict()
            metrics['sentiment_distribution'] = sentiment_counts
            
            # Calculate percentage
            sentiment_pct = {}
            total = sum(sentiment_counts.values())
            for sentiment, count in sentiment_counts.items():
                sentiment_pct[sentiment] = round(100 * count / total, 2)
            
            metrics['sentiment_percentage'] = sentiment_pct
        
        # Engagement metrics
        if 'engagement_score' in df.columns:
            metrics['engagement_avg'] = df['engagement_score'].mean()
            metrics['engagement_median'] = df['engagement_score'].median()
            
            # Engagement by sentiment
            if 'sentiment' in df.columns:
                engagement_by_sentiment = df.groupby('sentiment')['engagement_score'].mean().to_dict()
                metrics['engagement_by_sentiment'] = engagement_by_sentiment
        
        # Time-based metrics
        if 'timestamp' in df.columns:
            df['timestamp'] = pd.to_datetime(df['timestamp'])
            
            # Posts by hour of day
            hour_counts = df['timestamp'].dt.hour.value_counts().sort_index().to_dict()
            metrics['hour_distribution'] = hour_counts
            
            # Posts by day of week
            day_of_week_counts = df['timestamp'].dt.dayofweek.value_counts().sort_index().to_dict()
            day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            metrics['day_of_week_distribution'] = {day_names[day]: count for day, count in day_of_week_counts.items()}
            
            # Activity over time (last 30 days)
            last_30_days = datetime.now() - timedelta(days=30)
            recent_df = df[df['timestamp'] >= last_30_days]
            daily_counts = recent_df.resample('D', on='timestamp').size().to_dict()
            metrics['daily_activity'] = {str(date.date()): count for date, count in daily_counts.items()}
        
        logger.info(f"Calculated {len(metrics)} metrics")
        
        return metrics