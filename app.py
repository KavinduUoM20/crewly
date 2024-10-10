import streamlit as st

# Title of the web app
st.title('Hello, Crewly!')

# A text input box for user input
name = st.text_input('Enter your name')

# A button that when clicked displays a message
if st.button('Submit'):
    st.write(f'Hello {name}! Welcome to Crewly.')
