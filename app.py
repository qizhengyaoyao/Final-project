import os
#from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import numpy as np
#import tensorflow
import joblib
#from flask_cors import CORS
import requests
import pandas as pd

#################################################
# Flask Setup
#################################################
app = Flask(__name__, template_folder = 'templates' )

#################################################
# Flask Routes
#################################################
#from tensorflow.keras.models import load_model
model = joblib.load("model/revenue_xgboost_model.sav")


@app.route("/")
def home():
    return(render_template('index.html', result = 100))

@app.route("/index", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':

        #retreiving input values
        budget = request.form['budget']
        votes = request.form['popularity']
        year = request.form['year']
        day = request.form['day']
        duration = request.form['duration']

        # input_variables = pd.DataFrame([[title,budget,date]],
        #                                columns=['title', 'budget', 'date'],
        #                                dtype=float)

        # prediction = model.predict(input_variables)[0]

        if budget=="":
            prediction=10000000
        else:
            prediction=int(budget)*10

        return render_template("index.html", result = prediction)
    else:
        prediction=10000000
        return render_template("index.html", result = prediction)

    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == '__main__':
    app.run(debug=True)