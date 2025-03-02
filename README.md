# Overview

This project provides a FastAPI-based REST API for making hydrological model predictions. The API loads a pre-trained machine learning model stored as hydrological_model.pkl and serves it for predictions based on user-provided input data.

# Features

FastAPI Framework: A lightweight and high-performance API.

Machine Learning Integration: Uses a pre-trained hydrological model.

JSON Input & Output: Accepts numerical input and returns predictions in JSON format.

Docker & Uvicorn Support: Can be deployed efficiently.

# Installation & Setup

1. Clone the Repository

git clone https://github.com/KB2100/Hydrological_Model_API.git
cd Hydrological_Model_API

2. Install Dependencies

Create a virtual environment (optional but recommended) and install dependencies:

pip install virtualenv
virtualenv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install required Python packages:

pip install -r requirements.txt

# 3. Run the API Server

uvicorn app:app --host 0.0.0.0 --port 8000

The API will now be accessible at: http://127.0.0.1:8000

# API Endpoints

1. Health Check

Endpoint: /

Method: GET

Response:

{"message": "Hydrological Model API is running!"}

2. Prediction Endpoint

Endpoint: /predict/

Method: POST

Request Body: JSON

{"features": [0.5, 1.2, 3.4, 5.6]}

Response:

{"prediction": [4.56]}

# Deployment

# Using Docker

Build Docker Image:

docker build -t hydrological_model_api .

Run Container:

docker run -p 8000:8000 hydrological_model_api

# Using Ngrok (for Public Access)

Install Ngrok:

pip install pyngrok

Run Ngrok Tunnel:

ngrok http 8000

Get the public URL from the terminal and use it to access the API.

