# Account and Password Management API

## Description
This project implements two RESTful HTTP APIs for creating and verifying an account and password.

## Setup
1. Clone this repository.
2. Build the Docker image: `docker build -t account-management-api .`
3. Run the Docker container: `docker run -d --name account-management-api -p 80:80 account-management-api`

## API Endpoints

### Create Account
- **Method:** POST
- **URL:** `/create-account/`
- **Input Payload:**
  ```json
  {
      "username": "string",
      "password": "string"
  }

- **Output Payload:**

  ```json
  {
      "success": "boolean",
      "reason": "string"
  }
- **EX:**

**Note:** Before running the script, make sure that the `requests` library is installed. If not, you can install it using the following command:
    ```bash
    pip3 install requests

## Sample Usage

To use the `create_account` function, you can follow this example:

    #!/usr/bin/python3
    import requests

    # Define the base URL where your FastAPI application is running
    base_url = "http://localhost"

    # Sample user data
    user_data = {
        "username": "Username",
        "password": "Password123"
    }

    # Send POST request to create_account endpoint
    response = requests.post(f"{base_url}/create-account/", json=user_data)
    
    # Print the response
    print(response.json())


### Verify Account
- **Method:** POST
- **URL:** `/verify-account/`
- **Input Payload:**
  ```json
  {
      "username": "string",
      "password": "string"
  }
- **Output Payload:**
  ```json
  {
      "success": "boolean",
      "reason": "string"
  }

- **EX:**
## Sample Usage

To use the `validate_account` function, you can follow this example: 

    #!/usr/bin/python3
    import requests

    # Define the base URL where your FastAPI application is running
    base_url = "http://localhost"

    # Sample user data
    user_data = {
        "username": "Username",
        "password": "Password123"
    }

    # Send POST request to validate_account endpoint
    response = requests.post(f"{base_url}/validate-account/", json=user_data)
    
    # Print the response
    print(response.json())

## Get image from docker
    $ docker pull roycjob104/account-management-api:latest


## Run the image
    $ docker run -d --name account-management-api -p 80:80 roycjob104/account-management-api:latest