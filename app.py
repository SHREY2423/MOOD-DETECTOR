import streamlit as st
from textblob import TextBlob
import random
import base64
from PIL import Image
import os

st.set_page_config(page_title="Conversational Mood Detector", layout="wide")
st.markdown("""
    <style>
        body {
            background-color: #f4f9ff;
        }
        .question-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        }
        .gif-container {
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .stButton>button {
            background-color: #8ecae6;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Data: Questions, Quotes, Jokes, GIFs ---
questions = [
    "How are you feeling right now in one word?",
    "What's been on your mind lately?",
    "Did anything today make you smile or feel sad?",
    "Do you feel supported or alone these days?",
    "How do you handle stress when it hits you?"
]

motivational_quotes = {
    "happy": ["Happiness is contagious. Pass it on!", "Keep shining! Your joy lights up others."],
    "sad": ["Tough times don’t last, tough people do.", "Your current situation is not your final destination."],
    "depressed": ["You matter. You’re not alone.", "Even the darkest night will end and the sun will rise."],
    "neutral": ["Every day is a second chance.", "Stay grounded and keep growing."]
}

jokes = {
    "happy": ["Why don’t scientists trust atoms? Because they make up everything!"],
    "sad": ["Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "depressed": ["I'm on a seafood diet. I see food and I eat it."],
    "neutral": ["Why can’t your nose be 12 inches long? Because then it would be a foot!"]
}

gif_paths = {
    "happy": "gifs/happy.gif",
    "sad": "gifs/sad.gif",
    "depressed": "gifs/depressed.gif",
    "neutral": "gifs/neutral.gif"
}

music_recommendations = {
    "happy": ["https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC"],
    "sad": ["https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1"],
    "depressed": ["https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"],
    "neutral": ["https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6"]
}

# --- Session Setup ---
if "step" not in st.session_state:
    st.session_state.step = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

st.title("🧠 Conversational Mood Detector")
st.subheader("Let's talk and discover how you're truly feeling 😊")

# --- Main Conversation Loop ---
if st.session_state.step < len(questions):
    st.markdown(f"**Q{st.session_state.step + 1}: {questions[st.session_state.step]}**")
    user_input = st.text_input("Your response:", key=f"input_{st.session_state.step}")
    if user_input:
        st.session_state.answers.append(user_input)
        st.session_state.step += 1
        st.experimental_rerun()
else:
    all_text = " ".join(st.session_state.answers).lower()
    blob = TextBlob(all_text)
    polarity = blob.sentiment.polarity

    if any(word in all_text for word in ["suicide", "worthless", "kill myself"]):
        mood = "depressed"
    elif polarity > 0.3:
        mood = "happy"
    elif polarity < -0.3:
        mood = "sad"
    elif polarity < -0.6:
        mood = "depressed"
    else:
        mood = "neutral"

    st.success(f"We think you're feeling **{mood.upper()}**")

    # --- Display GIF ---
    st.image(gif_paths[mood], width=300)

    # --- Show Recommendations ---
    st.markdown("---")
    st.subheader("🎧 Here's something for you:")
    st.markdown(f"- **Motivational Quote**: *{random.choice(motivational_quotes[mood])}*")
    st.markdown(f"- **A Little Joke**: _{random.choice(jokes[mood])}_")
    st.markdown(f"- **Spotify Vibes**: [Listen here]({music_recommendations[mood][0]})")

    st.markdown("---")
    st.markdown("Feel free to restart for another round.")
    if st.button("🔄 Restart"):
        st.session_state.step = 0
        st.session_state.answers = []
        st.experimental_rerun()

# --- Optional Stickers (decorative) ---
st.image("gifs/sticker-corner.png", width=100, use_column_width=False)
