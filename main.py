import streamlit as st 
import pickle
st.title("titanic  survival")
st.sidebar.title("Input Parameters")
pclass=st.sidebar.selectbox('select passenger class',[1,2,3])
sex=st.sidebar.selectbox("select gender (Female,Male)",['Female','Male'])
age=st.sidebar.number_input('Age',0,100)
fare=st.sidebar.number_input('Fare',0.0,300.00)
if sex=='Female':
    se=0
elif sex=='Male':
    se=0

with open ('model.pkl','rb') as f:
    model=f.read()

if st.sidebar.button('Predict',key='predict_button'):
    input_data=[[pclass,se,age,fare]]
    prediction=model.predict(input_data)
    if prediction[0]==1:
        st.success("the passenger survived")
    else:
        st.error("low survival chances")
