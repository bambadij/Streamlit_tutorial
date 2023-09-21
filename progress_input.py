
import streamlit as stst
import streamlit as st
import time
stst.write("Hello ,Welcome to Streamlit App New")
st.title ("It 's my first App Streamlit TEST")
st.header("I want to discover streamlit")

st.number_input('Pick a number',0,10)
st.text_input('Email address')
st.date_input('Choose date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload photo')
st.color_picker('Choose your favorite color')

st.balloons()
st.progress(100)
with st.spinner('Wait for it...'):    
    time.sleep(10)