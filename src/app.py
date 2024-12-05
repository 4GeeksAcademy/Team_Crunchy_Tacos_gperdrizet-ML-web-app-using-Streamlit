'''Simple Streamlit web app.'''
import pickle
import pandas as pd
import streamlit as st

# Load the model
model_file='../models/model.pkl'

with open(model_file, 'rb') as input_file:
    model=pickle.load(input_file)

# Dictionary to translate numerical predictions into
# human readable strings
class_dict={
    '0': 'Not diabetic',
    '1': 'Diabetic'
}

# Page title
st.title('Diabetes prediction')

# Set up inputs for the user to enter data - take a look at the tutorial
# for a hint on how to do this. Also, if you are using the model
# supplied above, you need to send it four features: Glucose,
# Insulin, BMI and Age
val1 = st.slider("Glucose", min_value = 70, max_value = 200, step = 1)
val2 = st.slider("Insulin", min_value = 0, max_value = 50, step = 1)
val3 = st.slider("BMI", min_value = 18, max_value = 45, step = 1)
val4 = st.slider("Age ", min_value = 10, max_value = 100, step = 1)


# When the user clicks 'Predict'
if st.button('Predict'):

        # Format the data for input into the model. For the model
        # Supplied above, it should be a Pandas dataframe with four
        # columns, one for each feature and one row.

        # Then do the prediction and covert the class number that the
        # model returns to a human readable string, like 'diabetic' etc.
        prediction = str(model.predict([[val1, val2, val3, val4]])[0])
pred_class = class_dict[prediction]
st.write("Prediction:", pred_class)

    # Display the prediction to the user
st.write('Prediction:', predicted_class)