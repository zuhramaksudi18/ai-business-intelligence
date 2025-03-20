FROM python:3.9-slim

WORKDIR /app

# Install Java for Spark
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the data pipeline code
COPY . .

# Set up a volume for data persistence
VOLUME /app/data

# Run the data pipeline
CMD ["python", "main.py", "--output", "data"]