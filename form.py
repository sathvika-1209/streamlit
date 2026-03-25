import streamlit as st
import pandas as pd
st.title(" form")
with st.form("my_form"):
    st.write("inside the form")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("enter first your name")
    with col2:
        st.text_input("enter your last name")
    st.number_input("enter your age")
    st.text_area("enter the address")
    st.selectbox("enter the branch",["cse","ecs","eee","aiml","civil","mech"])
    st.selectbox("select your year",[1,2,3,4])
    st.form_submit_button("submit")
    submit = True
    if submit:
        st.write("form submitted successfully")
    else:
        st.write("form not submitted")