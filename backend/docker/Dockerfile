# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY backend/requirements.txt /app

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Command to run your application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]