import streamlit as st

st.write("choose you fav programming language")

lang = st.selectbox("choose 1:",["c++","java","python","r"])
if lang in ["python","java"]:
    st.write(f"your fav language is: {lang}")
    st.success("Thanks good choice")
else:
    st.error("bad choice")