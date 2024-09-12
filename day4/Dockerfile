FROM python:3.11.5

WORKDIR /app

COPY . /app

RUN pip install -r /app/requirements.txt

EXPOSE 5000

CMD fastapi dev main.py


# Use an official Python runtime as a base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any necessary Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 80 to allow outside access
EXPOSE 5000

# Define environment variable
# ENV MODEL_PATH="/app/model.pkl"

# Run the application (FastAPI in this example)
CMD ["fastapi", "dev", "main.py"]
