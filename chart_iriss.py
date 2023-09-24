
import streamlit as stst
import streamlit as st
import matplotlib.pyplot as plt
import time
import pandas as pd
# import graphviz as graphviz
st.write("Hello ,Welcome to Streamlit App New")
st.title ("It 's my first App Streamlit TEST")

sepal_height = st.number_input("Enter sepal height")
sepal_width = st.number_input("Enter sepal width")

petal_height = st.number_input("Enter petal height")
petal_width = st.number_input("Enter petal width")

#prediction executed
if st.button("Predict"):
    #Dataframe creation
    df=pd.DataFrame(
        {
            "sepal_height":[sepal_height], "sepal_width":[sepal_width], "petal_height":[petal_height], "petal_width":[petal_width]
        }
    )
    #df.columns = num_cols+cat_cols
    #df=df[num_cols+cat_cols] #reorder the dataframe
    st.text(f"[info] Input data as dataframe:\n{df.to_markdown()}")
    
    st.text(f"The iris has been classified as :'{''}' .")
    st.balloons()
# prompt = st.chat_input("Say something")
# if prompt:
#     st.write(f"User has sent the message following prompt:{prompt}")