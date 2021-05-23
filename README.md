# Film Review & Revenue Predictor

## Background

Producers pitch movie ideas to studios in hopes of making the next blockbuster, or movie theatres may need to know which film will have a higher probability of positive reception. Traditionally producing or hosting a blockbuster film was more art than science.

Our Machine Learning Program enables Producers to better assess and choose which films would be a success and which are likely to flop with greater confidence.

## Workflow

1. [Data Wrangling](model/01_Data_Wrangling.ipynb)
2. [Model selection](model/02_Model_Selection.ipynb)
3. [Feature selection](model/03_Feature_Importance.ipynb)
4. [XGBoost Model training](model/04_Predictor_XGBOOST_Hyperparameter.ipynb)
5. [LightGBM Model training](model/05_Predictor_LightGBM_Hyperparameter.ipynb)
6. [Web Page Design](templates/index.html)
7. [Web Design](app.py)
8. [Deployment](requirements.txt)

## File description

Raw data [IMDb movies.csv] from [Kaggle](https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset) can be found in [data](data) folder. Cleaned data, including selected features and encoded inputs, can be found in [encoded_data](model/encoded_data) folder.

    .
    ├── analysis            # data and model exploration 
    ├── data                # raw data
    ├── model               # model training and cleaned data
    │   ├── encoded_data    # cleaned data
    │   └── ....            # model training codes
    ├── static              # css files
    ├── templates           # html files
    └── ...                 # backend and deployments files

## Result

The 

The preditor has been deployed on [Heroku](https://film-predict.herokuapp.com/) and the model traing analysis has also been given in the [model introduction page](https://film-predict.herokuapp.com/model).

![Film predictor](images/predicta.jpeg)

## Summary
