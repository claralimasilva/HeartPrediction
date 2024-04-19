# Heart Disease Prediction Project
## Overview
This project aims to predict the likelihood of heart disease in individuals using machine learning techniques. We have utilized the scikit-learn library to build our predictive models and incorporated MLOps practices with MLflow for experiment tracking and model management. The model is served using FastAPI and containerized with Docker for easy deployment and scalability.
## Dataset
The dataset used for this project contains various attributes that are considered significant in predicting heart disease. The attributes include:
- Age: Age of the individual
- Sex: Gender of the individual
- ChestPainType: Type of chest pain experienced (4 values)
- RestingBP: Resting blood pressure
- Cholesterol: Serum cholesterol
- FastingBS: Fasting blood sugar
- RestingECG: Resting electrocardiogram results
- MaxHR: Maximum heart rate achieved
- ExerciseAngina: Exercise-induced angina
- Oldpeak: ST depression induced by exercise relative to rest
- ST_Slope: The slope of the peak exercise ST segment
- HeartDisease: Output class (1: heart disease, 0: no heart disease)
## Project Structure
The project is structured as follows:
- data/: Directory containing the dataset and data-related scripts.
- models/: Directory where trained models are saved.
- notebooks/: Jupyter notebooks for exploratory data analysis and model prototyping.
- src/: Source code for the project, including model training and API code.
- Dockerfile: Dockerfile for building the container image of the FastAPI server.
- mlruns/: Directory where MLflow tracking information is stored.
- requirements.txt: A text file listing the project's dependencies.
## Model Training
We used scikit-learn to train a machine learning model on the dataset. The model training process is logged and managed using MLflow, which allows us to track experiments, compare model performance, and manage the model lifecycle.
## API
The trained model is served using FastAPI, which provides a high-performance, easy-to-use framework for building APIs. The API allows users to submit patient data and receive predictions on the likelihood of heart disease.
## Docker
The FastAPI server is containerized using Docker, ensuring that the API can be easily deployed and run in any environment. The Dockerfile contains all the necessary instructions to build the container image.
## Getting Started
To get started with this project, clone the repository and install the required dependencies:
bash
git clone <repository-url>
cd <repository-name>
pip install -r requirements.txt
To run the FastAPI server locally, execute:
bash
uvicorn src.main:app --reload
To build and run the Docker container, use:
bash
docker build -t heart-disease-prediction .
docker run -p 8000:8000 heart-disease-prediction
## Usage
Once the server is running, you can make requests to the API to get predictions. An example request might look like this:
bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "Age": 45,
  "Sex": "M",
  "ChestPainType": "ATA",
  "RestingBP": 120,
  "Cholesterol": 225,
  "FastingBS": 0,
  "RestingECG": "Normal",
  "MaxHR": 180,
  "ExerciseAngina": "N",
  "Oldpeak": 0.0,
  "ST_Slope": "Up"
}'
## Example
### Running Docker Container
[Running Docker.webm](https://github.com/claralimasilva/HeartPrediction/assets/111255062/88715e37-d971-4586-abe4-8cc9fd65e063)

### Request to post
[Request video.webm](https://github.com/claralimasilva/HeartPrediction/assets/111255062/698113a9-34f3-47e0-9f47-59b3fc961997)

## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.
## License
This project is licensed under the MIT License - see the LICENSE file for details.
