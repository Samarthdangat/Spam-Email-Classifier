import pickle
import streamlit as st 
import numpy as np 

tfidf = pickle.load(open('vector.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


st.title('Email Spam Classifier')
input = st.text_input('Enter email subject:')

if st.button('Predict'):
    
    vector_input = tfidf.transform([input])

    result = model.predict(vector_input)[0]

    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")