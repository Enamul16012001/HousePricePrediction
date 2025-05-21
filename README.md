# House Price Prediction

This project implements a linear regression model to predict house prices based on various features. The model is trained using the provided dataset and can be used to make predictions on new data.

## Table of Contents
- [Local Setup](#local-setup)
  - [Training the Model](#training-the-model)
- [Docker Setup](#docker-setup)
  - [Building the Docker Image](#building-the-docker-image)
  - [Running the Docker Container](#running-the-docker-container)
- [Using DockerHub Image](#using-dockerhub-image)
  - [Pulling the Image](#pulling-the-image)
  - [Running the Container](#running-the-container)


## Local Setup

Clone the repository:

```bash
git clone https://github.com/Enamul16012001/HousePricePrediction.git
```

Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Training the Model

To train the model, run the training script:

```bash
python train.py
```

## Docker Setup

### Building the Docker Image

Build the Docker image using the Dockerfile provided in the repository:

```bash
docker build -t house-price-prediction .
```

### Running the Docker Container

Run the Docker container with:

```bash
docker run -p 8000:8000 house-price-prediction
```

This will:
1. Start the container
2. Expose the prediction API on port 8000
3. Load the pre-trained model

## Using DockerHub Image

### Pulling the Image

Pull the pre-built Docker image from DockerHub:

```bash
docker pull enamulatiq/house-price-prediction:latest
```

### Running the Container

Run the container from the DockerHub image:

```bash
docker run -p 8000:8000 enamulatiq/house-price-prediction
```
