# AI-Powered Business Intelligence Platform

A comprehensive business intelligence platform that leverages AI to analyze customer engagement trends, perform sentiment analysis, and forecast demand patterns. The project combines NLP, time-series forecasting, and data visualization to provide actionable insights for business decision-making.

## Features

- **Customer Engagement Analysis**: Track and analyze customer interactions and engagement metrics
- **Sentiment Analysis**: Process customer reviews and social media mentions using NLP models
- **Time-Series Forecasting**: Predict demand cycles and peak engagement periods
- **Interactive Dashboard**: Visualize AI-driven insights through an intuitive React.js interface
- **Automated Data Pipeline**: Collect and process data using Scrapy and Apache Spark

## Tech Stack

### Backend

- FastAPI (Python)
- OpenAI GPT
- Hugging Face Transformers
- Prophet
- TensorFlow
- SQLAlchemy
- PostgreSQL

### Frontend

- React.js
- Chart.js
- Material-UI

### Data Pipeline

- Scrapy
- Apache Spark
- Pandas

## Quick Start

### Using Docker (Recommended)

1. Make sure Docker and Docker Compose are installed on your system.

2. Clone the repository:

```bash
git clone https://github.com/your-username/ai-business-intelligence.git
cd ai-business-intelligence

Create a .env file based on the example:

bashCopycp .env.example .env
# Edit .env with your API keys

Run the application:

bashCopy# On Linux/Mac
./run.sh

# On Windows
run.bat

Access the services:

Frontend Dashboard: http://localhost:3000
Backend API: http://localhost:8000
API Docs: http://localhost:8000/docs



Manual Setup (Development)
Backend Setup

Set up a Python virtual environment:

bashCopycd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Run the backend server:

bashCopyuvicorn app.main:app --reload
Frontend Setup

Install dependencies:

bashCopycd frontend
npm install

Run the development server:

bashCopynpm start
Data Pipeline Setup

Set up a Python virtual environment:

bashCopycd data_pipeline
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Run the data pipeline:

bashCopypython main.py --source all --transform
Project Structure

backend/: FastAPI application with AI models

app/: Main application code

api/: API routes and services
core/: AI models and data processing
db/: Database models and configuration




frontend/: React.js dashboard

src/: Source code

components/: Reusable UI components
pages/: Main application pages
services/: API communication




data_pipeline/: Data collection and processing

scrapers/: Social media and reviews scrapers
spark/: Data transformation using Apache Spark



Features

Sentiment Analysis: Analyze text sentiment using Hugging Face Transformers and OpenAI models
Time Series Forecasting: Predict future trends with Prophet and LSTM models
Interactive Dashboard: Visualize business intelligence data in real-time
Automated Data Collection: Gather data from social media and review platforms
Scalable Architecture: Containerized services for easy deployment and scaling

API Documentation
The backend API provides endpoints for:

/api/sentiment/analyze: Analyze sentiment of a text
/api/sentiment/batch: Analyze sentiment of multiple texts
/api/forecast/train: Train a time series forecasting model
/api/forecast/predict: Generate forecasts
/api/dashboard/metrics: Get dashboard metrics

Complete API documentation is available at http://localhost:8000/docs when the application is running.
Contributing

Fork the repository
Create your feature branch (git checkout -b feature/amazing-feature)
Commit your changes (git commit -m 'Add some amazing feature')
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
```
