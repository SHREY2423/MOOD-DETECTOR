import streamlit as st
from textblob import TextBlob
import random

# ------------------ Mood Data ------------------
mood_data = {
    "happy": {
        "quote": "Happiness is not something ready made. It comes from your own actions.",
        "joke": "Why don’t scientists trust atoms? Because they make up everything!",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        "gif": "https://media.giphy.com/media/yoJC2Olx0ekMy2nX7W/giphy.gif"
    },
    "sad": {
        "quote": "Tough times never last, but tough people do.",
        "joke": "Why did the sad man bring a ladder to the bar? Because he was going through some ups and downs.",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
        "gif": "https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif"
    },
    "depressed": {
        "quote": "This too shall pass. You are stronger than you think.",
        "joke": "Why don’t skeletons fight each other? They don’t have the guts.",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634",
        "gif": "https://media.giphy.com/media/3o6ZsYm5Xx2Z4qNf0k/giphy.gif"
    },
    "neutral": {
        "quote": "Keep going. Everything you need will come to you at the perfect time.",
        "joke": "Why did the computer show up at work late? It had a hard drive!",
        "spotify": "https://open.spotify.com/playlist/37i9dQZF1DWYBO1MoTDhZI",
        "gif": "https://media.giphy.com/media/jUwpNzg9IcyrK/giphy.gif"
    }
}

# ------------------ App UI ------------------
st.set_page_config(page_title="Conversational Mood Detector", layout="centered", initial_sidebar_state="auto")

st.title("🧠 Conversational Mood Detector")
st.markdown("Hi there! Let's talk and understand how you're feeling today 😊")

questions = [
    "How are you feeling right now in one word?",
    "What was the best part of your day?",
    "Did anything upset you recently?",
    "How are you feeling about tomorrow?",
    "Describe your current energy level."
]

responses = []

for q in questions:
    answer = st.text_input(q, key=q)
    if answer:
        responses.append(answer)
    else:
        break

# ------------------ Mood Prediction ------------------
def predict_mood(answers):
    full_text = " ".join(answers)
    sentiment = TextBlob(full_text).sentiment.polarity

    if sentiment > 0.4:
        return "happy"
    elif 0.1 < sentiment <= 0.4:
        return "neutral"
    elif -0.4 < sentiment <= 0.1:
        return "sad"
    else:
        return "depressed"

if len(responses) == len(questions):
    mood = predict_mood(responses)
    st.success(f"🎯 Your mood is: **{mood.upper()}**")

    data = mood_data[mood]
    st.image(data["gif"], width=300)
    st.markdown(f"💬 **Quote:** _{data['quote']}_")
    st.markdown(f"😂 **Joke:** {data['joke']}")
    st.markdown(f"🎵 **Music for you:** [Listen on Spotify]({data['spotify']})")

