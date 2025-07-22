import streamlit as st
from textblob import TextBlob
import random
import time

# ----- MOTIVATIONAL QUOTES -----
motivational_quotes = {
    "happy": [
        "Happiness is not out there, it's in you.",
        "Smile, it's your superpower!",
        "Joy is the simplest form of gratitude.",
        "Celebrate the small wins.",
        "Happiness radiates like the fragrance from a flower.",
        "The purpose of life is to be happy.",
        "Create your own sunshine.",
        "Happiness is a direction, not a place.",
        "You deserve all the good things.",
        "Keep smiling, you're amazing!"
    ],
    "sad": [
        "It's okay to feel sad. Healing starts with acceptance.",
        "Tough times never last, but tough people do.",
        "You’re stronger than you think.",
        "This moment will pass.",
        "Don’t give up now, you’ve come so far.",
        "Your feelings are valid.",
        "Take it one day at a time.",
        "Crying isn’t a weakness, it’s strength.",
        "You matter, even on the hardest days.",
        "Pain is temporary. Strength is forever."
    ],
    "depressed": [
        "You are not alone. Help is always available.",
        "Speak up. Someone cares.",
        "Your life matters.",
        "You’ve survived 100% of your bad days.",
        "This is not the end. Brighter days are ahead.",
        "Take a deep breath. You are enough.",
        "One step at a time. You’ve got this.",
        "Please talk to someone. You're important.",
        "You are not your thoughts.",
        "Hope is real. Recovery is possible."
    ],
    "neutral": [
        "Even a calm day is a blessing.",
        "Use this time to refocus.",
        "Pause. Breathe. Reflect.",
        "You are in control of your direction.",
        "Balance is key to everything.",
        "Neutral moments give space for growth.",
        "Sometimes no mood is a mood too.",
        "Let stillness speak.",
        "Today is a blank canvas.",
        "Progress, even in silence."
    ]
}

# ----- SPOTIFY AND YOUTUBE LINKS -----
media_recommendations = {
    "happy": {
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
            "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs",  # Happy - Pharrell
            "https://www.youtube.com/watch?v=OPf0YbXqDm0"   # Uptown Funk
        ]
    },
    "sad": {
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
            "https://open.spotify.com/playlist/37i9dQZF1DX7gIoKXt0gmx"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=J_ub7Etch2U",  # Fix You - Coldplay
            "https://www.youtube.com/watch?v=uelHwf8o7_U"   # Love The Way You Lie
        ]
    },
    "depressed": {
        "spotify": [
            "https://open.spotify.com/playlist/1rqqCSm0Qe4I9rUvWncaom",
            "https://open.spotify.com/playlist/2FQyEcNfb52wYISgVLzYZd"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=VN6c4hN_NL8",  # Motivational Speech
            "https://www.youtube.com/watch?v=mgmVOuLgFB0"   # Rise Again
        ]
    },
    "neutral": {
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DXc2aPBXGmXrt",
            "https://open.spotify.com/playlist/37i9dQZF1DWUvHZA1zLcjW"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=2vjPBrBU-TM",  # Chandelier - Sia
            "https://www.youtube.com/watch?v=6hzrDeceEKc"   # Wonderwall - Oasis
        ]
    }
}

# ----- INIT -----
st.set_page_config(page_title="Conversational Mood Detector", layout="centered")
st.title("🧠 Conversational Mood Detector")
st.write("Let's talk and understand how you're feeling today.")

# ----- QUESTIONS -----
questions = [
    "1️⃣ How are you feeling right now in one word?",
    "2️⃣ What kind of thoughts are you having today?",
    "3️⃣ Have you felt this way recently?",
    "4️⃣ What's the reason behind your mood today?",
    "5️⃣ Describe your current mental energy: High / Medium / Low?"
]

if "answers" not in st.session_state:
    st.session_state.answers = []
if "step" not in st.session_state:
    st.session_state.step = 0

if st.session_state.step < len(questions):
    answer = st.text_input(questions[st.session_state.step], key=f"q{st.session_state.step}")
    if answer:
        st.session_state.answers.append(answer)
        st.session_state.step += 1
        st.experimental_rerun()
else:
    full_text = " ".join(st.session_state.answers).lower()
    
    # Detect 'depressed' keywords
    depressed_keywords = ['depressed', 'suicide', 'worthless', 'hopeless', 'end it', 'kill myself']
    if any(word in full_text for word in depressed_keywords):
        mood = "depressed"
    else:
        blob = TextBlob(full_text)
        polarity = blob.sentiment.polarity
        if polarity > 0.2:
            mood = "happy"
        elif polarity < -0.2:
            mood = "sad"
        else:
            mood = "neutral"

    st.subheader(f"🧠 Detected Mood: **{mood.capitalize()}**")

    # Show quote
    quote = random.choice(motivational_quotes[mood])
    st.success(f"💬 {quote}")

    # Show media
    st.markdown("### 🎧 Recommended Spotify Playlist:")
    for link in media_recommendations[mood]["spotify"]:
        st.markdown(f"- [Listen here]({link})")

    st.markdown("### 📺 Recommended YouTube Videos:")
    for link in media_recommendations[mood]["youtube"]:
        st.markdown(f"- [Watch here]({link})")

    # Restart Option
    if st.button("🔁 Restart Conversation"):
        st.session_state.answers = []
        st.session_state.step = 0
        st.experimental_rerun()

