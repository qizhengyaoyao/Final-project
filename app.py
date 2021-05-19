import os
from flask import (Flask, render_template, request, redirect)
import numpy as np
import tensorflow

#################################################
# Flask Setup
#################################################
app = Flask(__name__, template_folder = 'templates' )

#################################################
# Flask Routes
#################################################
from tensorflow.keras.models import load_model
model = load_model("xgboost_model.h5")


@app.route("/", methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('contact.html'))

    if flask.request.method == 'POST':

        #retreiving input values
        year = flask.request.form['year']
        day = flask.request.form['day']
        budget = flask.request.form['budget']
        duration = flask.request.form['duration']
        votes = flask.request.form['votes']
        


        input_variables = pd.DataFrame([[title,budget,date]],
                                       columns=['title', 'budget', 'date'],
                                       dtype=float)

        prediction = model.predict(input_variables)[0]

        return(flask.render_template("review.html"), original_input = {'title':title,'budget':budget,'date':date}, 'result' = prediction)
    




if __name__ == '__main__':
    app.run(debug=True)