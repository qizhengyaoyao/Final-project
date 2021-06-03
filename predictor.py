import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

revenue_filename = 'model/revenue_xgboost_model.sav'
ratings_filename = 'model/rating_xgboost_model.sav'

revenue_regressor = joblib.load(revenue_filename)
rating_regressor = joblib.load(ratings_filename)

revenue_select_sample_df = pd.read_csv("model/encoded_data/select_sample_data_rev_xgb.csv")
rating_select_sample_df = pd.read_csv("model/encoded_data/select_sample_data_rate_xgb.csv")

def film_predictor(input_dict):
    if input_dict['budget'] != "" and input_dict['year'] != "" and input_dict['day'] != "" and input_dict['duration'] != "" and input_dict['popularity'] != "":
        #organising inputs into compulsary ot optional by using a dictionary
        predictor_inputs={
            # Compulsory inputs
            "comp":{},
            # Optional inputs
            "opt":{}
            }

        predictor_inputs["comp"]['budget'] = int(input_dict['budget'])
        predictor_inputs["comp"]['year'] = int(input_dict['year'])
        predictor_inputs["comp"]['day'] = int(input_dict['day'])
        predictor_inputs["comp"]['duration'] = int(input_dict['duration'])
        predictor_inputs["comp"]['votes'] = int(input_dict['popularity'])

        if predictor_inputs["comp"]['day'] < 1 or predictor_inputs["comp"]['day'] > 365:
            err_msg = 1
            movie_name=""
            revenue_pred = "-"
            ratings_pred = "-"
        else:
            predictor_inputs["opt"]["language_"] = [ x.lstrip().rstrip().lower().title() for x in input_dict['language'].split(";")]
            predictor_inputs["opt"]["country_"] = [ x.lstrip().rstrip() for x in input_dict['country'].split(";")]
            predictor_inputs["opt"]["genre_"] = [ x.lstrip().rstrip().lower().title() for x in input_dict['genre'].split(";")]
            predictor_inputs["opt"]["company_"] = [ x.lstrip().rstrip() for x in input_dict['company'].split(";")]
            predictor_inputs["opt"]["director_"] = [ x.lstrip().rstrip().lower().title() for x in input_dict['director'].split(";")]
            predictor_inputs["opt"]["writer_"] = [ x.lstrip().rstrip().lower().title() for x in input_dict['writer'].split(";")]
            predictor_inputs["opt"]["actor_"] = [ x.lstrip().rstrip().lower().title() for x in input_dict['actor'].split(";")]
            
            # Scaling Data for specific columns (day and duration)
            X_revenue = revenue_select_sample_df
            X_rating = rating_select_sample_df    
            
            duration_scaler=MinMaxScaler().fit(X_revenue[["duration"]])
            day_scaler=MinMaxScaler().fit(X_rating[["day"]])
            
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
            
            for comp_key in predictor_inputs["comp"].keys():
                rev_test_df[comp_key]=predictor_inputs["comp"][comp_key]

            for comp_key in predictor_inputs["comp"].keys():
                rate_test_df[comp_key]=predictor_inputs["comp"][comp_key]

            for opt_key in predictor_inputs["opt"].keys():
                for x in predictor_inputs["opt"][opt_key]:
                    feature = opt_key + x
                    if feature in revenue_feat:
                        rev_test_df[feature]=1

            for opt_key in predictor_inputs["opt"].keys():
                for x in predictor_inputs["opt"][opt_key]:
                    feature = opt_key + x
                    if feature in rate_feat:
                        rate_test_df[feature]=1

            rev_test_df["duration"]=duration_scaler.transform(rev_test_df[["duration"]])
            rev_test_df["day"]=day_scaler.transform(rev_test_df[["day"]])

            rate_test_df["duration"]=duration_scaler.transform(rate_test_df[["duration"]])
            rate_test_df["day"]=day_scaler.transform(rate_test_df[["day"]])

            err_msg = 0
            movie_name="-"
            revenue_pred = "${:}".format(int(revenue_regressor.predict(rev_test_df)[0]))
            ratings_pred = round(rating_regressor.predict(rate_test_df)[0],1)

            if input_dict["moviename"] != "":
                movie_name = input_dict["moviename"]

    else:
        err_msg = 1
        movie_name=""
        revenue_pred = "-"
        ratings_pred = "-"
    
    predictions = {"err_msg":err_msg,"movie_name":movie_name,"revenue": revenue_pred, "rating": ratings_pred}

    return predictions

