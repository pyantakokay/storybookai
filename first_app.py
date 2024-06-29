import streamlit as st

st.title("My First Streamlit App")

st.write("Welcome to my streamlit app!")

st.button("Reset", type="primary")
if st.button("Say Hello"):
  st.write("Why Hello There")
else:
  st.write("Goodbye")
