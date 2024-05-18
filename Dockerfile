# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy everything from the current directory into the container
COPY . /app/

# Install Pipenv
RUN pip install pipenv

# Install dependencies from Pipfile
RUN pipenv install --deploy --system

# Define environment variables (if needed)
# ENV ENV_VARIABLE=value

# Run the Python script
CMD ["python", "exporter.py"]
