# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory in the container (in this case .root)
WORKDIR /

# Copy the main.py file and other application files into the container
COPY flask_server/ .

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install ODBC Driver Dependencies:
RUN apt-get update && apt-get install -y unixodbc unixodbc-dev

# Expose the port on which the Flask application will run
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "main.py"]
