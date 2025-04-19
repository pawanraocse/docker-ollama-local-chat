# Docker Ollama Local Chat

This project demonstrates how to build a **local chat application** powered by Ollama models using Docker. The chat app interacts with powerful AI models (like Gemma) through Docker containers to enable seamless and interactive conversations. This project can serve as a base for developing AI-powered chatbots or conversational agents for various applications.

## Table of Contents

- [Docker Ollama Local Chat](#docker-ollama-local-chat)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Technologies Used](#technologies-used)
  - [Setup Instructions](#setup-instructions)
    - [1. Clone the Repository](#1-clone-the-repository)
    - [2. Build and Run the Containers](#2-build-and-run-the-containers)
    - [3. Install Python Dependencies](#3-install-python-dependencies)
    - [4. Start the Chat](#4-start-the-chat)
    - [5. Interact with the Chatbot](#5-interact-with-the-chatbot)
  - [Usage](#usage)
    - [Example:](#example)
  - [Contributing](#contributing)

## Overview

This project involves setting up **Ollama models** in Docker containers to run a local chat application. The system uses a Python app to communicate with the Ollama container via HTTP, sending a prompt and receiving responses from the chosen AI model.

**Key Features**:

- AI-powered chat using Ollama's Gemma 3:1b model.
- Easy setup with Docker Compose.
- Streamlined code for interactive conversations with the AI model.
- Dockerized environment for isolation and easy reproducibility.

## Features

- **Ollama Integration**: Uses Ollama's containerized models to provide conversational AI capabilities.
- **Interactive Chat**: Sends prompts to the AI model and displays the generated responses.
- **Dockerized Environment**: The entire application, including Ollama and the Python chat application, runs inside Docker containers.
- **Easy to Extend**: You can easily add new models or modify the Python app to change functionality.

## Technologies Used

- **Docker**: Containerization for the entire setup.
- **Ollama**: For the AI model that powers the chatbot (Gemma 3:1b).
- **Python**: For the backend application that interacts with Ollama.
- **Docker Compose**: To manage multi-container Docker applications.
- **Requests Library**: For HTTP requests to communicate with the Ollama container.

## Setup Instructions

Follow these steps to get the project up and running:

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/pawanraocse/docker-ollama-local-chat.git
cd docker-ollama-local-chat
```

### 2. Build and Run the Containers

Make sure you have Docker and Docker Compose installed on your system.

Run the following commands to stop any previously running containers, build the Docker images, and start the containers:

```bash
python restart.py  # This will stop old containers, build new ones, and pull models
```

### 3. Install Python Dependencies

Inside the `python-app` container, the required Python libraries are already listed. However, if you want to run the app locally or modify it, you can install dependencies as follows:

```bash
docker-compose run python-app pip install -r requirements.txt
```

### 4. Start the Chat

Once the containers are running, open a terminal and run the Python application:

```bash
docker-compose run python-app
```

### 5. Interact with the Chatbot

The application will ask you for an input. Type a message to interact with the chatbot. Type **'exit'** to quit the conversation.

## Usage

The Python app interacts with the Ollama model container to send text prompts to the AI model and retrieve responses.

### Example:

```bash
Chat with Gemma! Type 'exit' to quit.

You: Hello!
Gemma: Hi there! How can I assist you today?
```

## Contributing

We welcome contributions! If you would like to contribute to the project, please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-name`)
5. Create a new Pull Request
