"""
To run this app, in your terminal:
> python h1b_lca_classification_api.py
"""
import connexion
import pandas as pd
from sklearn.externals import joblib

# Instantiate our Flask app object
app = connexion.FlaskApp(__name__, port=5555, specification_dir='swagger/')
application = app.app

# Load our pre-trained model
clf = joblib.load('./model/svm_final_pipeline.joblib')

#Load the encoder
enc = joblib.load('./model/final_preprocessing_pipeline.joblib')

# Implement a simple health check function (GET)
def health():
    # Test to make sure our service is actually healthy
    try:
        predict('Y', 'WASHINGTON', 'INFOSYS LIMITED', 'COMPUTER AND MATHEMATICAL OCCUPATIONS', 
        44370.0)
    except:
        return {"Message": "Service is unhealthy"}, 500

    return {"Message": "Service is OK"}

# Implement our predict function
def predict(full_time_position, state, employer, occupation, prevailing_wage):
    # Accept the feature values provided as part of our POST

    list_input = [(full_time_position, prevailing_wage, state, employer.lower(), occupation.lower())]
    X_test = pd.DataFrame(list_input, columns = ['FULL_TIME_POSITION','PREVAILING_WAGE','STATE','NEW_EMPLOYER','OCCUPATION'], index=[1])

    #encoding the new test data 
    X_test_encoded = enc.transform(X_test)


    #predicting on the encoded test data 
    y_pred = clf.predict(X_test_encoded)

    if y_pred == 0: 
        #If certified(class is mapped to 0)
        pred_proba = clf.predict_proba(X_test_encoded)[:,0][0]
    else: 
        #If denied(class is mapped to 1)
        pred_proba = clf.predict_proba(X_test_encoded)[:,1][0]

    #pred_proba = clf.predict_proba(X_test_encoded)[:,0][0]


    # Map the predicted value to an actual class
    if y_pred == 0: 
        predicted_class = "CERTIFIED"
    else: 
        predicted_class = "DENIED"
    
    # round the predict proba value and set to new variable
    probability_certified = (round(pred_proba,3))*100

    #Converting to percentage and making a string
    probability_string = str(probability_certified)+"%"
    
    # create JSON object
    output = {'prediction': predicted_class, 'probability': probability_string}
        
    return output


    #making sense of the predicted probability 
    #if y_pred_proba[1:] >= 0.7:
    #   prediction_proba = "You have a higher chance of being certified!"
    #else: 
    #   prediction_proba = "You have higher chance of being denied.. :("


    # # Return the prediction as a json
    # return {
    #     "Probability your LCA will be certified" : probability_certified
    # }


# Read the API definition for our service from the yaml file
app.add_api("h1b_classification_api.yaml")

# Start the app
if __name__ == "__main__":
    app.run()
