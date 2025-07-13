import streamlit as st
from textblob import TextBlob
import random

# Multi-question form
questions = [
    "How are you feeling today in one word?",
    "What made you feel this way?",
    "Describe your current thoughts in a sentence.",
    "What's one thing you wish could be different right now?"
]

# Mood data
mood_data = {
    "happy": {
        "quotes": [
            "Keep smiling, because life is a beautiful thing!",
            "Happiness is not out there, it's in you."
        ],
        "jokes": [
            "Why don’t scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!"
        ],
        "music": [
            "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",  # Happy Hits!
            "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"   # Good Vibes
        ]
    },
    "sad": {
        "quotes": [
            "It’s okay to not be okay.",
            "Tough times never last, but tough people do."
        ],
        "jokes": [
            "Why did the computer visit the therapist? It had too many bytes of sadness.",
            "Why did the math book look sad? Because it had too many problems."
        ],
        "music": [
            "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",  # Life Sucks
            "https://open.spotify.com/playlist/37i9dQZF1DX7gIoKXt0gmx"   # Sad Vibes
        ]
    },
    "angry": {
        "quotes": [
            "Calm is a superpower.",
            "Speak when you’re angry, and you’ll make the best speech you’ll ever regret."
        ],
        "jokes": [
            "Why don’t skeletons fight each other? They don’t have the guts.",
            "I'm not arguing, I'm just explaining why I'm right!"
        ],
        "music": [
            "https://open.spotify.com/playlist/37i9dQZF1DX76Wlfdnj7AP",  # Rock Hard
            "https://open.spotify.com/playlist/37i9dQZF1DX1tyCD9QhIWF"   # Angry Rock
        ]
    },
    "neutral": {
        "quotes": [
            "Every day may not be good, but there's good in every day.",
            "Stay grounded. Everything will fall into place."
        ],
        "jokes": [
            "What did one wall say to the other? I’ll meet you at the corner.",
            "Why can’t your nose be 12 inches long? Because then it would be a foot!"
        ],
        "music": [
            "https://open.spotify.com/playlist/37i9dQZF1DX6VdMW310YC7",  # Chill Vibes
            "https://open.spotify.com/playlist/37i9dQZF1DWUvHZA1zLcjW"   # Lo-Fi Beats
        ]
    }
}

# Combine polarity from multiple answers
def detect_mood_from_responses(responses):
    total_polarity = 0
    for r in responses:
        total_polarity += TextBlob(r).sentiment.polarity
    avg_polarity = total_polarity / len(responses)

    if avg_polarity > 0.2:
        return "happy"
    elif avg_polarity < -0.2:
        return "sad"
    elif -0.2 <= avg_polarity <= 0.2:
        return "neutral"
    else:
        return "angry"

# Streamlit UI
st.set_page_config(page_title="Conversational Mood Detector", layout="centered")
st.title("🧠 Conversational Mood Detector")
st.markdown("Let's understand how you're feeling today. Answer a few quick questions 👇")

responses = []
with st.form("mood_form"):
    for q in questions:
        responses.append(st.text_input(q, key=q))
    submitted = st.form_submit_button("Analyze Mood")

if submitted and all(responses):
    mood = detect_mood_from_responses(responses)
    st.success(f"Detected Mood: **{mood.capitalize()}**")

    st.subheader("💬 Motivational Quote")
    st.info(random.choice(mood_data[mood]["quotes"]))

    st.subheader("🎧 Spotify Playlist Suggestions")
    for link in mood_data[mood]["music"]:
        st.markdown(f"[Listen here]({link})")

    st.subheader("😂 Here's a joke for you")
    st.write(random.choice(mood_data[mood]["jokes"]))

