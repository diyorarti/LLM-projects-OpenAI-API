from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import openai

# Load all the environment variables
load_dotenv()

# Configure OpenAI Key
openai.api_key = os.getenv("OPENAI_API_KEY")

## Function To Load OpenAI Model and provide queries as response
def get_openai_response(question, prompt):
    # Combine the prompt and question
    full_prompt = f"{prompt[0]} {question}"
    
    # Generate a response using OpenAI's ChatCompletion
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert in SQL."},
            {"role": "user", "content": full_prompt}
        ]
    )
    
    # Extract and return the response text
    return response.choices[0].message['content']

## Function To retrieve query from the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this: SELECT COUNT(*) FROM STUDENT;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this: SELECT * FROM STUDENT 
    where CLASS='Data Science'; 
    """
]

## Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("OpenAI App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")

# if submit is clicked
if submit:
    response = get_openai_response(question, prompt)
    print(response)
    response = read_sql_query(response, "student.db")
    st.subheader("The Response is")
    for row in response:
        print(row)
        st.header(row)
