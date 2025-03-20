@echo off
echo Checking for Docker...
where docker >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Docker is required to run this application.
    echo Please install Docker Desktop first.
    exit /b 1
)

echo Creating data directory if it doesn't exist...
if not exist data mkdir data

echo Building and starting services...
docker-compose up --build -d

echo Services are starting up...
echo - Frontend will be available at: http://localhost:3000
echo - Backend API will be available at: http://localhost:8000

echo To view logs, run: docker-compose logs -f
echo To stop the services, run: docker-compose down