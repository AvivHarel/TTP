# Use an official Python runtime as a parent image
FROM python:3.7-slim

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install espeak
RUN apt-get update && apt-get install -y espeak

# Make port 80 available to the world outside this container
EXPOSE 80

# Run ttp.py when the container launches
CMD ["gunicorn", "ttp:app"]

