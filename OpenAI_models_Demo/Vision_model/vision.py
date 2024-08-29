from dotenv import load_dotenv
import streamlit as st
from io import BytesIO
import requests
from PIL import Image
from openai import OpenAI
import os

load_dotenv()
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

def get_response(input):
    client = OpenAI()
    response = client.images.generate(
        model="dall-e-3",
        prompt=input,
        size="1024x1024",
        quality="standard",
        n=1
    )
    return response.data[0].url

def download_image(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    return image

st.set_page_config(page_title="Image Generator", page_icon="🤖")
st.title("Image Generator Bot")

input_prompt = st.text_input('describe your image to generate...')

if st.button("Generate Image"):
    if input_prompt:
        with st.spinner("Generating Image..."):
            image_url = get_response(input_prompt)
            st.image(image_url, caption='Generated Image', use_column_width=True)
            
            # Download the image from the generated URL
            image = download_image(image_url)
            
            # Save image to a BytesIO object
            img_byte_arr = BytesIO()
            image.save(img_byte_arr, format='PNG')
            img_byte_arr = img_byte_arr.getvalue()

            # Add a download button
            st.download_button(
                label="Download Image",
                data=img_byte_arr,
                file_name="generated_image.png",
                mime="image/png"
            )
    else:
        st.warning("Please enter a prompt")