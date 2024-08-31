from dotenv import load_dotenv
import streamlit as st
import os
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
load_dotenv()
OpenAI.api_key = os.environ.get("OPENAI_API_KEY")

prompt="""You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """

def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except TranscriptsDisabled:
        st.error("Transcripts are disabled for this video. Please try another video.")
        return None

    except NoTranscriptFound:
        st.error("No transcript found for this video. It might be that the video doesn't have captions.")
        return None

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def generate_response(transcript, prompt):
    client = OpenAI()
    response = client.chat.completions.create(
        model = "gpt-4",
        messages=[
            {"role":"system", "content":"You are helpful assistant"},
            {'role':"user", "content":prompt}
        ]
    )
    return response.choices[0].message


st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)

if st.button("Get Detailed Notes"):
    transcript_text=extract_transcript_details(youtube_link)

    if transcript_text:
        summary=generate_response(transcript_text,prompt)
        st.markdown("## Detailed Notes:")
        st.write(summary)
