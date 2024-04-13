#!/bin/bash

# Check if Docker is installed and command is available
if ! command -v docker &> /dev/null; then
    echo "Docker is not installed. Please install Docker first."
    exit 1
fi

# Build the image
echo "Building Docker image..."
if docker build -t oauth_image .; then
    echo "Image built successfully."

    # Check if a container named "oauth_container" already exists
    existing_container=$(docker ps -aq -f name=^/oauth_container$)
    if [[ -n "$existing_container" ]]; then
        echo "Container already exists. Stopping and removing it..."
        docker stop oauth_container && docker rm oauth_container
    fi

    echo "Running new container..."
    # Run the Docker container in detached mode
    if docker run -p 443:443 -d --name oauth_container -v $(pwd)/ssl:/ssl oauth_image; then
        echo "Container started. Following logs now:"
        # Follow the logs of the newly started container
        docker logs -f oauth_container
    else
        echo "Failed to start container."
    fi
else
    echo "Image build failed."
fi
