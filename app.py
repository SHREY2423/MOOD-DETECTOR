import streamlit as st
from textblob import TextBlob
import random

st.set_page_config(page_title="Conversational Mood Detector", layout="centered")

# ========== Data ==========
questions = [
    "How are you feeling right now in one word?",
    "What has been bothering you lately?",
    "When did you last feel genuinely happy?",
    "Do you feel heard and understood?",
    "What would make your day better today?",
    "Any thoughts you want to share?"
]

mood_keywords = {
    "depressed": ["depressed", "suicide", "hopeless", "worthless", "end my life", "tired of life"],
    "sad": ["sad", "upset", "hurt", "cry", "lonely"],
    "happy": ["happy", "joy", "excited", "great", "amazing"],
    "neutral": ["okay", "fine", "normal", "good"]
}

motivational_quotes = {
    "depressed": [
        "You are not alone. Keep going.",
        "This too shall pass.",
        "Your story isn't over yet.",
        "Dark times make the light brighter.",
        "You are stronger than your thoughts."
    ],
    "sad": [
        "Tears are words the heart can’t say.",
        "Every storm runs out of rain.",
        "Keep your face toward the sunshine.",
        "Let it out, and then let it go.",
        "Healing takes time. You're doing fine."
    ],
    "happy": [
        "Keep shining, you're doing amazing!",
        "Happiness looks great on you.",
        "Enjoy every moment!",
        "Spread the joy!",
        "Keep smiling 😄"
    ],
    "neutral": [
        "Stay steady and focused.",
        "Every day is a fresh start.",
        "Breathe. You're doing fine.",
        "Calm is a superpower.",
        "Balance is key to everything."
    ]
}

mood_gifs = {
    "depressed": "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
    "sad": "https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif",
    "happy": "https://media.giphy.com/media/1BdIPQHXOfB7fziT5I/giphy.gif",
    "neutral": "https://media.giphy.com/media/3ohc1fQ1pFZnp6BEX2/giphy.gif"
}

spotify_links = {
    "depressed": "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0",
    "sad": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
    "happy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
    "neutral": "https://open.spotify.com/playlist/37i9dQZF1DWUvHZA1zLcjW"
}

# ========== Functions ==========
def detect_mood(responses):
    text = " ".join(responses).lower()
    for mood, keywords in mood_keywords.items():
        if any(word in text for word in keywords):
            return mood
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment < -0.4:
        return "depressed"
    elif sentiment < 0:
        return "sad"
    elif sentiment > 0.3:
        return "happy"
    else:
        return "neutral"

# ========== Session State ==========
if "step" not in st.session_state:
    st.session_state.step = 0
if "responses" not in st.session_state:
    st.session_state.responses = []

# ========== UI ==========
st.markdown("<h1 style='text-align: center;'>🧠 Conversational Mood Detector</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Let's talk and discover how you're truly feeling 😊</h3>", unsafe_allow_html=True)

if st.session_state.step < len(questions):
    st.markdown(f"**{questions[st.session_state.step]}**")
    answer = st.text_input("Your answer:", key=f"q_{st.session_state.step}")
    if st.button("Next"):
        if answer.strip():
            st.session_state.responses.append(answer)
            st.session_state.step += 1
else:
    mood = detect_mood(st.session_state.responses)
    st.subheader(f"🌈 Your mood is detected as: **{mood.upper()}**")
    st.image(mood_gifs[mood], use_column_width=True)
    st.success(random.choice(motivational_quotes[mood]))
    st.markdown(f"[🎧 Listen on Spotify]({spotify_links[mood]})")
    st.markdown("🔄 Want to restart the conversation?")
    if st.button("Start Over"):
        st.session_state.step = 0
        st.session_state.responses = []
