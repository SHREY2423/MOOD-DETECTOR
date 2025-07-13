import streamlit as st
from textblob import TextBlob
import random

# Mood-based data
mood_quotes = {
    "happy": [
        "Keep smiling, because life is a beautiful thing!",
        "Happiness is not out there, it's in you."
    ],
    "sad": [
        "It's okay to not be okay. You're not alone.",
        "Tough times never last, but tough people do."
    ],
    "angry": [
        "Take a deep breath. Calm is a superpower.",
        "Speak when you are angry and you’ll make the best speech you’ll ever regret."
    ],
    "neutral": [
        "Every day may not be good, but there is something good in every day.",
        "Stay grounded. Everything will fall into place."
    ]
}

mood_music = {
    "happy": ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake"],
    "sad": ["Someone Like You - Adele", "Fix You - Coldplay"],
    "angry": ["Stronger - Kanye West", "Numb - Linkin Park"],
    "neutral": ["Weightless - Marconi Union", "Clair de Lune - Debussy"]
}

# Mood detection logic
def detect_mood(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.2:
        return "happy"
    elif polarity < -0.2:
        return "sad"
    elif -0.2 <= polarity <= 0.2:
        return "neutral"
    else:
        return "angry"

# App layout
st.set_page_config(page_title="AI Mood Detector", layout="centered")
st.title("🧠 Conversational Mood Detector")
st.markdown("Hi there! Let's talk and understand how you're feeling today 😊")

user_input = st.text_input("How are you feeling right now? (Say it in one sentence)", "")

if user_input:
    mood = detect_mood(user_input)
    st.success(f"Detected Mood: **{mood.capitalize()}** 😄" if mood == "happy" else
               f"Detected Mood: **{mood.capitalize()}** 😐" if mood == "neutral" else
               f"Detected Mood: **{mood.capitalize()}** 😔")

    st.subheader("💡 Uplifting Quote")
    st.info(random.choice(mood_quotes[mood]))

    st.subheader("🎵 Music Recommendation")
    for track in mood_music[mood]:
        st.write(f"- {track}")

