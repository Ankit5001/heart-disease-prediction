from flask import Flask, render_template, request
import pandas as pd
from model.predictor import HeartPredictor

app = Flask(__name__)
predictor = HeartPredictor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get values from the form
        features = {
            'Age': float(request.form['Age']),
            'Sex': request.form['Sex'],
            'ChestPainType': request.form['ChestPainType'],
            'Cholesterol': float(request.form['Cholesterol']),
            'FastingBS': int(request.form['FastingBS']),
            'MaxHR': float(request.form['MaxHR']),
            'ExerciseAngina': request.form['ExerciseAngina'],
            'Oldpeak': float(request.form['Oldpeak']),
            'ST_Slope': request.form['ST_Slope']
        }
        
        prediction = predictor.predict(features)
        probability = predictor.predict_proba(features)
        
        return render_template('result.html', 
                             prediction=prediction, 
                             probability=probability,
                             features=features)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)