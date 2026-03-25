import streamlit as st 
import datetime
date = st.date_input("selct data from here")
# i want when user enter date of birth age is calculated 
today = datetime.date.today()
age = today.year - date.year
st.write(f"your age is {age} years")