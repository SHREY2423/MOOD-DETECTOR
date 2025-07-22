import streamlit as st
from textblob import TextBlob
import random

# ------------------ Setup Page Config ------------------
st.set_page_config(page_title="Conversational Mood Detector",
                   page_icon="🧠",
                   layout="centered")

# ------------------ Calm Theme Background ------------------
st.markdown("""
    <style>
    body {
        background-color: #f0f7f4;
        font-family: 'Segoe UI', sans-serif;
    }
    .stTextInput>div>div>input {
        background-color: #e8f5e9;
        color: #000000;
    }
    .stButton>button {
        background-color: #aed581;
        color: black;
        font-weight: bold;
        border-radius: 12px;
        padding: 0.5em 1em;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Data ------------------
questions = [
    "How are you feeling right now in one word?",
    "What kind of day did you have today?",
    "What’s something on your mind?",
    "How much energy do you have right now (scale of 1-10)?",
    "Did anything recently make you smile or feel good?",
    "What kind of music do you feel like listening to right now?"
]

mood_gifs = {
    "happy": ["https://media.giphy.com/media/l0HlvtIPzPdt2usKs/giphy.gif"],
    "sad": ["https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif"],
    "depressed": ["https://media.giphy.com/media/l1J3preURPiwjRPvG/giphy.gif"],
    "neutral": ["https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"],
    "joyful": ["https://media.giphy.com/media/3o7btXJQm5DD8/giphy.gif"]
}

mood_quotes = {
    "happy": [
        "Happiness is not by chance, but by choice.",
        "Keep smiling, because life is a beautiful thing."
    ],
    "sad": [
        "Tough times never last, but tough people do.",
        "Every day may not be good, but there's something good in every day."
    ],
    "depressed": [
        "You are stronger than you think. Keep going.",
        "It's okay to not be okay. Just don't give up."
    ],
    "neutral": [
        "Take a deep breath. Keep moving forward.",
        "You’re doing better than you think you are."
    ],
    "joyful": [
        "Let your joy burst forth like flowers in the spring.",
        "Joy is the simplest form of gratitude."
    ]
}

def analyze_mood():
    all_text = " ".join([st.session_state.get(f"input_{i}", "") for i in range(len(questions))])
    blob = TextBlob(all_text)
    polarity = blob.sentiment.polarity

    if any(word in all_text.lower() for word in ["suicide", "kill myself", "worthless"]):
        return "depressed"
    elif polarity < -0.3:
        return "depressed"
    elif polarity < -0.05:
        return "sad"
    elif polarity < 0.2:
        return "neutral"
    elif polarity < 0.6:
        return "happy"
    else:
        return "joyful"

def display_results(mood):
    st.subheader(f"Your detected mood is: {mood.upper()} ✨")

    # Show gif
    st.image(random.choice(mood_gifs[mood]), use_column_width=True)

    # Show quote
    st.success(random.choice(mood_quotes[mood]))

    # Show media links
    if mood in ["depressed", "sad"]:
        st.markdown("[🎵 Comforting Music Playlist](https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro)")
        st.markdown("[📽 Uplifting YouTube Video](https://www.youtube.com/watch?v=ZJZpFT8bAP8)")
    elif mood == "happy" or mood == "joyful":
        st.markdown("[🎶 Happy Vibes Spotify](https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC)")
        st.markdown("[🎥 Celebrate Your Mood](https://www.youtube.com/watch?v=d-diB65scQU)")
    else:
        st.markdown("[🌉 Chill Playlist](https://open.spotify.com/playlist/37i9dQZF1DX4WYpdgoIcn6)")

# ------------------ Question Flow ------------------
if 'step' not in st.session_state:
    st.session_state.step = 0

def next_question():
    if st.session_state.step < len(questions):
        st.session_state.step += 1

# ------------------ UI Start ------------------
st.title("\U0001F9E0 Conversational Mood Detector")
st.markdown("""
    <div style='text-align: center;'>
        <h4>Let's talk and discover how you're truly feeling 😊</h4>
    </div>
""", unsafe_allow_html=True)

if st.session_state.step < len(questions):
    st.markdown(f"**{questions[st.session_state.step]}**")
    st.text_input("Your response:",
                  key=f"input_{st.session_state.step}",
                  on_change=next_question,
                  label_visibility="collapsed")
else:
    mood_result = analyze_mood()
    display_results(mood_result)

