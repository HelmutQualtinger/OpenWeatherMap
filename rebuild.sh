#!/bin/bash

# Stop and remove the existing container
docker stop openweathermap
docker rm openweathermap

# Build the new container
docker build -t openweathermap .

# Run the new container
docker run -d -it --restart unless-stopped --name openweathermap openweathermap
