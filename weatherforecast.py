import streamlit as st
import plotly.express as px

st.title("Weather forecast for next days")

place=st.text_input("Place: ")
days=st.slider("Forecast Days: ",min_value=1,max_value=5,help="Select the no of days for forecasting")

option=st.selectbox("Select Data to view:",("Temperature","Sky"))
st.subheader(f"{option} for next {days} days in {place}")

def get_data(days):
    dates = ["2022-10-10","2022-10-17","2022-10-19"]
    temperatures = [10,11,15]
    temperatures = [ days * i for i in temperatures ]
    return dates,temperatures

d,t = get_data(days)

figure=px.line(x=d,y=t,labels={"x" : "Date","y" : "Temperatures(C)"})
st.plotly_chart(figure)



