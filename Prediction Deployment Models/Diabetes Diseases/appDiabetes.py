# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'diabetes-disease-prediction-model.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('Diabetes Main.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':

        Pregnancies = int(request.form['Pregnancies'])
        Glucose = request.form.get('Glucose')
        BloodPressure = request.form.get('BloodPressure')
        SkinThickness = int(request.form['SkinThickness'])
        Insulin = int(request.form['Insulin'])
        BMIs = float(request.form['BMI'])
        DiabetesPedigreeFunction = float(request.form['DiabetesPedigreeFunction'])
        Age = int(request.form['Age'])
        
        data = np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMIs,DiabetesPedigreeFunction,Age]])
        my_prediction = model.predict(data)
        
        return render_template('resultDiabetes.html', prediction=my_prediction)
        
        

if __name__ == '__main__':
	app.run(debug=True)

