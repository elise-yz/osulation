import streamlit as st
from osulation import start_game

# Set the title of the app
st.title("demo")

# Add a button
if st.button("Click Me"):
    start_game()