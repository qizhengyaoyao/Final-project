def movie_prediction(year, day, budget, duration, votes, language):
    
    for_df = {}
    
    for col in col_list:
        for_df[col] = [0]
    
    input_variables = pd.DataFrame(for_df)
    
    
    if f"language_{language.capitalize()}" in col_list:
        
        
        if (year, day, budget, duration, votes, language):
            
            language_cap = "language_"+language.capitalize()

            
            input_variables.loc[:,"year"] = year
            input_variables.loc[:,"day"] = day
            input_variables.loc[:,"budget"] = budget
            input_variables.loc[:,"duration"] = duration
            input_variables.loc[:,"votes"] = votes
            input_variables.loc[:,language_cap] = 1
    
            prediction = model.predict(input_variables)
    
    return prediction[0]






#using pickle to load model 
import pickle
file_name = 'Model/xgboost_model.h5'

model = pickle.load(open(file_name, "rb"))

# creating dictionary to turn into dataframe for all inputs
for_df = {}

# list of columns names
col_list = list(select_sample_df.columns)

# dummy data
year = 2021
day = 360
budget = 100000000
duration = 90
votes = 100
language = 'english'

# for loop that makes the value in all cells zero
for col in col_list:
    for_df[col] = [0]
    
# creating dataframe 
input_variables = pd.DataFrame(for_df)

# if the user's selected language is in our list of languages...  
if f"language_{language.capitalize()}" in col_list:

    #and if there values for each of the following inputs
    if (year, day, budget, duration, votes, language):

        # in case the input is all caps
        language = language.lower()
        
        # taking 'english' and making it conform to our language columns => language_English
        language_cap = "language_"+language.capitalize()

        #updating dataframe with input data
        input_variables.loc[:,"year"] = year
        input_variables.loc[:,"day"] = day
        input_variables.loc[:,"budget"] = budget
        input_variables.loc[:,"duration"] = duration
        input_variables.loc[:,"votes"] = votes
        input_variables.loc[:,language_cap] = 1
        
        #running model
        prediction = model.predict(input_variables)

print(prediction)