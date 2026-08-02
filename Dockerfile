# Mustapha Blida AI - Docker Image
# ==================================
FROM python:3.11-slim

LABEL maintainer="https://x.com/mouse0000000"
LABEL app="Mustapha Blida AI"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    libgl1 \
    libglib2.0-0 \
    wget \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create necessary directories
RUN mkdir -p storage/output resource/songs resource/fonts

# Expose ports
EXPOSE 8080 8501

# Default command (override in docker-compose)
CMD ["python", "main.py"]
