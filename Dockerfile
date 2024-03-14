# Use the official Python image for Windows as a base
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /

# Copy the Flask application files into the container
COPY /flask_server .
COPY requirements.txt .

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Line 15 to 19 are for installnig OBDC driver dependencies
ENV ACCEPT_EULA=Y
RUN apt-get update -y && apt-get update \
  && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
  && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends --allow-unauthenticated msodbcsql17 mssql-tools \
  && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
  && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

# Expose the port on which the Gunicorn server will run
EXPOSE 5000

# Command to run the Flask application using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]
