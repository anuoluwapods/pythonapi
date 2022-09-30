import streamlit as st
import json
import requests


st.title("Basic Calculator app ")

# User inputs
option = st.selectbox('What opeatio do you want to perform?',
                      ('Addition', 'Subtraction','Multiplication','Division'))

st.write("")
st.write("Select the numbers from the sliders below")

x = st.slider("x", 0, 100, 20)
y = st.slider("y", 0, 130, 10)

# Convert input into json format
inputs = {"operation": option, "x":x, "y":y}

#User click on button and fetch API
if st.button('Calculate'):
    res =requests.post(url= "http://127.0.0.1:8000/calculate", data=json.dumps(inputs))
    st.subheader(f"Response from API = {res.text}")
