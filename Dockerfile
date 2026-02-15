# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .

# Expose port 8000 for FastAPI
EXPOSE 8000

# Run database initialization and start the app
CMD python database.py && uvicorn main:app --host 0.0.0.0 --port 8000
