import pickle

import numpy as np
from flask import Flask, request, render_template, redirect, url_for, flash



model = pickle.load(open("model.pkl", 'rb'))
app = Flask(__name__)
import secrets

secret = secrets.token_urlsafe(32)

app.secret_key = secret


@app.route("/", methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        try:

            age = int(request.form['age'])
            sex = request.form['sex']
            cp = request.form['cp']
            trestbps = int(request.form['trestbps'])
            chol = int(request.form['chol'])
            fbs = request.form['fbs']
            restecg = int(request.form['restecg'])
            thalach = int(request.form['thalach'])
            exang = request.form['exang']
            oldpeak = float(request.form['oldpeak'])
            slope = request.form['slope']
            ca = int(request.form['ca'])
            thal = request.form['thal']
            data = [int(age), int(sex), int(cp), int(trestbps), int(chol), int(restecg), int(fbs), int(thalach),
                    int(exang), float(oldpeak), int(slope), int(ca), int(thal)]
            # convert data to numpy array
            data_as_array = np.asarray(data)
            data_reshape = data_as_array.reshape(1, -1)
            prediction = model.predict(data_reshape)

            return render_template('result.html', prediction = prediction)
        except ValueError:
            flash('invalid inputs', 'info')
            return redirect(url_for("home"))



if __name__ == "__main__":
    app.run()

