import streamlit as st
import google.genai as genai
import os

# Function to read the script.js file
@st.cache_data
def read_script_js():
    """Reads the content of script.js"""
    try:
        with open("script.js", "r") as f:
            return f.read()
    except FileNotFoundError:
        st.error("script.js not found. Please make sure the file exists.")
        return None

# Configure the Gemini API
@st.cache_resource
def load_client() -> genai.Client:
    """Load Google Gen AI Client."""
    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except (FileNotFoundError, KeyError):
        st.error("🚨 Configuration Error: `GEMINI_API_KEY` not found in `.streamlit/secrets.toml`.")
        st.stop()
    
    return genai.Client(
        api_key=api_key,
    )

client = load_client()
script_content = read_script_js()

MODEL_ID = "gemini-2.0-flash-001" 

st.title("My First GenAI App")

# Text input
prompt = st.text_input("Enter a prompt:")

# Button
if st.button("Generate"): 
    if prompt and script_content:
        try:
            # Combine the script content with the user's prompt
            combined_prompt = f"Based on the following Javascript code, please answer the user's prompt.\n\nCode:\n```javascript\n{script_content}\n```\n\nUser Prompt: {prompt}"
            response = client.models.generate_content(model=MODEL_ID, contents=combined_prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    elif not script_content:
        st.warning("Could not generate response because script.js is missing.")
    else:
        st.warning("Please enter a prompt.")