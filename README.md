# Chat Application

## Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Technologies Used](#technologies-used)
4. [Installation and Usage](#installation-and-usage)
   - [Setup and Running](#setup-and-running)
   - [Docker Setup](#docker-setup)
5. [Code Explanation](#code-explanation)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)



## Overview

The Chat Application project is a modern chat solution developed using FastAPI and MongoDB. This application supports a range of features designed to facilitate effective communication:

- **Group and Private Chats**: Users can engage in group conversations and private messages.
- **User Authentication**: Secure authentication is provided through JWT tokens, ensuring that user sessions are protected and managed effectively.
- **Chat History Storage**: All chat interactions are stored in MongoDB, allowing users to review past conversations.
- **Real-Time Communication**: The application supports real-time messaging through WebSocket connections managed in `sockets.py`.

The project is structured to follow best practices for maintainability and scalability. The core application logic resides in the' app' directory, including configuration files, middleware, models, API routes, and utility functions. Docker is utilized to containerize the application, simplifying deployment and ensuring consistent environments across different systems.

With this setup, developers and users can easily deploy and run the chat application in a local or production environment, taking advantage of both FastAPI's high performance and MongoDB's flexibility.


## Features

The Chat Application includes the following key features:

- **Real-Time Messaging**: Leverage WebSocket connections to provide real-time communication for both group and private chats.
- **Group Chats**: Create and manage chat groups where multiple users can participate in discussions.
- **Private Chats**: Send and receive direct messages between users for one-on-one conversations.
- **User Authentication**: Secure login and registration processes with JSON Web Tokens (JWT) to ensure user data and sessions are protected.
- **Chat History**: Persistent storage of chat messages in MongoDB, enabling users to view their chat history.
- **Rate Limiting**: Middleware for controlling the rate of incoming requests, protecting the application from abuse and ensuring fair use.
- **Configurable Logging**: Advanced logging configuration to monitor application activity and troubleshoot issues effectively.
- **Scalable Architecture**: Designed to handle growth with a modular codebase and containerization using Docker.

These features combine to deliver a robust and scalable chat solution suitable for various use cases, from personal messaging to group discussions and beyond.

## Technologies Used

The Chat Application is built using a combination of modern technologies to ensure performance, scalability, and maintainability:

- **FastAPI**: A high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints. It enables fast development and efficient performance for handling HTTP requests and WebSocket connections.
- **MongoDB**: A NoSQL database used for storing chat messages and user data. Its flexible schema design allows for scalable and high-performance data storage.
- **Uvicorn**: A lightning-fast ASGI server for running the FastAPI application, supporting asynchronous capabilities and efficient handling of concurrent requests.
- **Docker**: A platform for containerizing the application, ensuring consistent environments across development, testing, and production. Docker Compose is used for managing multi-container setups.
- **JWT (JSON Web Tokens)**: A compact and self-contained way to securely transmit information between parties as a JSON object. Used for user authentication and session management.
- **pytest**: A testing framework for writing simple and scalable test cases to ensure the application functions as expected.
- **virtualenv**: A tool for creating isolated Python environments, allowing for dependency management and avoiding conflicts between project requirements.

These technologies work together to create a robust and efficient chat application with real-time capabilities and secure user interactions.

## Project Structure

The project structure is as follows:

Chatapp/
├── venv/ # Virtual environment for the project
├── logs/ # Log files
├── app/
│ ├── pycache/ # Python cache files
│ ├── config/ # Configuration files
│ │ ├── auth.py # Authentication and token functions
│ │ ├── config.py # Project configuration settings
│ │ └── logs.py # Logging configuration
│ ├── middlewares/ # Middleware components
│ │ └── request_limit.py # Request rate limiting middleware
│ ├── models/ # Data models
│ ├── routes/ # API routes
│ ├── schemas/ # Data schemas
│ ├── services/ # Service components
│ ├── utils/ # Utility functions
│ ├── init.py # Initialization file for the module
│ ├── main.py # Main FastAPI application file
│ └── sockets.py # Socket management
├── docker-compose.yml # Docker Compose configuration
├── Dockerfile # Dockerfile for building the Docker image
├── entrypoint.sh # Docker entrypoint script
├── readme.md # This README file
└── requirements.txt # Python dependencies

## Installation and Usage

Follow these steps to set up and run the Chat Application on your local machine:

### Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/erfanalimohammadi/chatapp.git
cd chat-app
```

### Setup and Running

1. ###Set up the Virtual Environment:

Ensure you have `virtualenv` installed. If not, install it using:
   ```bash
   python -m pip install virtualenv
   ```
Create a virtual environment in the venv/ directory:
  ```bash
  python -m venv venv
  ```
Activate the virtual environment:
  ```bash
    venv\Scripts\activate
  ```
2. ###Install Dependencies:
Once the virtual environment is activated, install the required Python packages:
  ```bash
  pip install -r requirements.txt
  ```
Run the Application:
Start the FastAPI application by running:
  ```bash
  uvicorn app.main:app --reload
  ```
The application will be available at **http://127.0.0.1:8000.**

***Run Tests:***

To run tests, ensure that the virtual environment is activated and executed:
  ```bash
  pytest
  ```
Ensure that your test database configuration is properly set up in ***config.py***

***Docker Setup:***

To build and run the application using Docker, ensure Docker and Docker Compose are installed. Then:

Build the Docker image:
  ```bash
  docker-compose build
  ```
Start the application in a Docker container:
```bash
  docker-compose up
  ```
The application will be available at ***http://127.0.0.1:8000*** inside the container.

3. ###Logging and Configuration:

Logs are stored in the logs/ directory. Configuration settings can be adjusted in config/config.py.

For additional information or troubleshooting, refer to the documentation or seek support as needed.

This detailed README file includes a complete setup guide, instructions for running the application, and information about Docker usage. It should provide clear instructions for getting the project up and running.


## Code Explanation

This section provides an overview of the main components and files in the codebase, explaining their purposes and functionalities.

### Directory Structure

#### `venv/`
- **Description:** Contains the virtual environment for the project. This directory includes all the Python dependencies required for the project to run.

#### `logs/`
- **Description:** Directory for storing application log files. These logs help track the application's runtime behavior and are crucial for debugging and monitoring.

#### `app/`
- **Description:** Main directory containing the application’s code. The subdirectories and files within `app/` are organized as follows:

  - **`config/`**
    - **`auth.py`**: Implements authentication-related functions, including JWT token generation and validation.
    - **`config.py`**: Contains main configuration settings for the project, such as JWT secrets, database configurations, and other application-wide settings.
    - **`logs.py`**: Configures logging for the application, setting up how and where logs are recorded.

  - **`middlewares/`**
    - **`request_limit.py`**: Provides middleware to limit the rate of incoming requests. This helps prevent abuse and ensures fair usage of the API.

  - **`models/`**
    - **Description:** Contains data models used in the application. These models define the structure of the data stored in the database.

  - **`routes/`**
    - **Description:** Defines the API routes of the application. Each file in this directory corresponds to a set of related API endpoints.

  - **`schemas/`**
    - **Description:** Contains data schemas used for validating and serializing request and response data. Schemas ensure data integrity and proper format.

  - **`services/`**
    - **Description:** Implements business logic and service layer components. Services handle the core functionality of the application and interact with data models.

  - **`utils/`**
    - **Description:** Contains utility functions that provide common functionalities used across different parts of the application.

  - **`__init__.py`**
    - **Description:** Initialization file that makes the `app` directory a Python package. It allows importing modules from `app/` as a package.

  - **`main.py`**
    - **Description:** The entry point of the FastAPI application. This file initializes and runs the FastAPI app, configuring routes and middleware.

  - **`sockets.py`**
    - **Description:** Manages WebSocket connections and real-time communication features. This file handles socket-based interactions such as live chat updates.

#### `docker-compose.yml`
- **Description:** Docker Compose configuration file. It defines services, networks, and volumes needed for multi-container Docker applications. This file helps in setting up and running the application in a Docker environment.

#### `Dockerfile`
- **Description:** Defines how to build the Docker image for the application. It includes instructions for setting up the environment, installing dependencies, and configuring the application inside a Docker container.

#### `entrypoint.sh`
- **Description:** Entrypoint script for Docker. It initializes the container environment, running necessary setup commands before starting the application.

#### `readme.md`
- **Description:** This file, which provides an overview, installation instructions, and usage information for the project.

#### `requirements.txt`
- **Description:** Lists the Python dependencies required for the project. This file is used by `pip` to install all necessary packages into the virtual environment.

### Summary

This directory and file structure is designed to keep the project organized and modular, making it easier to manage and scale. Each component is responsible for a specific part of the application, from handling configuration and logging to managing routes and services.

## Contributing

We welcome contributions from the community to enhance and improve this project. If you are interested in contributing, please follow these guidelines to ensure a smooth collaboration process.

### How to Contribute

1. **Fork the Repository**
   - Start by forking the repository to your own GitHub account. This allows you to freely make changes without affecting the original codebase.

2. **Clone Your Fork**
   - Clone your forked repository to your local machine:
     ```bash
     git clone https://github.com/your-username/chatapp.git
     ```
   - Navigate to the project directory:
     ```bash
     cd chatapp
     ```

3. **Create a Branch**
   - Create a new branch for your changes. Use a descriptive name for the branch:
     ```bash
     git checkout -b feature/your-feature-name
     ```

4. **Make Changes**
   - Make your changes or additions to the code. Ensure that your code adheres to the project's coding standards and guidelines.

5. **Test Your Changes**
   - Test your changes thoroughly to ensure they work as expected and do not introduce any new issues.

6. **Commit Your Changes**
   - Add and commit your changes with a descriptive commit message:
     ```bash
     git add .
     git commit -m "Add feature/bugfix description"
     ```

7. **Push Your Changes**
   - Push your branch to your forked repository:
     ```bash
     git push origin feature/your-feature-name
     ```

8. **Create a Pull Request**
   - Navigate to the original repository on GitHub and open a new pull request. Provide a clear description of the changes and the reasoning behind them.

### Code of Conduct

Please adhere to the following code of conduct to ensure a positive and productive environment for all contributors:

- **Respect:** Treat others with respect and kindness. Constructive criticism is encouraged, but personal attacks or offensive behavior is not tolerated.
- **Collaboration:** Collaborate effectively with others. Be open to feedback and be willing to revise your contributions based on community input.
- **Quality:** Aim to write high-quality code that is well-documented and tested. Follow the project's coding standards and best practices.

### Reporting Issues

If you encounter any bugs or issues, please report them by opening an issue on GitHub. Provide as much detail as possible to help us understand and address the problem.

### Acknowledgments

Thank you for your interest in contributing to this project! Your contributions help make the project better for everyone. We appreciate your support and look forward to working with you.

For any questions or further assistance, feel free to contact the project maintainers.





