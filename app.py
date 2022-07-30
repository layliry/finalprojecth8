from flask import Flask, render_template, request
app=Flask(__name__)

import numpy as py
import pickle

model=pickle.load(open('model/KNN_income.pkl','rb'))

@app.route('/')
def main() :
    return "Go to /predict for app or /report for analysis."


@app.route('/report')
def report() :
    return render_template('report.html')

@app.route('/predict', methods = ["GET"])
def hasil() :
    return render_template('index.html')

@app.route('/predict', methods = ["POST"])
def predict():
	int_features = [int(x) for x in Flask.request.form.values()]
	final_features = [np.array(int_features)]
	prediction = model.predict(final_features)[0]

	output = {0: '<= $ 50K', 1: '> $50K'}
	
	str_hasil = "I bet your income is " + str(output[prediction])

	return render_template('index.html', hasil = str_hasil)
