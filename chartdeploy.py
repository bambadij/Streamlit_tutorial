
import streamlit as stst
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 
import time
import pandas as pd
import altair as alt
# import graphviz as graphviz
stst.write("Hello ,Welcome to Streamlit App New")
st.title ("It 's my first App Streamlit TEST")
st.header("I want to discover streamlit")

rand=np.random.normal(1, 2, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
st.title('Line Chart')
df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
st.line_chart(df)

st.title('Bar Chart')
df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
st.bar_chart(df)
st.title('Area Chart')
df= pd.DataFrame(np.random.randn(10, 2),columns=['x', 'y'])
st.area_chart(df)
st.title('Altair Chart')
df=pd.DataFrame(np.random.randn(500,3),columns=['x','y','z'])
c=alt.Chart(df).mark_circle().encode(x='x',y='y',size='z',color='z',tooltip=['x','y','z'])
st.altair_chart(c, use_container_width=True)

# st.title('Graph Viz Chart')
# st.graphviz_chart('''digraph {Big_shark -> Tuna  
#                   Tuna -> Mackerel       
#                   Mackerel -> Small_fishes        
#                   Small_fishes -> Shrimp    }''')
st.title('MAP With Streamlit')
df = pd.DataFrame(np.random.randn(500, 2) / [50, 50] + [14.716677,-17.467686],columns=['lat', 'lon'])
st.map(df)
st.balloons()
st.progress(100)
with st.spinner('Wait for it...'):    
    time.sleep(10)
