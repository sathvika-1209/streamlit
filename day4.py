import requests
import streamlit as st

city = st.text_input("Enter city")

APT_KEY = "8056a50fad712147575de992701e20c7"

if city:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APT_KEY}"
    reponse = requests.get(url)
    data= reponse.json()
    st.write(data)