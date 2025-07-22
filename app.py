# app.py

import streamlit as st
from textblob import TextBlob
import random

# ------------------ Extended Mood Data ------------------ #
mood_data = {
    "joyful": {
        "quotes": [
            "Joy is the simplest form of gratitude 🌈",
            "Live life to the fullest and make every moment count! 🎉",
            "Smile more, worry less 😊",
            "Each day is a new beginning 🌞",
            "Gratitude turns what we have into enough 🙏",
            "Choose happiness over fear 🌸",
            "Today is a good day for a good day 💫",
            "Laughter is an instant vacation 😂",
            "The purpose of our lives is to be happy 😄",
            "Celebrate small victories 🥳",
            "Positive mind. Positive vibes. Positive life ✨",
            "Shine like the whole universe is yours ✨",
            "Life is short, smile while you still have teeth 😁",
            "Let your joy burst forth like flowers in spring 🌷",
            "Stay close to people who feel like sunlight ☀️",
            "Do more of what makes you happy 🎈",
            "Happiness blooms from within 🌼",
            "Joy multiplies when shared 💕",
            "You're someone's reason to smile 😊",
            "Your vibe attracts your tribe ✨",
            "Look for something positive in each day 🌟",
            "You deserve all the good things 🌠",
            "The sun is shining and so are you 🌞",
            "Nothing can dim the light within you 💡",
            "Live simply. Dream big. Be grateful 🌈",
            "Good energy is contagious 🔋",
            "Let joy be your compass 🧭",
            "Wake up. Be kind. Repeat 💖",
            "The best is yet to come 🎉",
            "Smile, it's free therapy 😃"
        ],
        "jokes": [
            "Why do bees have sticky hair? Because they use honeycombs! 🐝",
            "What do you call a singing computer? A Dell! 🎤"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=3GwjfUFyY6M",
            "https://www.youtube.com/watch?v=ZbZSe6N_BXs",
            "https://www.youtube.com/watch?v=9NjKgV65fpo",
            "https://www.youtube.com/watch?v=d-diB65scQU"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DXdPec7aLTmlC",
            "https://open.spotify.com/playlist/37i9dQZF1DWU0ScTcjJBdj"
        ],
        "gifs": [
            "https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif",
            "https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif"
        ]
    },
    "depressed": {
        "quotes": [
            "You're not alone. This too shall pass. 🌧",
            "Every storm runs out of rain. 🌦",
            "You are stronger than you think 💪",
            "Feelings are just visitors. Let them come and go 🧠",
            "Your story isn't over yet 💜",
            "Breathe in peace, breathe out anxiety 🌬️",
            "One step at a time 🐾",
            "Asking for help is a strength, not weakness 🤝",
            "You matter. Always have, always will 🌟",
            "There is hope, even when your brain tells you there isn’t 💫"
        ],
        "jokes": [
            "Why did the chicken go to therapy? To get to the other side of its emotions 🐔",
            "What's a depressed person's favorite food? Anything with serotonin 😅"
        ],
        "youtube": [
            "https://www.youtube.com/watch?v=w6T02g5hnT4",
            "https://www.youtube.com/watch?v=2vEStDd6HVY",
            "https://www.youtube.com/watch?v=ZToicYcHIOU"
        ],
        "spotify": [
            "https://open.spotify.com/playlist/37i9dQZF1DWVrtsSlLKzro",
            "https://open.spotify.com/playlist/37i9dQZF1DWXLeA8Omikj7"
        ],
        "gifs": [
            "https://media.giphy.com/media/l0HlJzQ9312VRFMBW/giphy.gif"
        ]
    },
    # Add similar expansions for happy, sad, angry, and neutral...
}

questions = [
    "How are you feeling today in one word?",
    "What happened today that affected your mood?",
    "What's something on your mind right now?",
    "How do you feel physically and mentally right now?",
    "If you could change one thing about your day, what would it be?"
]

if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "responses" not in st.session_state:
    st.session_state.responses = []
if "user_input" not in st.session_state:
    st.session_state.user_input = ""

def advance():
    if st.session_state.user_input.strip():
        st.session_state.responses.append(st.session_state.user_input.strip())
        st.session_state.q_index += 1
        st.session_state.user_input = ""

def detect_mood(texts):
    combined = " ".join(texts).lower()
    keywords = ["depressed", "hopeless", "suicidal", "worthless", "numb", "empty", "i want to die", "kill myself"]
    if any(k in combined for k in keywords):
        return "depressed"
    polarity = sum(TextBlob(t).sentiment.polarity for t in texts) / len(texts)
    if polarity >= 0.5:
        return "joyful"
    elif 0.2 <= polarity < 0.5:
        return "happy"
    elif -0.2 < polarity < 0.2:
        return "neutral"
    elif -0.6 < polarity <= -0.2:
        return "sad"
    else:
        return "depressed"

st.set_page_config(page_title="Mood Detector AI 🎭", layout="centered")
st.title("🧠 Conversational Mood Detector")

q_index = st.session_state.q_index
if q_index < len(questions):
    st.subheader(f"Q{q_index + 1}: {questions[q_index]}")
    st.text_input("",
        key="user_input",
        placeholder="Type your response and press Enter...",
        on_change=advance
    )
else:
    mood = detect_mood(st.session_state.responses)
    data = mood_data.get(mood, mood_data["neutral"])

    st.balloons()
    st.success(f"🎯 Detected Mood: **{mood.upper()}**")
    st.image(random.choice(data["gifs"]), use_container_width=True)

    st.subheader("💬 Motivation")
    for quote in random.sample(data["quotes"], min(3, len(data["quotes"]))):
        st.info(quote)

    st.subheader("🎧 Spotify")
    for link in data["spotify"]:
        st.markdown(f"[🎵 Open Playlist]({link})")

    st.subheader("📺 YouTube")
    for link in random.sample(data["youtube"], min(3, len(data["youtube"]))):
        st.markdown(f"[▶ Watch Video]({link})")

    st.subheader("😂 Joke")
    st.write(random.choice(data["jokes"]))

    if st.button("🔁 Start Again"):
        st.session_state.q_index = 0
        st.session_state.responses = []
        st.session_state.user_input = ""
        st.experimental_rerun()
