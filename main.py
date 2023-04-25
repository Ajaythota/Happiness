import streamlit as st
import pandas as pd
import os
import plotly.express as px


path=os.getcwd()+"\data\happy.csv"
df=pd.read_csv(path)


def get_data( option1, option2):
    df1 = df[option1]
    df2=df[option2]
    return df1,df2

st.title("In Search of Happiness")
#c=st.selectbox("select country ",df['country'])
option1=st.selectbox("Select data to view ", list(df.columns[1:]),key=1) # removing country column
option2=st.selectbox("Select data to view ", list(df.columns[1:]),key=2) # removing country column
st.subheader(f"   {option1}  vs {option2 }" )

o1,o2=get_data(option1,option2)

figure=px.scatter(x=o1,y=o2,labels={"x":option1,"y":option2})
st.plotly_chart(figure)