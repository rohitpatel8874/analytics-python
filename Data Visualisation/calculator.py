import streamlit as st 

st.title ("simple calculator")
st.write ("this is a simple calculator app using streamlit.")

c1,c2 = st.columns(2)
fnum = c1.number_input("first number", value=0)
snum = c2.number_input("second number", value=0)

option = ["add","subtract","multiply","divide"]
choice = st.radio("select operation", option )


button = st .button ("calculate")

result = 0 
if button:
    if choice == 'add' :
        result = fnum + snum 
    if choice == 'subtaract':
        result = fnum - snum 
    if choice == 'multiply':
        result = fnum * snum
    if choice == 'divide':
        result = fnum / snum
        
        
st.success (f"result: {result}")
st.balloons()
st.snow()
st.