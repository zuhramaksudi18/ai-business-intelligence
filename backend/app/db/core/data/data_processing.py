import pandas as pd
import numpy as np
from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

class DataProcessor:
    """
    Class to process collected data for analysis
    """
    
    def __init__(self):
        """
        Initialize the data processor
        """
        pass
    
    def prepare_sentiment_data(self, df: pd.DataFrame, 
                              text_column: str = 'text',
                              date_column: str = 'date') -> pd.DataFrame:
        """
        Prepare data for sentiment analysis
        
        Args:
            df: DataFrame with raw data
            text_column: Column containing text to analyze
            date_column: Column containing dates
            
        Returns:
            Processed DataFrame ready for sentiment analysis
        """
        logger.info("Preparing data for sentiment analysis")
        
        # Make a copy to avoid modifying the original
        result_df = df.copy()
        
        # Ensure date column is datetime type
        if date_column in result_df.columns:
            result_df[date_column] = pd.to_datetime(result_df[date_column])
        
        # Basic text cleaning
        if text_column in result_df.columns:
            # Remove URLs
            result_df[text_column] = result_df[text_column].str.replace(
                r'http\S+', '', regex=True
            )
            
            # Remove special characters
            result_df[text_column] = result_df[text_column].str.replace(
                r'[^\w\s]', '', regex=True
            )
            
            # Convert to lowercase
            result_df[text_column] = result_df[text_column].str.lower()
        
        return result_df
    
    def prepare_time_series_data(self, df: pd.DataFrame,
                                date_column: str,
                                value_column: str,
                                frequency: str = 'D') -> pd.DataFrame:
        """
        Prepare data for time series analysis
        
        Args:
            df: DataFrame with raw data
            date_column: Column containing dates
            value_column: Column containing values to forecast
            frequency: Frequency for resampling ('D' for daily, 'W' for weekly, etc.)
            
        Returns:
            Processed DataFrame ready for time series forecasting
        """
        logger.info(f"Preparing time series data with {frequency} frequency")
        
        # Make a copy to avoid modifying the original
        result_df = df.copy()
        
        # Ensure date column is datetime type
        result_df[date_column] = pd.to_datetime(result_df[date_column])
        
        # Set date as index
        result_df = result_df.set_index(date_column)
        
        # Resample to specified frequency
        result_df = result_df[[value_column]].resample(frequency).mean()
        
        # Handle missing values with forward fill, then backward fill
        result_df = result_df.fillna(method='ffill').fillna(method='bfill')
        
        # Reset index to get date as a column again
        result_df = result_df.reset_index()
        
        return result_df
    
    def aggregate_metrics(self, dfs: List[pd.DataFrame], 
                         date_column: str = 'date') -> pd.DataFrame:
        """
        Aggregate metrics from multiple DataFrames
        
        Args:
            dfs: List of DataFrames to aggregate
            date_column: Column containing dates
            
        Returns:
            Aggregated DataFrame with combined metrics
        """
        logger.info(f"Aggregating metrics from {len(dfs)} DataFrames")
        
        if not dfs:
            return pd.DataFrame()
        
        # Ensure all DataFrames have the date column as datetime
        for i in range(len(dfs)):
            if date_column in dfs[i].columns:
                dfs[i][date_column] = pd.to_datetime(dfs[i][date_column])
        
        # Start with the first DataFrame
        result_df = dfs[0].copy()
        
        # Set date as index for easier merging
        result_df = result_df.set_index(date_column)
        
        # Merge with other DataFrames
        for i in range(1, len(dfs)):
            df = dfs[i].copy()
            if date_column in df.columns:
                df = df.set_index(date_column)
                
                # Get unique column names
                columns_to_merge = [col for col in df.columns if col not in result_df.columns]
                
                if columns_to_merge:
                    # Merge only unique columns
                    result_df = result_df.join(df[columns_to_merge], how='outer')
        
        # Handle missing values
        result_df = result_df.fillna(method='ffill').fillna(method='bfill')
        
        # Reset index to get date as a column again
        result_df = result_df.reset_index()
        
        return result_df