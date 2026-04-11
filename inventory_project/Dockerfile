# Use the official Python image from the Docker Hub
FROM python:3.11-alpine

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for PostgreSQL
RUN apk add --no-cache postgresql-libs postgresql-dev build-base

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 9000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]
COPY . .

# Expose the port the app runs on
EXPOSE 9000

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]