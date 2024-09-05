from dotenv import load_dotenv
load_dotenv() # Activate the local env variables

import streamlit as st
import os
import google.generativeai as genai

# Setup the local environment for the Google API key
genai.configure(api_key = os.getenv("GOOGLE-API-KEY"))

# GenAI model
model = genai.GenerativeModel("gemini-pro")

# Function to generate the content
def generate(question):
    response = model.generate_content(question)
    return(response.text)

##### Streamlit Webpage #####
st.set_page_config(page_title="LLM QnA Application")
st.header("Generating answers using Gemini Pro")

# Streamlit run app.py to run the application
input = st.text_input(label="Ask the Question", key="input")

submit = st.button(label = "Generate Response")

if submit:
    response = generate(input)
    st.subheader("The response is: ")
    st.write(response)
    
    # streamlit run app.py
