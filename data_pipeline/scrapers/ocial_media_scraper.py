import pandas as pd
import numpy as np
import logging
import random
from datetime import datetime, timedelta
from typing import List, Dict, Any

logger = logging.getLogger(__name__)

class SocialMediaScraper:
    """Class for scraping social media data"""
    
    def __init__(self, api_keys: Dict[str, str] = None):
        """
        Initialize the scraper
        
        Args:
            api_keys: Dictionary of API keys for different platforms
        """
        self.api_keys = api_keys or {}
    
    def scrape_twitter(self, query: str = "customer service", days: int = 7) -> pd.DataFrame:
        """
        Scrape Twitter data (simulated)
        
        Args:
            query: Search query
            days: Number of days to look back
            
        Returns:
            DataFrame with Twitter data
        """
        logger.info(f"Scraping Twitter for '{query}' over the past {days} days")
        
        # In a real application, this would use the Twitter API
        # For now, we'll generate mock data
        
        # Generate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Generate random tweets
        tweets = []
        current_date = start_date
        
        while current_date <= end_date:
            # Random number of tweets per day (5-20)
            num_tweets = random.randint(5, 20)
            
            for _ in range(num_tweets):
                # Generate random sentiment
                sentiment_type = random.choices(
                    ["positive", "neutral", "negative"], 
                    weights=[0.6, 0.3, 0.1], 
                    k=1
                )[0]
                
                # Templates based on sentiment
                templates = {
                    "positive": [
                        f"Loving the customer service at #CompanyX! Quick response to my {query} issue.",
                        f"Great experience with {query} today. #Recommended",
                        f"The {query} team is amazing! They solved my problem in minutes.",
                        f"Just had the best {query} experience. Kudos to the team!"
                    ],
                    "neutral": [
                        f"Anyone else having issues with {query} today?",
                        f"Looking for recommendations on {query} providers.",
                        f"Is the {query} service down? Can't seem to connect.",
                        f"Trying to figure out how to use the new {query} feature."
                    ],
                    "negative": [
                        f"Frustrated with the {query} team. Still waiting for a response after 2 days.",
                        f"Terrible experience with {query}. Will not recommend.",
                        f"Why is {query} so difficult to use? Bad design.",
                        f"Another day, another problem with {query}. #Disappointed"
                    ]
                }
                
                # Random tweet text from templates
                text = random.choice(templates[sentiment_type])
                
                # Random engagement metrics
                likes = random.randint(0, 100)
                retweets = random.randint(0, int(likes * 0.5))
                
                # Random time during the day
                tweet_time = current_date.replace(
                    hour=random.randint(0, 23),
                    minute=random.randint(0, 59),
                    second=random.randint(0, 59)
                )
                
                tweets.append({
                    "timestamp": tweet_time,
                    "text": text,
                    "likes": likes,
                    "retweets": retweets,
                    "sentiment": sentiment_type,
                    "platform": "twitter",
                    "query": query
                })
            
            # Move to next day
            current_date += timedelta(days=1)
        
        # Create DataFrame
        df = pd.DataFrame(tweets)
        
        # Sort by timestamp
        df = df.sort_values("timestamp")
        
        return df
    
    def scrape_reddit(self, subreddit: str = "all", query: str = "customer service", days: int = 7) -> pd.DataFrame:
        """
        Scrape Reddit data (simulated)
        
        Args:
            subreddit: Subreddit to scrape
            query: Search query
            days: Number of days to look back
            
        Returns:
            DataFrame with Reddit data
        """
        logger.info(f"Scraping Reddit '{subreddit}' for '{query}' over the past {days} days")
        
        # In a real application, this would use the Reddit API
        # For now, we'll generate mock data
        
        # Generate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Generate random posts
        posts = []
        current_date = start_date
        
        while current_date <= end_date:
            # Random number of posts per day (3-10)
            num_posts = random.randint(3, 10)
            
            for _ in range(num_posts):
                # Generate random sentiment
                sentiment_type = random.choices(
                    ["positive", "neutral", "negative"], 
                    weights=[0.4, 0.3, 0.3], 
                    k=1
                )[0]
                
                # Templates based on sentiment
                templates = {
                    "positive": [
                        f"[Positive] Had a great experience with {query} yesterday.",
                        f"Just wanted to share my positive experience with {query}.",
                        f"Is it just me or has {query} gotten much better lately?",
                        f"I think {query} is underrated. Here's why..."
                    ],
                    "neutral": [
                        f"[Question] How do I contact {query} support?",
                        f"Looking for advice on {query} options. Any suggestions?",
                        f"Has anyone tried the new {query} service?",
                        f"What's your experience with {query} been like?"
                    ],
                    "negative": [
                        f"[Rant] Frustrated with {query} customer service",
                        f"Is anyone else having issues with {query}?",
                        f"{query} quality has gone downhill. Here's my experience...",
                        f"Need to vent about {query} support. This is ridiculous."
                    ]
                }
                
                # Random post title from templates
                title = random.choice(templates[sentiment_type])
                
                # Generate post content
                content_templates = {
                    "positive": [
                        f"I've been using {query} for a while and I'm really impressed. The team is responsive and helpful.",
                        f"After trying several services, I can confidently say {query} is the best option. Here's my experience...",
                        f"Just wanted to give a shoutout to the {query} team for their excellent service.",
                        f"I was skeptical at first, but {query} exceeded my expectations. Highly recommend!"
                    ],
                    "neutral": [
                        f"I'm considering switching to {query} but wanted to hear some experiences first. Any thoughts?",
                        f"Can someone explain how {query} works? I'm new to this and could use some guidance.",
                        f"Trying to decide between {query} and their competitors. Pros and cons?",
                        f"What's the best way to use {query}? Looking for tips and tricks."
                    ],
                    "negative": [
                        f"I've been a customer for years, but {query} has really declined in quality. Here's why I'm switching...",
                        f"Spent hours trying to resolve an issue with {query} with no success. Avoid if possible.",
                        f"Warning: {query} charged me twice and refuses to issue a refund. Be careful!",
                        f"The new {query} update is terrible. Anyone else having issues?"
                    ]
                }
                
                content = random.choice(content_templates[sentiment_type])
                
                # Random engagement metrics
                upvotes = random.randint(-10, 100)
                comments = random.randint(0, 30)
                
                # Random time during the day
                post_time = current_date.replace(
                    hour=random.randint(0, 23),
                    minute=random.randint(0, 59),
                    second=random.randint(0, 59)
                )
                
                posts.append({
                    "timestamp": post_time,
                    "title": title,
                    "content": content,
                    "upvotes": upvotes,
                    "comments": comments,
                    "subreddit": subreddit,
                    "sentiment": sentiment_type,
                    "platform": "reddit",
                    "query": query
                })
            
            # Move to next day
            current_date += timedelta(days=1)
        
        # Create DataFrame
        df = pd.DataFrame(posts)
        
        # Sort by timestamp
        df = df.sort_values("timestamp")
        
        return df
    
    def scrape_reviews(self, product: str = "product", days: int = 30) -> pd.DataFrame:
        """
        Scrape product reviews (simulated)
        
        Args:
            product: Product name
            days: Number of days to look back
            
        Returns:
            DataFrame with review data
        """
        logger.info(f"Scraping reviews for '{product}' over the past {days} days")
        
        # In a real application, this would scrape a website or use an API
        # For now, we'll generate mock data
        
        # Generate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Generate random reviews
        reviews = []
        current_date = start_date
        
        # Set of reviewer names
        reviewer_names = [
            "JohnD", "Alice22", "ReviewGuru", "TechFan", "RegularUser",
            "NewCustomer", "LongTimeUser", "CriticalThinker", "HappyCustomer",
            "ValueShopper", "DetailPerson", "QuickReviewer", "ThoughtfulBuyer"
        ]
        
        while current_date <= end_date:
            # Random number of reviews per day (0-5)
            num_reviews = random.randint(0, 5)
            
            for _ in range(num_reviews):
                # Generate random rating (1-5 stars)
                rating = random.choices(
                    [1, 2, 3, 4, 5],
                    weights=[0.05, 0.10, 0.15, 0.30, 0.40],
                    k=1
                )[0]
                
                # Map rating to sentiment
                if rating >= 4:
                    sentiment = "positive"
                elif rating == 3:
                    sentiment = "neutral"
                else:
                    sentiment = "negative"
                
                # Templates based on sentiment
                templates = {
                    "positive": [
                        f"Excellent {product}! Exactly what I needed.",
                        f"Very satisfied with this {product}. Works perfectly.",
                        f"Best {product} I've used. Highly recommend!",
                        f"Great value for money. This {product} is amazing."
                    ],
                    "neutral": [
                        f"Decent {product}. Does the job but nothing special.",
                        f"The {product} is okay. Some pros and cons.",
                        f"Average {product}. Met my expectations but didn't exceed them.",
                        f"Not bad, not great. The {product} is just average."
                    ],
                    "negative": [
                        f"Disappointed with this {product}. Not worth the money.",
                        f"The {product} stopped working after a week. Poor quality.",
                        f"Avoid this {product}. Many better alternatives available.",
                        f"Returned the {product}. Didn't meet my expectations at all."
                    ]
                }
                
                # Random review text from templates
                text = random.choice(templates[sentiment])
                
                # Add more details to some reviews
                if random.random() < 0.7:
                    detail_templates = {
                        "positive": [
                            f" The customer service was also excellent.",
                            f" Delivery was fast and the packaging was secure.",
                            f" Setup was easy and intuitive.",
                            f" It's durable and well-designed."
                        ],
                        "neutral": [
                            f" The instructions could be clearer.",
                            f" It works, but the design could be improved.",
                            f" Good features but a bit overpriced.",
                            f" Customer service was average."
                        ],
                        "negative": [
                            f" Customer service was unhelpful when I reported the issue.",
                            f" The materials feel cheap and flimsy.",
                            f" Save your money and look elsewhere.",
                            f" The description was misleading."
                        ]
                    }
                    text += random.choice(detail_templates[sentiment])
                
                # Random reviewer name
                reviewer = random.choice(reviewer_names)
                
                # Random time during the day
                review_time = current_date.replace(
                    hour=random.randint(0, 23),
                    minute=random.randint(0, 59),
                    second=random.randint(0, 59)
                )
                
                # Random verified purchase status
                verified = random.random() < 0.8
                
                # Random helpfulness votes
                helpful_votes = random.randint(0, 20)
                
                reviews.append({
                    "timestamp": review_time,
                    "reviewer": reviewer,
                    "rating": rating,
                    "text": text,
                    "helpful_votes": helpful_votes,
                    "verified_purchase": verified,
                    "product": product,
                    "sentiment": sentiment,
                    "platform": "reviews"
                })
            
            # Move to next day
            current_date += timedelta(days=1)
        
        # Create DataFrame
        df = pd.DataFrame(reviews)
        
        # Sort by timestamp
        df = df.sort_values("timestamp")
        
        return df