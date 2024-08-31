from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import pdf2image
from openai import OpenAI
import PyPDF2


load_dotenv()
OpenAI.api_key = os.environ.get("OPENAI_API_KEY")


def get_response(input_text, pdf_content, prompt):
    conbined_inpput = f"{prompt}\n\nJob Description:\n{input_text}\n\nResume Content:\n{pdf_content}"
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role":"system", "content":"You are a highly experienced technical HR professional."},
            {"role":"user", "content":conbined_inpput}
        ]
    )
    return response.choices[0].message


def extract_text_from_pdf(uploaded_file):
    if uploaded_file is not None:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page].extract_text()
        return text
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="ATS SYSTEM")
st.header("ATS Tracking System")
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume(PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("PDF uploaded successfully")


submit1 = st.button("Tell me about the Resume")

submit2 = st.button("matching percentage")

input_prompt1 = """
 You are an experienced Technical Human Resource Manager,your task is to review the provided resume against the job description. 
  Please share your professional evaluation on whether the candidate's profile aligns with the role. 
 Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are an skilled ATS (Applicant Tracking System) scanner with a deep understanding of data science and ATS functionality, 
your task is to evaluate the resume against the provided job description. give me the percentage of match if the resume matches
the job description. First the output should come as percentage and then keywords missing and last final thoughts.
"""


if submit1:
    if uploaded_file is not None:
        pdf_content = extract_text_from_pdf(uploaded_file)
        response = get_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is ")
        st.write(response)
    else:
        st.write("upload your resume")
elif submit2:
    if uploaded_file is not None:
        pdf_content=extract_text_from_pdf(uploaded_file)
        response=get_response(input_prompt2,pdf_content,input_text)
        st.subheader("The Repsonse is")
        st.write(response)
    else:
        st.write("Please uplaod the resume")