import streamlit as st
import numpy as np
import joblib
st.title("Fraud Detection App")
#Interface
st.markdown('Input Features of the Transaction')
Input_Sender_ID = st.number_input('Input Sender ID')
Input_Sender_ID= st.number_input('Input_Receiver_ID')


#Predict button
if st.button('Predict Fraud Detection'):
    model = joblib.load('CreaditCard.pkl')
    X = np.array([Input_Sender_ID,Input_Sender_ID])
    predictions = model.predict(features)
    
def check_fraud(transaction_amount):
    if transaction_amount > 1000:
        return {"fraudulent"}
    else:
        return {"valid"}