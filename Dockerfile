# Use an official Python runtime as a base image
FROM python:3

# Set the working directory in the container
WORKDIR /home/mrpau/Desktop/AWS/GoogleOauth2_Pau

# Copy only the requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Make port 80 available to the world outside this container
EXPOSE 80
EXPOSE 443

# Define the command to run the app
CMD ["python3", "app.py"]
