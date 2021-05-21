import os
from predictor import film_predictor
#from dotenv import load_dotenv
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
#from flask_cors import CORS
import requests

#################################################
# Flask Setup
#################################################
app = Flask(__name__, template_folder = 'templates' )

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    predictions = {"err_msg":0,"movie_name":"","revenue": "-", "rating": "-"}
    return(render_template('index.html', result = predictions))

@app.route("/index", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        #################################################
        # Prediction
        #################################################
        input_dict = {}

        input_dict['moviename'] = request.form.get('moviename')
        input_dict['budget'] = request.form.get('budget')
        input_dict['year'] = request.form.get('year')
        input_dict['day'] = request.form.get('day')
        input_dict['duration'] = request.form.get('duration')
        input_dict['popularity'] = request.form.get('popularity')

        input_dict['language'] = request.form.get('language')
        input_dict['country'] = request.form.get('country')
        input_dict['genre'] = request.form.get('genre')
        input_dict['company'] = request.form.get('company')
        input_dict['director'] = request.form.get('director')
        input_dict['writer'] = request.form.get('writer')
        input_dict['actor'] = request.form.get('actor')

        predictions=film_predictor(input_dict)

        return render_template("index.html", result = predictions)

    else:
        err_msg = 1
        movie_name=""
        revenue_pred = "-"
        ratings_pred = "-"
        predictions = {"err_msg":err_msg, "revenue": revenue_pred, "rating": ratings_pred}

        return render_template("index.html", result = predictions)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/model")
def model():
    return render_template("model.html")

if __name__ == '__main__':
    app.run(debug=True)