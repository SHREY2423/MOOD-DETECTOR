import streamlit as st
from textblob import TextBlob
import base64
from pathlib import Path

# Set page config
st.set_page_config(page_title="AI Mood Detector", layout="centered")

# Load background image
img_path = Path("ec48b19f-319b-4033-9922-870144238a13.png")
with open(img_path, "rb") as image_file:
    encoded_img = base64.b64encode(image_file.read()).decode()

# Apply custom CSS for background and text styling
page_bg_img = f"""
<style>
body {{
  background-image: url("data:image/png;base64,{encoded_img}");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
  color: white;
  font-family: 'Arial', sans-serif;
}}

[data-testid="stAppViewContainer"] > .main {{
  background-color: rgba(0, 0, 0, 0.65);
  padding: 3rem 2rem;
  border-radius: 10px;
}}

h1 {{
  text-align: center;
  font-size: 3rem;
  color: #ffffff;
}}

.question {{
  font-size: 1.5rem;
  font-weight: bold;
  color: white;
  text-align: center;
  margin-top: 2rem;
}}

input[type="text"] {{
  background-color: #111;
  color: white;
  border-radius: 8px;
  padding: 10px;
  width: 100%;
}}

input::placeholder {{
  color: gray;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Main Heading
st.markdown("<h1>🧠 Detect Your Mood</h1>", unsafe_allow_html=True)

# First Question
st.markdown('<div class="question">Q1: How are you feeling today in one word?</div>', unsafe_allow_html=True)
user_input = st.text_input("", placeholder="Type your mood...")

if user_input:
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        mood = "😊 Positive"
    elif polarity < 0:
        mood = "☹️ Negative"
    else:
        mood = "😐 Neutral"

    st.markdown(f"<div class='question'>Your detected mood is: <b>{mood}</b></div>", unsafe_allow_html=True)

