import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px 

st.title("this is the dasboard page")

df =  sns.load_dataset('titanic')
st.dataframe(df)

 #gender filter
gender = st.sidebar.multiselect('Gender',
                                 options=df['sex'].unique(),
                                 default=df['sex'].unique())
#pclass filter
pclass = st.sidebar.multiselect('passenger class',
                                options=df['pclass'].unique(),
                                default=df['pclass'].unique())
filtered_df = df[
    (df['sex'].isin(gender))& # to check whether the gender filter has the data of sex column of df
    (df['pclass'].isin(pclass))
]
fig = px.sunburst(df, path=['pclass', 'sex', 'survived'], 
                   values='age', 
                   title='Survival by Class and Gender', width=500, height=500,
                   template='plotly_dark', 
                   color='age', color_continuous_scale='RdBu')
st.plotly_chart(fig)
st.markdown("this  graph show the survival rate of passenger by their class and gender")

survived_count = filtered_df['survived'].value_counts()
fig =  px.pie(names=survived_count.index,values=survived_count.values,
       title='survival Rate', template='plotly_dark',
       width=500, height=500,)
st.plotly_chart(fig)

