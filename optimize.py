import streamlit as st
import os

from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-pro-latest')

def get_gemini_response(input, url, user_prompt):
    response = model.generate_content([input, url, user_prompt])
    return response.text
    
st.set_page_config(page_title="LinkedIn boost")

st.header('Optimize your LinkedIn profile')
user_input_prompt = st.text_input("Input prompt: ", key='input')
if (user_input_prompt == ""):
    user_input_prompt = "ignore this additional prompt"
url = st.text_input("LinkedIn URL: ", key='url')

submit = st.button("Go!")

base_prompt = """
You are a professional coach.
You will be given a prompt and a linkedIn URL. Help with suggestions on how
to optimize the linkedin profile for better appeal to all visitors. The
optional prompt will give you additional cues on what the user is looking for.
"""

if submit:
    response = get_gemini_response(base_prompt, url, user_input_prompt)
    st.subheader("My suggestions: ")
    st.write(response)

