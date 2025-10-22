# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . .

# Install dependencies (pytest in this case)
RUN pip install --no-cache-dir pytest

# Command to run tests (optional default)
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]
