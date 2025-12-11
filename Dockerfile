# Use an official Python runtime as a parent image
FROM python:3.13-slim
# Set the working directory inside the container
WORKDIR /app
# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copy the rest of the application’s code
COPY ./src .
# Expose the port the app runs on
EXPOSE 5000
# Define the command to run your app
CMD ["python", "app.py"]