#!/bin/bash

# Make sure Docker and Docker Compose are installed
if ! command -v docker &> /dev/null || ! command -v docker-compose &> /dev/null
then
    echo "Error: Docker and Docker Compose are required to run this application."
    echo "Please install them first."
    exit 1
fi

# Create data directory if it doesn't exist
mkdir -p data

# Build and start the services
echo "Building and starting services..."
docker-compose up --build -d

echo "Services are starting up..."
echo "- Frontend will be available at: http://localhost:3000"
echo "- Backend API will be available at: http://localhost:8000"

echo "To view logs, run: docker-compose logs -f"
echo "To stop the services, run: docker-compose down"