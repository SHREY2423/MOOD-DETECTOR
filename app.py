import streamlit as st
from textblob import TextBlob
import random

# Random background image URLs
backgrounds = [
    "https://images.unsplash.com/photo-1503264116251-35a269479413",
    "https://images.unsplash.com/photo-1522199794611-8e7f1f7d7363",
    "https://images.unsplash.com/photo-1533743983669-94fa5c4338ec",
    "https://images.unsplash.com/photo-1494172961521-33799ddd43a5",
    "https://images.unsplash.com/photo-1504384308090-c894fdcc538d"
]

bg_url = random.choice(backgrounds)

# Streamlit page config
st.set_page_config(page_title="Mood Detector", layout="centered")

# Background and styling
st.markdown(f"""
    <style>
    body {{
        background-image: url("{bg_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stAppViewContainer"] > .main {{
        background: rgba(0, 0, 0, 0.65);
        padding: 3rem 2rem;
        border-radius: 12px;
        color: #fff;
        font-family: 'Segoe UI', sans-serif;
    }}
    h1 {{
        text-align: center;
        font-size: 3rem;
        color: #ffffff;
    }}
    .question {{
        font-size: 1.5rem;
        margin-top: 2rem;
        text-align: center;
        font-weight: bold;
    }}
    .result {{
        font-size: 1.5rem;
        text-align: center;
        margin-top: 2rem;
        color: #00ffae;
    }}
    </style>
""", unsafe_allow_html=True)

# App Heading
st.markdown("<h1>🧠 AI Mood Detector</h1>", unsafe_allow_html=True)

# Mood input
st.markdown('<div class="question">Q1: How are you feeling today in one word?</div>', unsafe_allow_html=True)
user_input = st.text_input("", placeholder="Type here...")

# Mood detection logic
if user_input:
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        mood = "😊 Positive"
    elif polarity < 0:
        mood = "😞 Negative"
    else:
        mood = "😐 Neutral"

    st.markdown(f"<div class='result'>Your detected mood is: <b>{mood}</b></div>", unsafe_allow_html=True)
