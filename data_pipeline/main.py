#!/usr/bin/env python3
import argparse
import logging
import os
import sys
from datetime import datetime

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("data_pipeline")

# Add parent directory to path to enable imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scrapers.social_media_scraper import SocialMediaScraper
from spark.data_transformation import DataTransformer

def main():
    """Main entry point for the data pipeline"""
    parser = argparse.ArgumentParser(description='Run the data pipeline')
    parser.add_argument('--source', choices=['social_media', 'reviews', 'all'], 
                        default='all', help='Data source to collect')
    parser.add_argument('--transform', action='store_true', 
                        help='Run Spark transformations')
    parser.add_argument('--days', type=int, default=7, 
                        help='Number of days to look back')
    parser.add_argument('--output', type=str, default='data', 
                        help='Output directory')
    
    args = parser.parse_args()
    
    # Create output directory if it doesn't exist
    os.makedirs(args.output, exist_ok=True)
    
    # Timestamp for filenames
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Collect data
    if args.source in ['social_media', 'all']:
        logger.info("Starting social media data collection")
        try:
            scraper = SocialMediaScraper()
            
            # Scrape Twitter (simulated)
            twitter_data = scraper.scrape_twitter(days=args.days)
            twitter_file = os.path.join(args.output, f"twitter_data_{timestamp}.csv")
            twitter_data.to_csv(twitter_file, index=False)
            logger.info(f"Saved Twitter data to {twitter_file}")
            
            # Scrape Reddit (simulated)
            reddit_data = scraper.scrape_reddit(days=args.days)
            reddit_file = os.path.join(args.output, f"reddit_data_{timestamp}.csv")
            reddit_data.to_csv(reddit_file, index=False)
            logger.info(f"Saved Reddit data to {reddit_file}")
        except Exception as e:
            logger.error(f"Error in social media data collection: {str(e)}")
    
    if args.source in ['reviews', 'all']:
        logger.info("Starting reviews data collection")
        try:
            scraper = SocialMediaScraper()
            
            # Scrape product reviews (simulated)
            reviews_data = scraper.scrape_reviews(days=args.days)
            reviews_file = os.path.join(args.output, f"reviews_data_{timestamp}.csv")
            reviews_data.to_csv(reviews_file, index=False)
            logger.info(f"Saved reviews data to {reviews_file}")
        except Exception as e:
            logger.error(f"Error in reviews data collection: {str(e)}")
    
    # Run transformations if requested
    if args.transform:
        logger.info("Starting data transformations")
        try:
            transformer = DataTransformer()
            
            # Find the latest files
            latest_files = {}
            for file in os.listdir(args.output):
                for source in ['twitter', 'reddit', 'reviews']:
                    if file.startswith(f"{source}_data_") and file.endswith(".csv"):
                        if source not in latest_files or file > latest_files[source]:
                            latest_files[source] = file
            
            # Combine data sources
            combined_data = transformer.combine_data_sources([
                os.path.join(args.output, file) for file in latest_files.values()
            ])
            
            # Transform and enrich data
            enriched_data = transformer.enrich_data(combined_data)
            
            # Save transformed data
            transformed_file = os.path.join(args.output, f"transformed_data_{timestamp}.csv")
            enriched_data.to_csv(transformed_file, index=False)
            logger.info(f"Saved transformed data to {transformed_file}")
        except Exception as e:
            logger.error(f"Error in data transformation: {str(e)}")
    
    logger.info("Data pipeline completed successfully")

if __name__ == "__main__":
    main()