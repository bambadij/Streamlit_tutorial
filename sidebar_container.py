

import streamlit as stst
import streamlit as st
import time
stst.write("Hello ,Welcome to Streamlit App New")
st.title ("It 's my first App Streamlit TEST")
st.header("I want to discover streamlit")

st.sidebar.title('This is the written inside the sidebare')
st.sidebar.button('Click')
st.sidebar.radio('Pick your gender',['Male','Female'])
container = st.container()
container.write('This is written inside the container')
st.write('It outsider')