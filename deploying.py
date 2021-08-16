# -*- coding: utf-8 -*-


import streamlit as st

# # Importing libraries
import numpy as np
import pickle
import streamlit as st
import pandas as pd
#Creaing Heading and small description
st.write("""
Diabetes Prediction App

This app predicts diabetes:
""")
loaded_model=open('diabeties_prediction (3).pkl','rb')
loaded_model=pickle.load(loaded_model)
import os
loaded_model = {} # scores is an empty dict already
 
if os.path.getsize('diabeties_prediction (3).pkl') > 0:      
   with open('diabeties_prediction (3).pkl',"rb") as f:    
         unpickler = pickle.Unpickler(f)
       #if file is not empty scores will be equal
        # to the value unpickled
        loaded_model = unpickler.load()
# 
# # Creating a sidebar for getting input parameters
 st.sidebar.header('User Input Parameters')
# 
# # function for creating slide bar for input
def user_input_style():
     Pregnancies = st.sidebar.slider('Pregnancies', 0, 15, 0,step=1)
     Glucose = st.sidebar.slider('Glucose', 0, 200, 0,step=1)
     BMI = st.sidebar.slider('BMI', 1, 100, 1,step=1)
     Age = st.sidebar.slider('Age', 1, 100, 1,step=1)
     data={'Pregnancies':Pregnancies,'Glucose':Glucose,'BMI':BMI,'Age':Age}
 
     style = pd.DataFrame(data, index=[0])
     return style
 
# # Creating Variable for storing the fuction value
 df = user_input_style()
 
#  Creating markdown and adding data frame input
st.subheader('User Input Parameters')
 st.write(df)
 
# 
# # Making Prediction and its probability
 prediction = loaded_model.predict(df)
 prediction_proba = loaded_model.predict_proba(df)
# 
st.subheader('Prediction')
 if prediction[0]==0:
     st.write("Patient is not diabetic")
 else:
     st.write("Patient is diabetic")
st.write(prediction)
# 
st.subheader('Prediction Probability')
st.write(prediction_proba)



