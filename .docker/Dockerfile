# Use an official Python runtime as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file to the container
# COPY requirements.txt .

# Install the required dependencies
# RUN pip install --no-cache-dir -r requirements.txt

# Install dependencies manual
RUN pip install Django
RUN pip install python-dotenv
RUN pip install djangorestframework
RUN pip install pyresparser
RUN pip install nltk

# Copy the application code to the container
COPY . .

# Set the environment variable for running the application
ENV PYTHONUNBUFFERED 1

# Expose the port on which the application will run
EXPOSE 7000

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:7000"]
