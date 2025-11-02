# Base image
FROM python:3.11-slim

# Install OS-level build dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg-dev \
    zlib1g-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt /app/requirements.txt

# Upgrade pip
RUN python -m pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the project
COPY . /app

# Expose port
EXPOSE 8000

# Default command using gunicorn with uvicorn worker
CMD ["gunicorn", "app.main:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000", "--timeout", "180", "--workers", "2"]

