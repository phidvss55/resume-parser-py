# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

RUN apt-get update && apt-get install -y python3-venv

# Create a virtual environment
RUN python3 -m venv env

RUN source env/bin/activate

# Set the environment variable for the virtual environment
ENV PATH="/app/env/bin:$PATH"

# Install dependencies manual
RUN pip install Django
RUN pip install python-dotenv
RUN pip install djangorestframework
RUN pip install pyresparser
RUN pip install nltk

# Setup NLTK stopwords resources
RUN python3 -m nltk.downloader stopwords

# Copy the application code to the container
COPY . .

# Set the environment variable for running the application
ENV PYTHONUNBUFFERED 1

WORKDIR /app/resume_parser

# Expose the port on which the application will run
EXPOSE 7000

# Start the application
CMD ["python3", "manage.py", "runserver", "localhost:7000"]
