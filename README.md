# Diabetes Prediction with Flask and AWS Deployment

This project demonstrates the development and deployment of a machine learning model for predicting diabetes using the [Pima Indians Diabetes Dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database). The project involves data preprocessing, model training, creating a Flask API for predictions, containerizing the application with Docker, and deploying it on AWS.

## Technologies

* [x] **Python:** Core programming language used for data processing, model training, and Flask API development.
* [x] **Flask:** Lightweight web framework used to create the REST API for predictions.
* [x] **NumPy:** Library for numerical computations and data manipulation.
* [x] **Pandas:** Library for numerical computations and data manipulation.
* [x] **Scikit-learn:** Machine learning library used to train the model.
* [x] **Docker:** Containerization platform used to package the application for deployment.
* [x] **AWS:** Cloud platform used for hosting the Dockerized application and managing infrastructure.
  * [x] **AWS ECS (Elastic Container Service):** Service used to deploy and manage Docker containers in the cloud.

## Project Structure

- **data/**: Contains the `diabetes.csv` dataset used for training.
- **model/**: Contains the trained model file (`model.joblib`) and scaler file (`scaler.joblib`).
- **app.py**: The main Flask application for serving the prediction API.
- **Dockerfile**: Configuration for containerizing the Flask application.
- **requirements.txt**: Python dependencies required to run the project.
- **templates/**: Contains the HTML template for the web interface.

## Model Information
- The model used is a Random Forest Classifier trained on the [Pima Indians Diabetes Dataset](https://www.kaggle.com/uciml/pima-indians-diabetes-database).
- The model file `model.joblib` is loaded and used for predictions within the Flask API.

## Usage

- Navigate to the home page, fill in the form with the required inputs, and click "Predict" to get the diabetes prediction.
- The API can also be accessed programmatically via POST requests to /predict endpoint.

## Screenshots
![image](https://github.com/user-attachments/assets/cc6fba0f-922f-4f13-b2e7-3f401f0f5013)
![image](https://github.com/user-attachments/assets/78a35596-2fb2-44bc-a3a1-5db4c2075e6e)
![image](https://github.com/user-attachments/assets/134867a1-5707-4246-8c76-314b362525b1)
![image](https://github.com/user-attachments/assets/bb7cb272-5763-4ec7-8ef4-aec3ed4fcdfc)


### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sahinalp/diabetes-prediction-flask-aws.git
   cd diabetes-prediction-flask-aws
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Run the Flask application locally:
   ```bash
   python main.py
5. Access the application in your browser at http://127.0.0.1:5000

### Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t diabetes-prediction-app .
2. Install dependencies:
   ```bash
   docker run -p 5000:5000 diabetes-prediction-app   
