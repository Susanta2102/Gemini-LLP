from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure the API key for the generative AI model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel('gemini-1.0-pro-latest')

# Define a function to get the response from the model
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Input field and submit button
input_text = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# When submit is clicked
if submit:
    response = get_gemini_response(input_text)
    st.write(response)
