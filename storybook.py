# IMPORTS
from openai import OpenAI
from google.colab import userdata
import google.generativeai as genai
from IPython.display import Image
import streamlit as st
import os

client = OpenAI(api_key = os.environ['OPENAI_SECRET_KEY'])
genai.configure(api_key = os.environ["GOOGLE_API_KEY"])

# STORY_AI
def story_ai(msg,sysprompt):
  story_response=client.chat.completions.create(
      model="gpt-4o",
      messages=[{
          "role":"system",
          "content":sysprompt
      },
        {
          "role":"user",
          "content":msg
         }],
      max_tokens=300
  )

  story=story_response.choices[0].message.content
  return story

# ART_AI
def art_ai(msg):
  art_response=client.images.generate(
      model="dall-e-2",
      prompt=msg,
      size="1024x1024",
      n=1,
      style="vivid"
  )

  art=art_response.data[0].url
  return art

# DESIGN_AI
def design_ai(msg):
  design_model=genai.GenerativeModel('gemini-1.5-flash')
  design=design_model.generate_content([f"""
    Craft a fitting prompt for an AI image generator
    to generate a most fitting cover art for this story:
    {msg}
  """])

  return design.text

# STORYBOOK_AI
def storybook_ai(msg,sysprompt):
  story=story_ai(msg,sysprompt)
  design=design_ai(story)
  art=art_ai(design
    st.image(art)
  st.write(story)

msg=st.text_input("What story do you want to make?")
sysprompt="""
You are the best-selling author.
You will take in user's request and create a 100 word short story.
The story should be suitable for children ages 7 to 9.
"""
gemerate_story = st.button("Generate story")
with generate_story:
  storybook_ai(msg,sysprompt)