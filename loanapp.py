import streamlit as st
import pandas as pd
import pickle as pk

model = pk.load(open('model.pkl','rb'))
scaler = pk.load(open('scaler.pkl','rb'))

st.header('Loan Prediction App Created By Sanjay Krishnan')

no_of_dep = st.slider('Choose No of dependets', 0, 20)
grad = st.selectbox('Choose Education',['Graduated','Not Graduated'])
self_emp = st.selectbox('Self Employeed ?',['Yes','No'])
Annual_Income = st.slider('Choose Annual Income', 0, 100000)
Loaan_Amount = st.slider('Choose Loan Amount', 0, 100000)
Loan_dur = st.slider('Choose Loan Duration', 0, 20)
Cibil_sc = st.slider('Choose Cibil Score', 0, 1000)
Assets = st.slider('Choose Assets', 0, 100000)


if st.button("Predict"):    
    pred_data = pd.DataFrame([[no_of_dep,'0','1',Annual_Income,Loaan_Amount,Loan_dur,Cibil_sc,Assets]],
                         columns=['no_of_dependents','education','self_employed','income_annum','loan_amount','loan_term','cibil_score','Assets'])
    pred_data = scaler.transform(pred_data)
    predict = model.predict(pred_data)
    if predict[0] == 1:
        st.markdown('Load is Approved')
    else:
        st.markdown('Loan is Rejected')