import streamlit as st
from transformers import pipeline
import random

# Sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Mood-specific keywords
depression_keywords = ["depressed", "suicide", "worthless", "hopeless", "self-harm", "kill myself", "ending it"]

# Question bank
questions = [
    "How are you feeling right now (one word)?",
    "What made you feel that way today?",
    "Did something recently happen that affected your mood?",
    "How is your energy level right now?",
    "Would you rather talk to someone or be alone?",
    "What’s one word to describe your week?",
]

# Mood-based quotes
motivational_quotes = {
    "joyful": [
        "Happiness is not by chance, but by choice.",
        "Smile, breathe, and go slowly.",
        "Do more things that make you forget to check your phone.",
        "Joy is the simplest form of gratitude.",
        "Today is a good day to have a good day!",
        "The most wasted of all days is one without laughter.",
        "Be happy for this moment. This moment is your life.",
        "Every day brings new choices.",
        "Let your smile change the world.",
        "Choose happiness over everything.",
    ] * 3,  # Multiplied to ensure rotation
    "sad": [
        "This too shall pass.",
        "You are stronger than you think.",
        "Storms don’t last forever.",
        "Crying doesn’t indicate weakness.",
        "Even the darkest night will end and the sun will rise.",
        "You’ve survived 100% of your bad days so far.",
        "Pain is temporary. Keep going.",
        "You grow through what you go through.",
        "You’re allowed to scream, just never give up.",
        "Feel it. Heal it. Let it go.",
    ] * 3,
    "neutral": [
        "Balance is the key to everything.",
        "Some days are just days. And that’s okay.",
        "Stillness is not weakness.",
        "Every day may not be good, but there is good in every day.",
        "Progress is progress no matter how small.",
        "You are doing better than you think.",
        "Small steps every day.",
        "It's okay to pause. Just don’t stop.",
        "Life isn’t perfect, but it has perfect moments.",
        "The middle path is often the most powerful.",
    ] * 3,
    "depressed": [
        "You are not alone. Please talk to someone you trust.",
        "You matter. Always.",
        "It’s okay to ask for help.",
        "Don’t give up. The beginning is always the hardest.",
        "Even broken crayons still color.",
        "Your story isn’t over yet.",
        "Breathe. You’ve got this.",
        "Reach out. There is help.",
        "Darkness doesn’t define you. Hope does.",
        "Please be kind to yourself today.",
    ] * 3,
}

# Spotify playlists
spotify_links = {
    "joyful": [
        "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
        "https://open.spotify.com/playlist/37i9dQZF1DX3rxVfibe1L0",
        "https://open.spotify.com/playlist/37i9dQZF1DX9XIFQuFvzM4",
    ],
    "sad": [
        "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro",
        "https://open.spotify.com/playlist/37i9dQZF1DWX83CujKHHOn",
        "https://open.spotify.com/playlist/37i9dQZF1DX7qK8ma5wgG1",
    ],
    "neutral": [
        "https://open.spotify.com/playlist/37i9dQZF1DWT7XSlwvR1ar",
        "https://open.spotify.com/playlist/37i9dQZF1DX4E3UdUs7fUx",
        "https://open.spotify.com/playlist/37i9dQZF1DWXLeA8Omikj7",
    ],
    "depressed": [
        "https://open.spotify.com/playlist/37i9dQZF1DX7QOv5kjbU68",
        "https://open.spotify.com/playlist/37i9dQZF1DX3YSRoSdA634",
        "https://open.spotify.com/playlist/37i9dQZF1DWU0ScTcjJBdj",
    ],
}

# YouTube links
youtube_links = {
    "joyful": [
        "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
        "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
    ],
    "sad": [
        "https://www.youtube.com/watch?v=ho9rZjlsyYY",
        "https://www.youtube.com/watch?v=RB-RcX5DS5A",
    ],
    "neutral": [
        "https://www.youtube.com/watch?v=5qap5aO4i9A",
        "https://www.youtube.com/watch?v=DWcJFNfaw9c",
    ],
    "depressed": [
        "https://www.youtube.com/watch?v=wnHW6o8WMas",
        "https://www.youtube.com/watch?v=1vx8iUvfyCY",
    ],
}

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 0
if "responses" not in st.session_state:
    st.session_state.responses = []

# Title
st.title("🧠 Conversational Mood Detector")
st.markdown("Let’s have a quick conversation to understand how you're feeling today. 😊")

# Handle Q&A
if st.session_state.step < len(questions):
    question = questions[st.session_state.step]
    user_input = st.text_input(f"**Q{st.session_state.step + 1}: {question}**", key=f"q{st.session_state.step}")
    if user_input:
        st.session_state.responses.append(user_input)
        st.session_state.step += 1
        st.experimental_rerun()
else:
    # Join all responses into one text
    full_text = " ".join(st.session_state.responses).lower()

    # Detect depressed keywords first
    if any(word in full_text for word in depression_keywords):
        mood = "depressed"
    else:
        result = sentiment_pipeline(full_text)[0]
        label = result["label"]
        if label == "POSITIVE":
            mood = "joyful"
        elif label == "NEGATIVE":
            mood = "sad"
        else:
            mood = "neutral"

    # Show mood
    st.subheader(f"🌀 Detected Mood: `{mood.upper()}`")

    # Show quote
    quote = random.choice(motivational_quotes[mood])
    st.info(f"💬 **Motivational Quote:** _{quote}_")

    # Spotify
    st.markdown("🎵 **Listen on Spotify:**")
    for link in spotify_links[mood][:3]:
        st.markdown(f"- [Open Playlist]({link})")

    # YouTube
    st.markdown("📺 **Watch on YouTube:**")
    for link in youtube_links[mood][:2]:
        st.markdown(f"- [Open Video]({link})")

    st.success("Thank you for sharing! 💖")

