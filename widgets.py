import streamlit as stst
import streamlit as st
stst.write("Hello ,Welcome to Streamlit App New")
st.title ("It 's my first App Streamlit TEST")
st.header("I want to discover streamlit")
st.checkbox('yes')
st.button('Apply')
st.radio('Choose your gender',['Male','Female'])
st.selectbox('pick your gender',['Male','Female'])
st.multiselect('choose a planet',['Jupiter','Mars','neptune'])
st.select_slider('Pick a mark',['Bad','Good','Excellent'])
st.slider('Pick a number',0,50)