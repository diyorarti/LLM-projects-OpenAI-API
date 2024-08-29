from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
import os 

# Set the page configuration as the first Streamlit command
st.set_page_config(page_title="Chatbot", page_icon="🤖", layout="centered")

load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

# Initialize history 
if "history" not in st.session_state:
    st.session_state.history = []

# Function to get OpenAI response 
def get_response(input_question):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.5,
        max_tokens=200,
        messages=[
            {"role":"system", "content":"You are a helpful assistant"},
            {"role":"user", "content":input_question}
        ]
    )
    return response.choices[0].message.content

# Load custom CSS from a file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load the CSS file
load_css("style.css")

# Function to handle input submission
def handle_input():
    st.session_state.submit = True

# Initialize Streamlit app without extra headings
st.markdown("<h2 style='text-align: center;'>🤖 Chatbot</h2>", unsafe_allow_html=True)

# Display the chat history
for idx, entry in enumerate(st.session_state.history):
    st.markdown(f"<div class='bot-bubble'>{entry['response']}</div><div class='clear'></div>", unsafe_allow_html=True)
    st.markdown(f"<div class='user-bubble'>{entry['question']}</div><div class='clear'></div>", unsafe_allow_html=True)

# Create a container for the input box at the bottom
with st.container():
    input = st.text_input("Message", key="input", placeholder="Type your message here...", on_change=handle_input)

# Handle the input submission
if st.session_state.get("submit") and input:
    response = get_response(input)
    st.session_state.history.append({"question": input, "response": response})
    # Reset the input field by setting a query param (this triggers a rerun)
    st.session_state.submit = False


# Sidebar for new chat button
with st.sidebar:
    if st.button("New Chat"):
        st.session_state.history.clear()
       
