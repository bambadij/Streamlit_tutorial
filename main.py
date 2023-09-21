
import streamlit as stst
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 
import time
import pandas as pd
import altair as alt
import base64
import pickle  #to load a saved modelimport base64  #to open .gif files in streamlit app
# import graphviz as graphviz
# stst.write("Hello ,Welcome to Streamlit App New")
st.title ("Build a machine learning application")
st.header("I want to discover streamlit")


@st.cache_data
def get_fvalue(val):    
    feature_dict = {"No":1,"Yes":2}    
    for key,value in feature_dict.items():        
        if val == key:           
            return value
def get_value(val,my_dict):    
            for key,value in my_dict.items():        
                if val == key:            
                    return value
app_mode = st.sidebar.selectbox('Select Page',['Home','Prediction']) #two pages

if app_mode=='Home':    
    st.title('LOAN PREDICTION :')     
    # st.image('load_image.jpg')    
    st.markdown('Dataset :')   
    data=pd.read_csv('loan_data_set.csv')    
    st.write(data.head())    
    st.markdown('Applicant Income VS Loan Amount ')    
    st.bar_chart(data[['ApplicantIncome','LoanAmount']].head(20))
    
elif app_mode=='Prediction':
    # st.image('slider.jpg')
    st.subheader('Sir/Mme,You nedd to fill all neccesary information in order to a reply to your loan request')
    st.sidebar.header('Information about client')
    gender_dict ={"Male":1,"Female":2}
    feature_dict={"No":1,"Yes":2}
    edu={'Graduate':1,'Not Graduate':2}
    prop={'Rural':1,'Urban':2,'Semiurban':3}
    Gender=st.sidebar.radio('Gender',tuple(gender_dict.keys()))
    Married=st.sidebar.radio('Married',tuple(feature_dict.keys()))
    Self_Employed=st.sidebar.radio('Self Employed',tuple(feature_dict.keys()))
    Dependents=st.sidebar.radio('Dependents',options=['0','1','2','3+'])
    Education=st.sidebar.radio('Education',tuple(edu.keys()))
    Property_Area=st.sidebar.radio('Property_Area',tuple(prop.keys()))
    ApplicantIncome=st.sidebar.slider('ApplicantIncome',0,10000,0,)
    CoapplicantIncome=st.sidebar.slider('CoappliantIncome',0,10000,)
    LoanAmount=st.sidebar.slider('LoanAmount in k$',9.0,700.0,200.0)
    Loan_Amount_Term=st.sidebar.selectbox('Loan_Amount_Term',(12.0,36.0,60.0,84.0,120.0,180.0,240.0,300.0,360.0))
    Credit_History=st.sidebar.radio('Credit_History',(0.0,1.0))
    class_0,class_1,class_2,class_3=0,0,0,0
    if Dependents== '0':
        class_0=1
    elif Dependents =='1':
        class_1=1
    elif Dependents== '2':
        class_2 =1
    else:
        class_3=1
    Rural,Urban,Semiurban=0,0,0
    if Property_Area == 'Urban':
        Urban=1
    elif Property_Area == 'Semiurban':
        Semiurban = 1
    else:
        Rural =1

    data1= {'Gender':Gender,
            'Married':Married,    
            'Dependents':[class_0,class_1,class_2,class_3],  
            'Education':Education,    
            'ApplicantIncome':ApplicantIncome,    
            'CoapplicantIncome':CoapplicantIncome,    
            'Self Employed':Self_Employed,    
            'LoanAmount':LoanAmount,    
            'Loan_Amount_Term':Loan_Amount_Term,    
            'Credit_History':Credit_History,    
            'Property_Area':[Rural,Urban,Semiurban],    
            }    
    feature_list =[ApplicantIncome,
    CoapplicantIncome,
    LoanAmount,Loan_Amount_Term,
    Credit_History,
    get_value(Gender,gender_dict),
    get_fvalue(Married),
    data1['Dependents'][0],
    data1['Dependents'][1],
    data1['Dependents'][2],
    data1['Dependents'][3],
    get_value(Education,edu),
    get_fvalue(Self_Employed),
    data1['Property_Area'][0],
    data1['Property_Area'][1],
    data1['Property_Area'][2]]   
    single_sample = np.array(feature_list).reshape(1,-1)
    if st.button("Predict"):        
        file_ = open("img/netflux.JPG", "rb")        
        contents = file_.read()        
        data_url = base64.b64encode(contents).decode("utf-8")       
        file_.close()        
        file = open("img/netflux.JPG", "rb")        
        contents = file.read()        
        data_url_no = base64.b64encode(contents).decode("utf-8")        
        file.close()        
        loaded_model = pickle.load(open('Random_Forest.sav', 'rb'))        
        prediction = loaded_model.predict(single_sample)        
        if prediction[0] == 0 :            
            st.error('According to our Calculations, you will not get the loan from Bank'    )            
            st.markdown(f'<img src="data:image/gif;base64,{data_url_no}" alt="cat gif">',unsafe_allow_html=True,)       
        elif prediction[0] == 1 :            
            st.success('Congratulations!! you will get the loan from Bank')            
            st.markdown(f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',unsafe_allow_html=True,)