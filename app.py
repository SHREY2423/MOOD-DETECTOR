import streamlit as st
from textblob import TextBlob
import time

# Mood-based content
mood_quotes = {
    "happy": [
        "Keep smiling, because life is a beautiful thing!",
        "The purpose of our lives is to be happy.",
    ],
    "sad": [
        "Tough times never last, but tough people do.",
        "Stars can't shine without darkness.",
    ],
    "neutral": [
        "Be present in all things and thankful for all things.",
        "Neutral today? Let tomorrow be brighter.",
    ],
    "depressed": [
        "You're not alone. You matter. Keep going.",
        "The darkest nights produce the brightest stars.",
    ],
}

spotify_links = {
    "happy": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
    "sad": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
    "neutral": "https://open.spotify.com/playlist/37i9dQZF1DWU0ScTcjJBdj",
    "depressed": "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634",
}

youtube_links = {
    "happy": "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
    "sad": "https://www.youtube.com/watch?v=ho9rZjlsyYY",
    "neutral": "https://www.youtube.com/watch?v=lTRiuFIWV54",
    "depressed": "https://www.youtube.com/watch?v=1rD8yc8yKiY",
}

sensitive_words = ["depressed", "suicide", "hopeless", "worthless", "kill myself", "end it all", "give up"]

questions = [
    "How are you feeling right now in one word?",
    "What made you feel this way?",
    "Do you want to talk about your day?",
    "What’s the one thing on your mind right now?",
    "Do you feel energetic or tired?",
]

# Session state to store responses
if "step" not in st.session_state:
    st.session_state.step = 0
if "responses" not in st.session_state:
    st.session_state.responses = []

st.title("🧠 Conversational Mood Detector")

if st.session_state.step < len(questions):
    st.write(f"**Q{st.session_state.step+1}:** {questions[st.session_state.step]}")
    answer = st.text_input("Your response", key=f"q{st.session_state.step}")

    if answer:
        st.session_state.responses.append(answer)
        st.session_state.step += 1
        time.sleep(0.3)
        st.experimental_rerun()

elif st.session_state.step == len(questions):
    full_text = " ".join(st.session_state.responses).lower()
    mood = "neutral"
    
    # Check for sensitive keywords
    if any(word in full_text for word in sensitive_words):
        mood = "depressed"
    else:
        analysis = TextBlob(full_text).sentiment
        if analysis.polarity > 0.3:
            mood = "happy"
        elif analysis.polarity < -0.3:
            mood = "sad"
        else:
            mood = "neutral"

    st.subheader(f"🪄 Detected Mood: **{mood.upper()}**")
    st.write(f"💬 _{mood_quotes[mood][0]}_")
    st.write(f"💬 _{mood_quotes[mood][1]}_")

    st.markdown("---")
    st.markdown(f"[🎵 Listen on Spotify]({spotify_links[mood]})", unsafe_allow_html=True)
    st.markdown(f"[📺 Watch on YouTube]({youtube_links[mood]})", unsafe_allow_html=True)
    
    st.markdown("🔁 Click below to restart the conversation.")
    if st.button("Start Again"):
        st.session_state.step = 0
        st.session_state.responses = []
        st.experimental_rerun()

