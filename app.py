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
from sklearn.preprocessing import MinMaxScaler

#################################################
# Flask Setup
#################################################
app = Flask(__name__, template_folder = 'templates' )

#################################################
# Flask Routes
#################################################
#from tensorflow.keras.models import load_model
revenue_filename = 'model/revenue_xgboost_model.sav'
ratings_filename = 'model/rating_xgboost_model.sav'

revenue_regressor = joblib.load(revenue_filename)
rating_regressor = joblib.load(ratings_filename)

revenue_select_sample_df = pd.read_csv("model/encoded_data/select_sample_data_rev_xgb.csv")
rating_select_sample_df = pd.read_csv("model/encoded_data/select_sample_data_rate_xgb.csv")

@app.route("/")
def home():
    return(render_template('index.html', result = 100))

@app.route("/index", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':

        
        #################################################
        # Prediction
        #################################################
        budget = request.form.get('budget')
        year = request.form.get('year')
        day = request.form.get('day')
        duration = request.form.get('duration')
        popularity = request.form.get('popularity')

        if (year, day, duration, popularity, budget) != "":

            budget = int(request.form.get('budget'))
            year = int(request.form.get('year'))
            day = int(request.form.get('day'))
            duration = int(request.form.get('duration'))
            popularity = int(request.form.get('popularity'))

            language = request.form.get('language')
            country = request.form.get('country')
            genre = request.form.get('genre')
            company = request.form.get('company')
            director = request.form.get('director')
            writer = request.form.get('writer')
            actor = request.form.get('actor')

            # Scaling Data for specific columns (day and duration)
            X_revenue = revenue_select_sample_df
            X_rating = rating_select_sample_df    

            duration_scaler=MinMaxScaler().fit(X_revenue[["duration"]])
            day_scaler=MinMaxScaler().fit(X_rating[["day"]])

            #organising inputs into compulsary ot optional by using a dictionary
            revenue_inputs={
                # Compulsory inputs
                "comp":{},
                # Optional inputs
                "opt":{}    }

            revenue_inputs["comp"]["year"]= year
            revenue_inputs["comp"]["day"]= day
            revenue_inputs["comp"]["duration"]= duration
            revenue_inputs["comp"]["votes"]= popularity
            revenue_inputs["comp"]["budget"]= budget
            revenue_inputs["opt"]["language_"]= [] # Spanish/French/Russian etc.
            revenue_inputs["opt"]["genre_"]= [] # Drama/Action/Comedy etc.
            revenue_inputs["opt"]["country_"]= [] # UK/China/France/Australia etc. 
            revenue_inputs["opt"]["director_"]= [] # Woody Allen/Renny Harlin/Paul Schrader etc.
            revenue_inputs["opt"]["writer_"]= [] # Zak Penn/Tyler Perry/Christopher Nolan etc.
            revenue_inputs["opt"]["company_"]= [] # Warner Bros./Columbia Pictures/Paramount Pictures etc.
            revenue_inputs["opt"]["actor_"]= [] # Tom Hanks/Bruce Willis/Tom Cruise etc.

            #creating list of column names
            revenue_feat = revenue_select_sample_df.columns.tolist()
            rate_feat = rating_select_sample_df.columns.tolist()
            #creating initial Dataframe
            rev_dict = {}
            rate_dict = {}
            for feature in revenue_feat:
                rev_dict[feature] = [0]
            rev_test_df =pd.DataFrame.from_dict(rev_dict)

            for feature in rate_feat:
                rate_dict[feature] = [0]
            rate_test_df =pd.DataFrame.from_dict(rate_dict)

            # Language Input
            revenue_inputs["opt"]["language_"].append(language) # English/Spanish/French/Russian etc.
            # Genre Input
            revenue_inputs["opt"]["genre_"].append(genre) # Drama/Action/Comedy etc.
            # Country Input
            revenue_inputs["opt"]["country_"].append(country) # UK/China/France/Australia etc. 
            # Director Input
            revenue_inputs["opt"]["director_"].append(director) # Woody Allen/Renny Harlin/Paul Schrader etc.
            # Writer Input
            revenue_inputs["opt"]["writer_"].append(writer) # Zak Penn/Tyler Perry/Christopher Nolan etc.
            # Company Input
            revenue_inputs["opt"]["company_"].append(company) # Warner Bros./Columbia Pictures/Paramount Pictures etc.
            # Actor Input
            revenue_inputs["opt"]["actor_"].append(actor) # Tom Hanks/Bruce Willis/Tom Cruise etc.
            
            for rev_comp_key in revenue_inputs["comp"].keys():
                rev_test_df[rev_comp_key]=revenue_inputs["comp"][rev_comp_key]

            for rev_comp_key in revenue_inputs["comp"].keys():
                rate_test_df[rev_comp_key]=revenue_inputs["comp"][rev_comp_key]

            for rev_opt_key in revenue_inputs["opt"].keys():
                for x in revenue_inputs["opt"][rev_opt_key]:
                    feature = rev_opt_key + x
                    if feature in revenue_feat:
                        rev_test_df[feature]=1

            for rev_opt_key in revenue_inputs["opt"].keys():
                for x in revenue_inputs["opt"][rev_opt_key]:
                    feature = rev_opt_key + x
                    if feature in revenue_feat:
                            rate_test_df[feature]=1

            rev_test_df["duration"]=duration_scaler.transform(rev_test_df[["duration"]])
            rev_test_df["day"]=day_scaler.transform(rev_test_df[["day"]])

            rate_test_df["duration"]=duration_scaler.transform(rate_test_df[["duration"]])
            rate_test_df["day"]=day_scaler.transform(rate_test_df[["day"]])

            revenue_pred = int(revenue_regressor.predict(rev_test_df)[0])
            ratings_pred = round(rating_regressor.predict(rate_test_df)[0],2)

        else:
            revenue_pred = "Please fill out all fields marked with an asterisk"
            ratings_pred = "-"
                    #END OF PREDICTION

     
        predictions = {"revenue": revenue_pred, "rating": ratings_pred}

        return render_template("index.html", result = predictions)

    else:
        revenue_pred = "Please fill out all fields marked with an asterisk"
        ratings_pred = "-"
        predictions = {"revenue": revenue_pred, "rating": ratings_pred}

        return render_template("index.html", result = predictions)

    

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == '__main__':
    app.run(debug=True)