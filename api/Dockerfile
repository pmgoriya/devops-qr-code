# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the API code into the container
COPY . /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    rm -rf /var/lib/apt/lists/*

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000 (the default port FastAPI uses)
EXPOSE 8000

# Command to run the API server using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

