import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for next days")

place=st.text_input("Place: ")
days=st.slider("Forecast Days: ",min_value=1,max_value=5,help="Select the no of days for forecasting")

option=st.selectbox("Select Data to view:",("Temperature","Sky"))
st.subheader(f"{option} for next {days} days in {place}")

data=get_data(place,days,option)

d,t = get_data(days)

figure=px.line(x=d,y=t,labels={"x" : "Date","y" : "Temperatures(C)"})
st.plotly_chart(figure)



