from flask import Flask, request,render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load model and scaler
model = joblib.load('model/model.joblib')
scaler = joblib.load('model/scaler.joblib')

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get incoming data 
        pregnancies=int(request.form['Pregnancies'])
        glucose=int(request.form['Glucose'])
        bloodPressure=int(request.form['BloodPressure'])
        skinThickness=int(request.form['SkinThickness'])
        insulin=int(request.form['Insulin'])
        BMI=float(request.form['BMI'])
        diabetesPedigreeFunction=float(request.form['DiabetesPedigreeFunction'])
        age=int(request.form['Age'])
        
        # Transform data to numpy array
        features = [pregnancies, glucose, bloodPressure, skinThickness, insulin, BMI, diabetesPedigreeFunction, age]
        input_data = np.array(features).reshape(1, -1)
        
        # Scale data
        input_data_scaled = scaler.transform(input_data)
        
        # Do predictions
        prediction = model.predict(input_data_scaled)
        probability=max(model.predict_proba(input_data_scaled)[0])
        if prediction[0]==0:
            result="You don't have diabetes with probability {:.2f}%".format(probability * 100)
        else:
            result="You have diabetes with probability {:.2f}%".format(probability * 100)
        return render_template('prediction.html', prediction=result)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)