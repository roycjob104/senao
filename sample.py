#!/usr/bin/env python3
import requests

# Define the base URL where your FastAPI application is running
base_url = "http://localhost"

# Sample user data
user_data = {
    "username": "john_doe",
    "password": "Password123"
}

# Send POST request to create_account endpoint
response = requests.post(f"{base_url}/create-account/", json=user_data)

# Print the response
print(response.json())