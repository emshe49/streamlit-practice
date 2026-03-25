import streamlit as st


st.title("Chai Maker App")
if st.button("Make Chai"):
    st.success("Your Chai is ready")



add_masala = st.checkbox("add Masala")
if(add_masala):
    st.write("Masala Added To Your Chai"
    )

tea_type = st.radio("Pick your chai base",["milk","honey","bee"])

st.write(f"select base {tea_type} ")